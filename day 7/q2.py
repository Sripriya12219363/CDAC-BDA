import csv
import json

def convert_log_file(input_log_path, output_csv_path, output_json_path):
    records = []
    with open(input_log_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" | ")
            record = {
                "timestamp": parts[0],
                "user_id": parts[1],
                "endpoint": parts[2],
                "status_code": int(parts[3])
            }
            records.append(record)
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["timestamp", "user_id", "endpoint", "status_code"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

def main():
    convert_log_file(
        "server_access.log",
        "access_records.csv",
        "access_records.json"
    )

main()