import random
import matplotlib.pyplot as plt
import numpy as np


def fit(x, y):
    assert len(x) == len(y)
    slope = 0.0  # nagib linije
    intercept = 0.0  # tacka preseka na y-osi
    n = len(x)
    y_mean = sum(y) / n
    x_mean = sum(x) / n

    # convert to np arrays and subtract the mean element wise
    x_minus_mean = np.array(x) - x_mean
    y_minus_mean = np.array(y) - y_mean
    
    # calucate arrays from formula
    x_times_y = x_minus_mean * y_minus_mean
    x_squered = x_minus_mean ** 2
    
    # calulate slope and intersection
    slope = sum(x_times_y) / sum(x_squered)    
    intercept = y_mean - slope * x_mean
    
    return slope, intercept


def predict(x, slope, intercept):
    return x*slope + intercept


def make_predictions(x, slope, intercept):
    y_pred = [predict(xi, slope, intercept) for xi in x]
    return y_pred


if __name__ == '__main__':
    # da rezultati mogu da se reprodukuju
    random.seed(1337)
    # random generisi podatke sa nasumicnim sumom
    x = [xi for xi in range(50)]
    # y = x (+- nasumicni sum)
    y = [(xi + random.randint(-5, 5)) for xi in x]  

    # izracunaj nagib i presek za liniju koja se najbolja uklapa (best fit)
    slope, intercept = fit(x, y)

    # prediktuj y za svako x
    y_pred = make_predictions(x, slope, intercept)

    # plotuj podatke i liniju koja se nabolje uklapa (best fit)
    plt.plot(x, y, 'xr')
    plt.plot(x, y_pred, 'b')
    plt.title(f'slope: {slope:.2f}, intercept: {intercept:.2f}')
    plt.show()
