# TODO 3: implementirati primenu jednostavne linearne regresije
# nad podacima iz datoteke "data/skincancer.csv".
from linreg_simple import fit, make_predictions
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("../data/skincancer.csv")
    x = df["Lat"]
    y = df["Mort"]
    slope, intercept = fit(x, y)

    y_pred = make_predictions(x, slope, intercept)

    plt.plot(x, y, 'xr')
    plt.plot(x, y_pred, 'm')
    plt.title(f'slope: {slope:.2f}, intercept: {intercept:.2f}')
    plt.xlabel("Lat")
    plt.ylabel("Mort")
    plt.show()
