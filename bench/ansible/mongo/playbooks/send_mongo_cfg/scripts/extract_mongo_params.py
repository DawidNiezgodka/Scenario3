import yaml
import json
import datetime

def read_mongo_config():
    with open('/etc/mongod.conf', 'r') as file:
        return yaml.safe_load(file)

def extract_performance_params(config_data):
    params = {}
    if 'storage' in config_data:
        params['storageEngine'] = config_data['storage'].get('engine', 'N/A')
    if 'systemLog' in config_data:
        params['logVerbosity'] = config_data['systemLog'].get('verbosity', 'N/A')
    if 'net' in config_data:
        params['bindIp'] = config_data['net'].get('bindIp', 'N/A')
        params['port'] = config_data['net'].get('port', 'N/A')
    if 'operationProfiling' in config_data:
        params['slowOpThresholdMs'] = config_data['operationProfiling'].get('slowOpThresholdMs', 'N/A')
        params['mode'] = config_data['operationProfiling'].get('mode', 'N/A')
    return params

def save_to_json(performance_params, json_file_path):
    data = {
        'benchInfo': {
            'parametrization': performance_params,
            'otherInfo': ''
        }
    }
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    config_data = read_mongo_config()
    performance_params = extract_performance_params(config_data)
    save_to_json(performance_params, 'params.json')
