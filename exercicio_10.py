import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def plot_histograma(valores: list[float], bins: int = 10) -> Figure:
    plt.figure()
    plt.hist(valores, bins)
    plt.xlabel("Valores da Lista")
    plt.ylabel("Número de Ocorrências")
    plt.show()