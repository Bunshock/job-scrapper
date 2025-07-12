def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        return json.load(file)

def log(message):
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} - {message}")