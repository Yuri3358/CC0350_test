import pandas
def cria_resumo(df: pandas.DataFrame, coluna: str) -> pandas.DataFrame:
    data = df[coluna]
    manual_describe_data = pandas.Series({
        "count": data.count(),
        "mean": data.mean(),
        "std": data.std(),
        "min": data.min(),
        "25%": data.quantile(0.25), #filler
        "50%": data.quantile(0.5), 
        "75%": data.quantile(0.75),
        "max": data.max()
    })
    return manual_describe_data.to_frame(coluna)