import pandas
def filtra_df(df: pandas.DataFrame, coluna: str, limiar: float) -> pandas.DataFrame:
    return (df[df[coluna] >= limiar])