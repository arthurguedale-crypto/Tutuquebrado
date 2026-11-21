
import pandas as pd

def diagnosticar(df):
    print(f"Linhas: {len(df)}")

    print(f"Duplicatas: {df.duplicated().sum()}")

    print("\nValores faltando por coluna:")
    faltando = df.isna().sum()

    if faltando.any():
        print(faltando[faltando > 0])
    else:
        print("Nenhum")

    print("\nTipo de cada coluna:")
    print(df.dtypes)


# Abrir o Excel
df = pd.read_excel("aula10.xlsx")

# Fazer o diagnóstico
diagnosticar(df)
fsdfsd