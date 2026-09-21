from fastapi import FastAPI
import psutil 

app = FastAPI(
    title = "DevOps Health API",
    description = "Infra health monitoring system",
    version = "1.0.0"
)


@app.get("/")
def home():
    return {
        "message" : "DevOps Health API is running"
    }
    
@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }
    

@app.get("/system")
def system():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent" : psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent
    }