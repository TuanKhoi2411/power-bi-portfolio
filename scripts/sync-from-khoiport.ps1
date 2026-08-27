param(
    [string]$KhoiPortRoot = 'C:\PowerBI Dashboard - KhoiPort',
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$expectedRepository = [System.IO.Path]::GetFullPath($RepositoryRoot)
$projectsRoot = [System.IO.Path]::GetFullPath((Join-Path $expectedRepository 'projects'))
if (-not $projectsRoot.StartsWith($expectedRepository, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Resolved projects path escaped repository root: $projectsRoot"
}
if (-not (Test-Path -LiteralPath $KhoiPortRoot)) {
    throw "KhoiPort root does not exist: $KhoiPortRoot"
}

$projects = @(
    @{
        Name = 'sales-performance'
        Canonical = '01_UK_Online_Retail_Sales'
        PbixSource = 'PowerBI_Project/UK_Online_Retail_Sales - pbix.pbix'
        PbixTarget = 'UK_Online_Retail_Sales_Performance_Dashboard.pbix'
    },
    @{
        Name = 'finance-performance'
        Canonical = '02_Apple_Finance'
        PbixSource = 'PowerBI_Project/Apple_Finance - pbix.pbix'
        PbixTarget = 'Apple_Inc_Financial_Performance_Dashboard.pbix'
    },
    @{
        Name = 'marketing-performance'
        Canonical = '03_Portuguese_Bank_Marketing'
        PbixSource = 'PowerBI_Project/Portuguese_Bank_Marketing - pbix.pbix'
        PbixTarget = 'Portuguese_Bank_Marketing_Performance_Dashboard.pbix'
    },
    @{
        Name = 'credit-risk-performance'
        Canonical = '04_FinTech_Credit_Risk'
        PbixSource = 'PowerBI_Project/FinTech_Credit_Risk - pbix.pbix'
        PbixTarget = 'FinTech_Credit_Risk_Dashboard.pbix'
    }
)

foreach ($project in $projects) {
    $sourceRoot = [System.IO.Path]::GetFullPath((Join-Path $KhoiPortRoot $project.Canonical))
    if (-not $sourceRoot.StartsWith([System.IO.Path]::GetFullPath($KhoiPortRoot), [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Resolved source escaped KhoiPort: $sourceRoot"
    }
    $targetRoot = [System.IO.Path]::GetFullPath((Join-Path $projectsRoot $project.Name))
    if (-not $targetRoot.StartsWith($projectsRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Resolved target escaped projects root: $targetRoot"
    }

    New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null
    $pbixSource = Join-Path $sourceRoot $project.PbixSource
    if (-not (Test-Path -LiteralPath $pbixSource)) { throw "Missing canonical PBIX: $pbixSource" }
    Copy-Item -LiteralPath $pbixSource -Destination (Join-Path $targetRoot $project.PbixTarget) -Force

    foreach ($pair in @(
        @{ Source='PowerBI_Project'; Target='dashboard'; Exclude=@('*.pbix') },
        @{ Source='Data'; Target='data'; Exclude=@() },
        @{ Source='Documentation'; Target='source-documentation'; Exclude=@() },
        @{ Source='Build_Scripts'; Target='build-scripts'; Exclude=@('__pycache__','*.pyc') },
        @{ Source='Theme'; Target='theme'; Exclude=@() }
    )) {
        $source = Join-Path $sourceRoot $pair.Source
        $target = [System.IO.Path]::GetFullPath((Join-Path $targetRoot $pair.Target))
        if (-not $target.StartsWith($targetRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Resolved mirror target escaped project root: $target"
        }
        if (Test-Path -LiteralPath $target) {
            Remove-Item -LiteralPath $target -Recurse -Force
        }
        if (Test-Path -LiteralPath $source) {
            New-Item -ItemType Directory -Force -Path $target | Out-Null
            Get-ChildItem -LiteralPath $source -Force | Where-Object {
                $item = $_
                -not ($pair.Exclude | Where-Object { $item.Name -like $_ })
            } | Copy-Item -Destination $target -Recurse -Force
        }
    }
}

$sportsSource = Join-Path $KhoiPortRoot '05_Sports_Health_Financial_Performance_GitHub/Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix'
$sportsTarget = Join-Path $projectsRoot 'financial-performance-dashboard/Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix'
Copy-Item -LiteralPath $sportsSource -Destination $sportsTarget -Force

Write-Host 'Synchronized 5 canonical PBIX files and 4 editable PBIP packages from KhoiPort.'
