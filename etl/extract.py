import pandas as pd
import yaml

def load_config():
    with open(r"D:\Projetos\Projeto ETL\config\config.yaml", 'r') as file:
        config = yaml.safe_load(file)
    return config

def extract_data():
    config = load_config()
    raw_data_path = config['data_paths']['raw_data']
    data = pd.read_csv(raw_data_path)
    return data