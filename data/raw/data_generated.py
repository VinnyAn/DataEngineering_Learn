import pandas as pd
import numpy as np
import random

# Configurando o tamanho da base de dados
num_records = 1000

# Gerando dados fictícios
data = {
    "ID": range(1, num_records + 1),
    "Name": [f"Person_{i}" for i in range(1, num_records + 1)],
    "Age": np.random.randint(18, 65, num_records),
    "City": [random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]) for _ in range(num_records)],
    "Salary": np.random.randint(30000, 120000, num_records)
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Exibindo as primeiras linhas da base de dados
print(df.head())

# Salvando em um arquivo CSV (opcional)
df.to_csv(r'D:\Projetos\Projeto ETL\data\raw\data.csv', index=False)
