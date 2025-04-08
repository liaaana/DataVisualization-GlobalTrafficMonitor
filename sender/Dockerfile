FROM python:3.11-slim-buster
WORKDIR /app
COPY sender.py .
COPY ip_addresses.csv .
RUN pip install requests
CMD ["python", "sender.py"]
