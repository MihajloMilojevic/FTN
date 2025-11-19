import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.model_selection import train_test_split
from utils import *


if __name__ == '__main__':
    # 1. Izbacuje sve redove kojima nedostaje vrednost.
    df = pd.read_csv('data/missing_data_housing.csv', sep=',') 

    # 2. Izbacuje atribut `stories`, a atribut `lotsize(m^2)` popunjava srednjom vrednošću.
    

    # 3. Nedostajuće vrednosti popunjava kubnim splajnom.
    

    # 4. Nedostajuce vrednosti atributa `stories` popunjava linearnim splajnom. Ostale nedostajuce vrednosti popunjava kubnim splajnom.
    