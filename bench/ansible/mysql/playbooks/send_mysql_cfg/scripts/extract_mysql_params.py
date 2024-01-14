import configparser
import json
import datetime

def read_mysql_config(file_path='/etc/mysql/my.cnf'):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_path)

    performance_params = {
        'innodb_log_file_size',
        'innodb_log_buffer_size',
        'innodb_flush_log_at_trx_commit',
        'query_cache_size',
        'tmp_table_size',
        'max_heap_table_size',
    }
    parametrization = {}
    for section in config.sections():
        for key, value in config.items(section):
            if key in performance_params:
                parametrization[key] = value

    return parametrization

if __name__ == '__main__':
    file_path = '/etc/mysql/my.cnf'
    parametrization = read_mysql_config(file_path)

    benchInfo = {
        'parametrization': parametrization,
        'otherInfo': ''
    }

    result = {
        'benchInfo': benchInfo
    }
    with open('params.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
