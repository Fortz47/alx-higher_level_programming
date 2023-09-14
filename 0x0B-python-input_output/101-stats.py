#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def print_metrics(metrics):
    """reads stdin line by line and computes metrics"""
    total_size = metrics.get("total_size", 0)
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if code in metrics:
            print(f"{code}: {metrics[code]}")

def main():
    """reads stdin line by line and computes metrics"""
    metrics = {"total_size": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 11:
                status_code = int(parts[10])
                file_size_str = parts[11]

                try:
                    file_size = int(file_size_str)
                except ValueError:
                    # Handle invalid file size
                    continue

                metrics["total_size"] += file_size

                if status_code in metrics:
                    metrics[status_code] += 1
                else:
                    metrics[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        print_metrics(metrics)

if __name__ == "__main__":
    main()
