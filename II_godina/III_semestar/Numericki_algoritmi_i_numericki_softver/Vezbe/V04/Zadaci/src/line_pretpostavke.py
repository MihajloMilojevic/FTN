import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

from statsmodels.regression.linear_model import RegressionResultsWrapper
from sklearn.linear_model import LinearRegression  

from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import normal_ad
import statsmodels.api as sm

matplotlib.rcParams['figure.figsize'] = (8, 4)
sb.set(font_scale=1.)

def calculate_residuals(model, features, labels):
    '''Calculates residuals between true value `labels` and predicted value.'''
    y_pred = model.predict(features)
    df_results = pd.DataFrame({'Actual': labels, 'Predicted': y_pred})
    df_results['Residuals'] = abs(df_results['Actual']) - abs(df_results['Predicted'])
    return df_results


def linear_assumption(model, features, labels, p_value_thresh = 0.05, plot = True):
    if plot:
        plt.figure(figsize=(6,6))
        y_pred = model.predict(features)
        plt.scatter(labels, y_pred, alpha=.5)

        # x = y line
        line_coords = np.linspace(np.concatenate([labels, y_pred]).min(), np.concatenate([labels, y_pred]).max())
        plt.plot(line_coords, line_coords, color='darkorange', linestyle='--')
        plt.title('Tacno vs Predikcija')
        plt.xlabel('stvarna vrednost')
        plt.ylabel('prediktovana vrednost')
        plt.show()
    if type(model) == RegressionResultsWrapper:
        p_value = model.pvalues[1]
        is_linearity_found = True if p_value < p_value_thresh else False
        return is_linearity_found, p_value
    else:
        pass

def independence_of_errors_assumption(model, features, labels, plot = True):
    if plot:
        df_results = calculate_residuals(model, features, labels)
        sb.scatterplot(x='Predicted', y='Residuals', data=df_results)
        plt.axhline(y=0, color='darkorange', linestyle='--')
        plt.show()
    durbinWatson = durbin_watson(df_results['Residuals'])
    print('Durbin-Watson:', durbinWatson)
    if durbinWatson < 1.5:
        return 1
    elif durbinWatson > 2:
        return -1
    else:
        return 0

def normality_of_errors_assumption(model, features, labels, p_value_thresh=0.05, plot=True):
    if plot:
        df_results = calculate_residuals(model, features, labels)
        sb.histplot(df_results['Residuals'], kde=True, kde_kws=dict(cut=3))
    p_value = normal_ad(df_results['Residuals'])[1]
    return p_value >= p_value_thresh 

def equal_variance_assumption(model, features, labels, p_value_thresh=0.05, plot = True):
    if plot:
        df_results = calculate_residuals(model, features, labels)
        sb.scatterplot(x='Predicted', y='Residuals', data=df_results)
        plt.axhline(y=0, color='darkorange', linestyle='--')
        plt.show()
    p_value = sm.stats.het_goldfeldquandt(df_results['Residuals'], features)[1]
    return p_value >= p_value_thresh 