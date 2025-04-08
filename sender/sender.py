import csv
import time
import requests
from collections import defaultdict

CSV_FILE = "ip_addresses.csv"
SERVER_URL = "http://server:5000/data"

def load_packets(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            pkt = {
                "ip": row["ip address"],
                "latitude": float(row["Latitude"]),
                "longitude": float(row["Longitude"]),
                "timestamp": int(row["Timestamp"]),
                "suspicious": int(float(row["suspicious"]))
            }
            data.append(pkt)
        data.sort(key=lambda x: x["timestamp"])
        return data

def group_by_timestamp(packets):
    grouped = defaultdict(list)
    for pkt in packets:
        grouped[pkt["timestamp"]].append(pkt)
    return sorted(grouped.items())

def send_packets(grouped):
    if not grouped:
        return

    base_time = grouped[0][0]
    start = time.time()

    for ts, group in grouped:
        delay = ts - base_time
        now = time.time()
        wait = delay - (now - start)
        if wait > 0:
            time.sleep(wait)
        try:
            requests.post(SERVER_URL, json=group)
            print(f"Sent {len(group)} packets at t={ts}")
        except Exception as e:
            print("send error:", e)

if __name__ == "__main__":
    data = load_packets(CSV_FILE)
    grouped = group_by_timestamp(data)
    send_packets(grouped)
