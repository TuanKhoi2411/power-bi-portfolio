param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$projects = @(
    @{ Name='sales-performance'; Pbip='dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip'; Report='dashboard/UK_Online_Retail_Sales.Report'; Model='dashboard/UK_Online_Retail_Sales.SemanticModel'; Fact='definition/tables/FactSales.tmdl'; Source='data/Online Retail.xlsx' },
    @{ Name='marketing-performance'; Pbip='dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip'; Report='dashboard/Portuguese_Bank_Marketing.Report'; Model='dashboard/Portuguese_Bank_Marketing.SemanticModel'; Fact='definition/tables/FactMarketing.tmdl'; Source='data/bank-additional-full.csv' },
    @{ Name='finance-performance'; Pbip='dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip'; Report='dashboard/Apple_Finance.Report'; Model='dashboard/Apple_Finance.SemanticModel'; Fact='definition/tables/FactFinance.tmdl'; Source='data/sec-aapl-companyfacts.json' }
)

$failed = $false
foreach ($project in $projects) {
    $root = Join-Path $RepositoryRoot "projects/$($project.Name)"
    $pbipPath = Join-Path $root $project.Pbip
    $reportRoot = Join-Path $root $project.Report
    $modelRoot = Join-Path $root $project.Model
    $pagesRoot = Join-Path $reportRoot 'definition/pages'
    $pagesMetadata = Get-Content -LiteralPath (Join-Path $pagesRoot 'pages.json') -Raw | ConvertFrom-Json
    $pageResults = @()

    foreach ($pageDirectory in Get-ChildItem -LiteralPath $pagesRoot -Directory) {
        $pagePath = Join-Path $pageDirectory.FullName 'page.json'
        if (-not (Test-Path -LiteralPath $pagePath)) { continue }
        $page = Get-Content -LiteralPath $pagePath -Raw | ConvertFrom-Json
        $visualTypes = @()
        $visualRoot = Join-Path $pageDirectory.FullName 'visuals'
        if (Test-Path -LiteralPath $visualRoot) {
            foreach ($visualDirectory in Get-ChildItem -LiteralPath $visualRoot -Directory) {
                $visualPath = Join-Path $visualDirectory.FullName 'visual.json'
                if (-not (Test-Path -LiteralPath $visualPath)) { continue }
                $visual = Get-Content -LiteralPath $visualPath -Raw | ConvertFrom-Json
                if ($visual.visual.visualType) { $visualTypes += $visual.visual.visualType }
            }
        }
        $pageResults += [pscustomobject]@{
            name = $page.name
            display_name = $page.displayName
            width = $page.width
            height = $page.height
            report_visual_count = $visualTypes.Count
            visual_types = @($visualTypes | Group-Object | Sort-Object Name | ForEach-Object { [pscustomobject]@{ type=$_.Name; count=$_.Count } })
        }
    }

    $factPath = Join-Path $modelRoot $project.Fact
    $measureCount = ([regex]::Matches((Get-Content -LiteralPath $factPath -Raw), '(?m)^\s*measure\s+')).Count
    $activeExists = $pagesMetadata.activePageName -in $pageResults.name
    $pageOrderValid = @($pagesMetadata.pageOrder | Where-Object { $_ -notin $pageResults.name }).Count -eq 0
    $checks = [ordered]@{
        pbip_exists = Test-Path -LiteralPath $pbipPath
        report_folder_exists = Test-Path -LiteralPath $reportRoot
        semantic_model_folder_exists = Test-Path -LiteralPath $modelRoot
        source_exists = Test-Path -LiteralPath (Join-Path $root $project.Source)
        page_count_is_three = $pageResults.Count -eq 3
        active_page_exists = $activeExists
        page_order_resolves = $pageOrderValid
        every_page_is_1280x720 = @($pageResults | Where-Object { $_.width -ne 1280 -or $_.height -ne 720 }).Count -eq 0
        every_page_has_report_visuals = @($pageResults | Where-Object { $_.report_visual_count -eq 0 }).Count -eq 0
    }
    $passed = @($checks.Values | Where-Object { -not $_ }).Count -eq 0
    if (-not $passed) { $failed = $true }
    $result = [ordered]@{
        project = $project.Name
        generated_at = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ssK')
        status = if ($passed) { 'pass' } else { 'fail' }
        checks = $checks
        measure_count = $measureCount
        active_page_name = $pagesMetadata.activePageName
        page_order = $pagesMetadata.pageOrder
        pages = $pageResults
        scope_note = 'Structural PBIP/PBIR/TMDL validation only. This does not replace refresh, reconciliation, interaction, or Power BI Desktop reopen QA.'
    }
    $qaRoot = Join-Path $root 'qa'
    New-Item -ItemType Directory -Force -Path $qaRoot | Out-Null
    [System.IO.File]::WriteAllText((Join-Path $qaRoot 'structural_validation.json'), ($result | ConvertTo-Json -Depth 8), $utf8NoBom)
    Write-Host "$($project.Name): $($result.status), $measureCount measures, $($pageResults.Count) pages."
}

if ($failed) { exit 1 }
