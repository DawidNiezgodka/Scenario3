import json
import sys

def extract_metrics(filename, workload, operationcount, threads):
    output = {
        "benchInfo": {
            "executionTime": "",
            "otherInfo": f"YCSB Parameters: workload={workload}, operationcount={operationcount}, threads={threads}"
        },
        "results": []
    }
    with open(filename, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split(", ")

            if len(parts) < 3:
                continue

            section, metric, value = parts[0], parts[1], parts[2]

            if section == "[OVERALL]" and metric == "RunTime(ms)":
                minutes = int(value) // 60000
                seconds = (int(value) % 60000) // 1000
                output["benchInfo"]["executionTime"] = f"{minutes}m {seconds}s"

            elif section == "[OVERALL]" and metric == "Throughput(ops/sec)":
                output["results"].append({
                    "unit": "ops/sec",
                    "value": round(float(value), 2),
                    "name": "OVERALL Throughput"
                })

            elif (section in ["[READ]", "[UPDATE]"]) and metric in ["AverageLatency(us)", "MaxLatency(us)"]:
                output["results"].append({
                    "unit": "us",
                    "value": round(float(value), 2),
                    "name": f"{section}, {metric}"
                })

    return output

def main():
    if len(sys.argv) >= 5:
        host_identifier, workload, operationcount, threads = sys.argv[1:5]
    else:
        host_identifier = "default"
        workload = 'workloada'
        operationcount = '50000'
        threads = '8'

    results_file_name = f"result_{host_identifier}.json"
    metrics = extract_metrics("ycsb.txt", workload, operationcount, threads)
    with open(results_file_name, 'w') as f:
        json.dump(metrics, f, indent=2)

if __name__ == '__main__':
    main()
