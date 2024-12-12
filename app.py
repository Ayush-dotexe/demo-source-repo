import yaml
import sys

def main(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        print("Configuration Loaded:")
        print(config)
    except FileNotFoundError:
        print(f"Error: Configuration file {config_path} not found!")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)

    print(f"Application Name: {config['app']['name']}")
    print(f"Application Version: {config['app']['version']}")
    print(f"Running in {config['app']['environment']} environment.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <config_file_path>")
        sys.exit(1)

    config_file_path = sys.argv[1]
    main(config_file_path)
