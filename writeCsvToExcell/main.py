import pandas as pd
import csv

def main():
    with open('enterpriseSurvey.csv', 'r') as file:

        reader = csv.reader(file)
        data = list(reader)

    df = pd.DataFrame(data)
    print(df)

    df.to_excel('enterpriseData.xlsx', index=False)

main()

