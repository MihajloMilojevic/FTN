import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

from todo1 import are_assumptions_satisfied

def get_rsquared_adj(model, x, y):
    num_attributes = x.shape[1]
    y_pred = model.predict(sm.add_constant(x, has_constant='add'))

    from sklearn.metrics import r2_score
    r_squared = r2_score(y, y_pred)
    n = len(y_pred)
    p = num_attributes
    adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
    return adjusted_r_squared

def get_fitted_model(x, y):
    x_with_const = sm.add_constant(x, has_constant='add')
    model = sm.OLS(y, x_with_const).fit()
    return model

if __name__ == '__main__':
    pass