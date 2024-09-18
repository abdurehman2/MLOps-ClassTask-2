# docker-build.ps1

param (
    [string]$action
)

if ($action -eq "image") {
    docker build -t flask-app .
}
elseif ($action -eq "run") {
    docker run -d -p 5000:5000 flask-app
}
elseif ($action -eq "containers") {
    docker ps -a
}
else {
    Write-Host "Unknown action: $action"
}
