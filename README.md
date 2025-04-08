# Global Traffic Monitor 🌎

Real-time traffic visualization system that shows where web traffic hits your server from around the globe. It processes traffic data from a CSV file (simulating real network packets), detects suspicious activities, and displays everything on an interactive 3D globe using Three.js. Watch as packets flow in with their actual timing - normal traffic shows up in white, while suspicious packets glow red. The whole thing runs in Docker containers, with Python handling the backend magic and Three.js making the frontend look sweet.

![In Action](./traffic.gif)

## Tech
- Three.js + WebGL + Three-Globe for 3D globe visualization
- Socket.IO for real-time data streaming
- Flask backend for data processing
- Docker for deployment

## Quick start
```bash
docker-compose up --build
```
Hit `http://localhost:8080/` 🚀
