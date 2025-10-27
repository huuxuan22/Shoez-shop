# Start MinIO in Docker
Write-Host "Starting MinIO..." -ForegroundColor Green
docker-compose -f docker-compose.minio.yml up -d

# Wait a moment for MinIO to start
Start-Sleep -Seconds 3

# Check if MinIO is running
$minioStatus = docker ps --filter "name=minio_server" --format "table {{.Status}}"
Write-Host "MinIO Status: $minioStatus" -ForegroundColor Yellow

# Start FastAPI
Write-Host ""
Write-Host "🚀 Starting SHOEZ API Server..." -ForegroundColor Cyan
Write-Host ""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
