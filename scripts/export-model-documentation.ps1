param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$projects = @(
    @{
        Name = 'sales-performance'
        Model = 'dashboard/UK_Online_Retail_Sales.SemanticModel/definition'
        Fact = 'tables/FactSales.tmdl'
        MeasureTable = 'FactSales'
    },
    @{
        Name = 'marketing-performance'
        Model = 'dashboard/Portuguese_Bank_Marketing.SemanticModel/definition'
        Fact = 'tables/FactMarketing.tmdl'
        MeasureTable = 'FactMarketing'
    },
    @{
        Name = 'finance-performance'
        Model = 'dashboard/Apple_Finance.SemanticModel/definition'
        Fact = 'tables/FactFinance.tmdl'
        MeasureTable = 'FactFinance'
    }
)

function Unquote-TmdlName([string]$Name) {
    $trimmed = $Name.Trim()
    if ($trimmed.StartsWith("'") -and $trimmed.EndsWith("'")) {
        return $trimmed.Substring(1, $trimmed.Length - 2).Replace("''", "'")
    }
    return $trimmed
}

function Escape-Markdown([string]$Value) {
    if ($null -eq $Value) { return '' }
    return $Value.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
}

foreach ($project in $projects) {
    $projectRoot = Join-Path $RepositoryRoot "projects/$($project.Name)"
    $modelRoot = Join-Path $projectRoot $project.Model
    $factPath = Join-Path $modelRoot $project.Fact
    $modelDocs = Join-Path $projectRoot 'model'
    $powerBiDocs = Join-Path $projectRoot 'powerbi'
    New-Item -ItemType Directory -Force -Path $modelDocs, $powerBiDocs | Out-Null

    $factLines = Get-Content -LiteralPath $factPath
    $measures = [System.Collections.Generic.List[object]]::new()
    $currentMeasure = $null

    foreach ($line in $factLines) {
        if ($line -match '^\s*measure\s+(.+?)\s*=\s*(.*)$') {
            if ($null -ne $currentMeasure) { $measures.Add([pscustomobject]$currentMeasure) }
            $currentMeasure = @{
                Name = Unquote-TmdlName $Matches[1]
                Expression = $Matches[2].Trim()
                Format = ''
                Folder = ''
            }
            continue
        }
        if ($null -ne $currentMeasure -and $line -match '^\s*formatString:\s*(.*)$') {
            $currentMeasure.Format = $Matches[1].Trim()
            continue
        }
        if ($null -ne $currentMeasure -and $line -match '^\s*displayFolder:\s*(.*)$') {
            $currentMeasure.Folder = $Matches[1].Trim()
            continue
        }
        if ($null -ne $currentMeasure -and $line -match '^\s*(column|partition|hierarchy)\s+') {
            $measures.Add([pscustomobject]$currentMeasure)
            $currentMeasure = $null
        }
    }
    if ($null -ne $currentMeasure) { $measures.Add([pscustomobject]$currentMeasure) }

    $dax = [System.Text.StringBuilder]::new()
    [void]$dax.AppendLine("// Auto-exported from the canonical TMDL semantic model.")
    [void]$dax.AppendLine("// Project: $($project.Name)")
    [void]$dax.AppendLine("// Measure table: $($project.MeasureTable)")
    [void]$dax.AppendLine("// Measure count: $($measures.Count)")
    [void]$dax.AppendLine("// Regenerate with scripts/export-model-documentation.ps1 after TMDL changes.")
    [void]$dax.AppendLine()
    foreach ($measure in $measures) {
        [void]$dax.AppendLine("// Display folder: $($measure.Folder)")
        [void]$dax.AppendLine("// Format string: $($measure.Format)")
        [void]$dax.AppendLine("[$($measure.Name)] = $($measure.Expression)")
        [void]$dax.AppendLine()
    }
    [System.IO.File]::WriteAllText((Join-Path $modelDocs 'measures.dax'), $dax.ToString(), $utf8NoBom)

    $catalog = $measures | Select-Object @{n='table';e={$project.MeasureTable}}, @{n='measure';e={$_.Name}}, @{n='display_folder';e={$_.Folder}}, @{n='format_string';e={$_.Format}}, @{n='expression';e={$_.Expression}} | ConvertTo-Csv -NoTypeInformation
    [System.IO.File]::WriteAllLines((Join-Path $modelDocs 'measure_catalog.csv'), $catalog, $utf8NoBom)

    $dictionaryRows = [System.Collections.Generic.List[object]]::new()
    foreach ($tableFile in Get-ChildItem -LiteralPath (Join-Path $modelRoot 'tables') -Filter '*.tmdl' | Sort-Object Name) {
        $lines = Get-Content -LiteralPath $tableFile.FullName
        $tableName = ''
        $currentColumn = $null
        foreach ($line in $lines) {
            if ($line -match '^table\s+(.+)$') {
                $tableName = Unquote-TmdlName $Matches[1]
                continue
            }
            if ($line -match '^\s*column\s+(.+?)(?:\s*=.*)?$') {
                if ($null -ne $currentColumn) { $dictionaryRows.Add([pscustomobject]$currentColumn) }
                $currentColumn = @{
                    Table = $tableName
                    Column = Unquote-TmdlName $Matches[1]
                    DataType = ''
                    SourceColumn = ''
                    Format = ''
                    SummarizeBy = ''
                }
                continue
            }
            if ($null -ne $currentColumn -and $line -match '^\s*dataType:\s*(.*)$') { $currentColumn.DataType = $Matches[1].Trim(); continue }
            if ($null -ne $currentColumn -and $line -match '^\s*sourceColumn:\s*(.*)$') { $currentColumn.SourceColumn = $Matches[1].Trim(); continue }
            if ($null -ne $currentColumn -and $line -match '^\s*formatString:\s*(.*)$') { $currentColumn.Format = $Matches[1].Trim(); continue }
            if ($null -ne $currentColumn -and $line -match '^\s*summarizeBy:\s*(.*)$') { $currentColumn.SummarizeBy = $Matches[1].Trim(); continue }
            if ($null -ne $currentColumn -and $line -match '^\s*(measure|partition|hierarchy)\s+') {
                $dictionaryRows.Add([pscustomobject]$currentColumn)
                $currentColumn = $null
            }
        }
        if ($null -ne $currentColumn) { $dictionaryRows.Add([pscustomobject]$currentColumn) }
    }

    $dictionary = [System.Text.StringBuilder]::new()
    [void]$dictionary.AppendLine('# Data dictionary')
    [void]$dictionary.AppendLine()
    [void]$dictionary.AppendLine('Auto-exported from the canonical TMDL tables. Business rules and source limitations are documented in `../agent/DATA_MODEL_SPEC.md`.')
    [void]$dictionary.AppendLine()
    [void]$dictionary.AppendLine('| Table | Column | Data type | Source column | Format | Summarization |')
    [void]$dictionary.AppendLine('|---|---|---|---|---|---|')
    foreach ($row in $dictionaryRows) {
        [void]$dictionary.AppendLine("| $(Escape-Markdown $row.Table) | $(Escape-Markdown $row.Column) | $(Escape-Markdown $row.DataType) | $(Escape-Markdown $row.SourceColumn) | $(Escape-Markdown $row.Format) | $(Escape-Markdown $row.SummarizeBy) |")
    }
    [System.IO.File]::WriteAllText((Join-Path $modelDocs 'data_dictionary.md'), $dictionary.ToString(), $utf8NoBom)

    $relationshipsPath = Join-Path $modelRoot 'relationships.tmdl'
    $relationshipText = if (Test-Path -LiteralPath $relationshipsPath) { Get-Content -LiteralPath $relationshipsPath -Raw } else { '# No explicit relationships file is present; the project uses a single analytical table.' }
    $relationshipDoc = "# Relationship map`r`n`r`nCanonical TMDL relationship definition:`r`n`r`n" + '```text' + "`r`n$relationshipText`r`n" + '```' + "`r`n"
    [System.IO.File]::WriteAllText((Join-Path $modelDocs 'relationship_map.md'), $relationshipDoc, $utf8NoBom)

    $partitionIndex = [Array]::FindIndex([string[]]$factLines, [Predicate[string]]{ param($value) $value -match '^\s*partition\s+' })
    if ($partitionIndex -ge 0) {
        $partitionLines = $factLines[$partitionIndex..($factLines.Length - 1)]
        $annotationIndex = [Array]::FindIndex([string[]]$partitionLines, [Predicate[string]]{ param($value) $value -match '^\s*annotation\s+' })
        if ($annotationIndex -gt 0) { $partitionLines = $partitionLines[0..($annotationIndex - 1)] }
        $sourceIndex = [Array]::FindIndex([string[]]$partitionLines, [Predicate[string]]{ param($value) $value -match '^\s*source\s*=' })
        if ($sourceIndex -ge 0 -and $sourceIndex + 1 -lt $partitionLines.Length) {
            $mLines = [string[]]$partitionLines[($sourceIndex + 1)..($partitionLines.Length - 1)]
            $indents = @($mLines | Where-Object { $_.Trim().Length -gt 0 } | ForEach-Object { ([regex]::Match($_, '^\s*')).Value.Length })
            $minimumIndent = ($indents | Measure-Object -Minimum).Minimum
            if ($minimumIndent -gt 0) {
                $mLines = @($mLines | ForEach-Object { if ($_.Length -ge $minimumIndent) { $_.Substring($minimumIndent) } else { '' } })
            }
        } else {
            $mLines = $partitionLines
        }
        $mText = "// Canonical Power Query M exported from TMDL.`r`n// Update SourcePath before refresh on another machine.`r`n`r`n" + ($mLines -join "`r`n") + "`r`n"
        [System.IO.File]::WriteAllText((Join-Path $powerBiDocs 'PowerQuery_M.txt'), $mText, $utf8NoBom)
    }
}

Write-Host 'Exported measures, measure catalogs, data dictionaries, relationship maps, and Power Query partitions for 3 PBIP projects.'
