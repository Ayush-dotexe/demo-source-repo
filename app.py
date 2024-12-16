import yaml

def main():
    print("Starting the application...")
    # Load configuration from config.yaml
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    
    print("Application Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
