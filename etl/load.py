import yaml

def load_config():
    with open(r"D:\Projetos\Projeto ETL\config\config.yaml", 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_data(data):
    config = load_config()
    processed_data_path = config['data_paths']['processed_data']
    data.to_csv(processed_data_path, index=False)