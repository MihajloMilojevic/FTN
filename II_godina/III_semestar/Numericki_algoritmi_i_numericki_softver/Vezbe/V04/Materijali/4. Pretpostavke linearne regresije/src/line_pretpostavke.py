import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

matplotlib.rcParams['figure.figsize'] = (8, 4)
sb.set(font_scale=1.)

def calculate_residuals(model, features, labels):
    '''Calculates residuals between true value `labels` and predicted value.'''
    y_pred = model.predict(features)
    df_results = pd.DataFrame({'Actual': labels, 'Predicted': y_pred})
    df_results['Residuals'] = abs(df_results['Actual']) - abs(df_results['Predicted'])
    return df_results


def linear_assumption(model, features, labels):
    pass

def independence_of_errors_assumption(model, features, labels):
    pass

def normality_of_errors_assumption(model, features, label, p_value_thresh=0.05):
    pass

def equal_variance_assumption(model, features, labels, p_value_thresh=0.05):
    pass