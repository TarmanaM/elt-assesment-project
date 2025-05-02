import uvicorn
import os
import signal

if __name__ == "__main__":
    port = int(os.getenv("API_PORT", 8000))  # Default ke 8000 jika tidak ada env
    reload = os.getenv("DEBUG", "true").lower() == "true"  # Optional, untuk dev

    def stop_signal_handler(signal, frame):
        print("Server stopped by signal.")
        exit(0)

    # Menangani SIGINT untuk memastikan bisa dimatikan dengan CTRL+C
    signal.signal(signal.SIGINT, stop_signal_handler)

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # Agar bisa diakses dari luar container
        port=port,
        reload=reload  # Hanya untuk development
    )
