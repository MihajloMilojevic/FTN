# TODO 3: implementirati primenu jednostavne linearne regresije
# nad podacima iz datoteke "data/skincancer.csv", koristeći scikit-learn bibiloteku.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from linreg_simple import make_predictions

if __name__ == "__main__":
    df = pd.read_csv("../data/skincancer.csv")
    x = df["Lat"]
    y = df["Mort"]
    
    reg = linear_model.LinearRegression()
    reg.fit(np.array(x).reshape(-1, 1), np.array(y))
    slope = reg.coef_[0]
    intercept = reg.intercept_

    y_pred = make_predictions(x, slope, intercept)

    plt.plot(x, y, 'xr')
    plt.plot(x, y_pred, 'm')
    plt.title(f'slope: {slope:.2f}, intercept: {intercept:.2f}')
    plt.xlabel("Lat")
    plt.ylabel("Mort")
    plt.show()
