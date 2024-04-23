import pandas as pd
import csv

def main():
    with open('enterpriseSurvey.csv', 'r') as file:

        # Ler o arquivo CSV e carregar os dados em um DataFrame do pandas
        reader = csv.reader(file)
        data = list(reader)  # Converte os dados do leitor CSV em uma lista

    # Criar um DataFrame do pandas com os dados do CSV
    df = pd.DataFrame(data)
    print(df)

    # Escrever o DataFrame para um arquivo Excel
    df.to_excel('enterpriseData.xlsx', index=False)

main()

