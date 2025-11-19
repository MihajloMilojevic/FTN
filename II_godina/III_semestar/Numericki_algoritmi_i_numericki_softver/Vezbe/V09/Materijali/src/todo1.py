import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import STL
import numpy as np

matplotlib.rcParams['figure.figsize'] = (8, 4)
sb.set(font_scale=1.)

if __name__ == '__main__':
    df = pd.read_csv('data/airline-passengers.csv')