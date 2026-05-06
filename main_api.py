import psutil
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="System Health API")

@app.get("/status")
def get_system_status():
    """Sistemin anlıq yükünü qaytarır."""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "ram_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "is_system_healthy": psutil.cpu_percent() < 90  # CPU 90%-dən çoxdursa riskli sayılır
    }

@app.get("/processes")
def get_top_processes(limit: int = 5):
    """Ən çox resurs aparan proseslərin siyahısını verir."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # CPU istifadəsinə görə sıralayırıq
    top_procs = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:limit]
    return {"top_processes": top_procs}

@app.get("/network")
def get_network_info():
    """İnternet sürəti və data axını haqqında məlumat."""
    net = psutil.net_io_counters()
    return {
        "sent_mb": round(net.bytes_sent / (1024 * 1024), 2),
        "received_mb": round(net.bytes_recv / (1024 * 1024), 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)