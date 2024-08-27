import yaml
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def test_connection(config_path=r"D:\Projetos\Projeto ETL\config\config.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={config['database']['server']};"
            f"UID={config['database']['username']};"
            f"PWD={config['database']['password']};"
        )
        print("Conexão com o banco de dados bem-sucedida!")
        conn.close()
    except pyodbc.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

test_connection()