import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from utils import *
import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    df = pd.read_csv('data/responses.csv')
    # ...