import json
import sys

def merge_dicts(d1, d2):
    for k, v in d2.items():
        if k in d1:
            if isinstance(d1[k], dict) and isinstance(v, dict):
                merge_dicts(d1[k], v)
            elif isinstance(d1[k], str) and isinstance(v, str):
                d1[k] = f"{d1[k]}, {v}"
        else:
            d1[k] = v

host_identifier = sys.argv[1]
print(host_identifier)
results_file_name = f"result_{host_identifier}.json"
with open('params.json', 'r') as f:
    params_data = json.load(f)
with open(results_file_name, 'r') as f:
    results_data = json.load(f)
merge_dicts(results_data, params_data)
with open(results_file_name, 'w') as f:
    json.dump(results_data, f, indent=2)
