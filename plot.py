import matplotlib.pyplot as plt
import pandas as pd


def plotCompareTimes():
    data = pd.read_csv('times4.csv')
    data2 = pd.read_csv('times5.csv')
    size = data['size'].tolist()
    timeIDS = data['IDS'].tolist()
    timeHC = data['HC'].tolist()
    timeRRHC = data2['RRHC'].tolist()
    timeSA = data['SA'].tolist()
    
    
    plt.figure(1)
    plt.title('Comparativo')
    plt.plot(size,timeIDS, label='IDS')
    plt.plot(size,timeHC, label='HC')
    plt.plot(size,timeRRHC, label='RRHC')
    plt.plot(size,timeSA, label='SA')
    plt.grid(True)
    plt.xlabel("Tamanho (NxN)")
    plt.ylabel("Tempo médio (s)")
    plt.legend()

    plt.figure(2)
    plt.title('Tempo gasto por IDS')
    plt.plot(size,timeIDS, label='IDS')
    plt.grid(True)
    plt.xlabel("Tamanho (NxN)")
    plt.ylabel("Tempo médio (s)")
    plt.legend()
    

    plt.figure(3)
    plt.title('Tempo gasto por HC')
    plt.plot(size,timeHC, label='HC')
    plt.grid(True)
    plt.xlabel("Tamanho (NxN)")
    plt.ylabel("Tempo médio (s)")
    plt.legend()
    

    plt.figure(4)
    plt.title('Tempo gasto por SA')
    plt.plot(size,timeSA, label='SA')
    plt.grid(True)
    plt.xlabel("Tamanho (NxN)")
    plt.ylabel("Tempo médio (s)")
    plt.legend()
    
    plt.figure(5)
    plt.title('Comparativo')
    plt.plot(size,timeHC, label='HC')
    plt.plot(size,timeRRHC, label='RRHC')
    plt.grid(True)
    plt.xlabel("Tamanho (NxN)")
    plt.ylabel("Tempo médio (s)")
    plt.legend()
    

    plt.show()


if __name__ == "__main__":
    plotCompareTimes()