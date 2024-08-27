import logging
import sys
sys.path.append(r'D:\Projetos\Projeto ETL\etl')

from extract import extract_data
from load import load_data


logging.basicConfig(filename='log\etl.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def run_etl():
    logging.info("ETL process started")

    data = extract_data()
    logging.info(f"Data extracted: {data.shape[0]} records.")

    load_data(data)
    logging.info("Data loaded successfully")

    logging.info("ETL process completed")

if __name__ == "__main__":
    run_etl()