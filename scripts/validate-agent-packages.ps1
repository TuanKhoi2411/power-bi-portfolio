param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'
$failures = [System.Collections.Generic.List[string]]::new()

$projects = @(
    @{ Name = 'sales-performance'; Mode = 'pbip'; Source = 'data/Online Retail.xlsx'; Entry = 'dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip' },
    @{ Name = 'marketing-performance'; Mode = 'pbip'; Source = 'data/bank-additional-full.csv'; Entry = 'dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip' },
    @{ Name = 'finance-performance'; Mode = 'pbip'; Source = 'data/sec-aapl-companyfacts.json'; Entry = 'dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip' },
    @{ Name = 'financial-performance-dashboard'; Mode = 'pbix'; Entry = 'Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix' }
)

$requiredAgentFiles = @(
    'AGENTS.md',
    'agent/BUILD_PROMPT.md',
    'agent/DATA_MODEL_SPEC.md',
    'agent/REPORT_SPEC.md',
    'agent/BUILD_AND_QA.md'
)

$requiredPbipDocumentation = @(
    'BI_Dashboard_Creation_Prompt.md',
    'docs/creation_history.md',
    'model/data_dictionary.md',
    'model/measure_catalog.csv',
    'model/measures.dax',
    'model/metric_definitions.md',
    'model/relationship_map.md',
    'model/semantic_model_notes.md',
    'powerbi/PBIX_build_instructions.md',
    'powerbi/PowerQuery_M.txt',
    'qa/qa_checklist.md',
    'qa/structural_validation.json',
    'qa/validation_results.md'
)

foreach ($project in $projects) {
    $projectRoot = Join-Path $RepositoryRoot "projects/$($project.Name)"
    foreach ($relativePath in $requiredAgentFiles + @('README.md', $project.Entry)) {
        $candidate = Join-Path $projectRoot $relativePath
        if (-not (Test-Path -LiteralPath $candidate)) {
            $failures.Add("Missing required artifact: projects/$($project.Name)/$relativePath")
        }
    }

    if ($project.Mode -eq 'pbip') {
        foreach ($relativePath in $requiredPbipDocumentation) {
            $candidate = Join-Path $projectRoot $relativePath
            if (-not (Test-Path -LiteralPath $candidate)) {
                $failures.Add("Missing detailed PBIP documentation: projects/$($project.Name)/$relativePath")
            }
        }
        $sourcePath = Join-Path $projectRoot $project.Source
        if (-not (Test-Path -LiteralPath $sourcePath)) {
            $failures.Add("Missing source for rebuildable project: projects/$($project.Name)/$($project.Source)")
        }
    }
}

Get-ChildItem -Path $RepositoryRoot -Recurse -Filter '*.md' | ForEach-Object {
    $markdownFile = $_
    $content = Get-Content -LiteralPath $markdownFile.FullName -Raw
    [regex]::Matches($content, '\]\((?!https?://|mailto:|#)([^)]+)\)') | ForEach-Object {
        $encodedTarget = $_.Groups[1].Value.Split('#')[0]
        if (-not $encodedTarget) { return }
        $target = [Uri]::UnescapeDataString($encodedTarget)
        $resolved = Join-Path $markdownFile.DirectoryName $target
        if (-not (Test-Path -LiteralPath $resolved)) {
            $relativeMarkdown = $markdownFile.FullName.Substring($RepositoryRoot.Length + 1)
            $failures.Add("Broken Markdown link in ${relativeMarkdown}: $encodedTarget")
        }
    }
}

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host "Agent package validation passed for $($projects.Count) projects."
