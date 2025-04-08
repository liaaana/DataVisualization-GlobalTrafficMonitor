FROM python:3.11-slim-buster
WORKDIR /app
COPY app.py .
RUN pip install flask flask-cors flask-socketio
EXPOSE 5000
CMD ["python", "app.py"]
