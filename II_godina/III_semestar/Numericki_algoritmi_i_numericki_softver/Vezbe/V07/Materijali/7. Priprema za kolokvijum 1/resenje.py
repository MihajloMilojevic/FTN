
import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *

# **Zadatak 1.**
# učitavamo podatke
df = pd.read_csv('data/train.csv', sep=',')
df.head()

# Pre treniranja modela moramo rešiti nedostajuće vrednosti.
# Najlakši način je da izbacimo sve redove.
df = df.dropna()

# fitujemo model (tražimo parametre)
x = df.drop(columns=['plata'])
y = df['plata']
model = get_fitted_model(x, y)

# prijavljujemo metriku na test skupu
df_test = pd.read_csv('data/test.csv', sep=',')
x_test = df_test.drop(columns=['plata'])
y_test = df_test['plata']
test_rmse = get_rmse(model, x_test, y_test)
print(test_rmse)


# **Zadatak 2.**
# tražimo min i maks vrednosti
min_expected_raise, max_expected_raise = get_conf_interval(model, 'zvanje', alpha=0.05)
print(f'{min_expected_raise:.2f}')
print(f'{max_expected_raise:.2f}')

# provera da li su min i maks vrednosti validne
autocorrelation, _ = independence_of_errors_assumption(model, sm.add_constant(x), y, plot=False)
if autocorrelation is None:
    print('vrednosti su validne, jer je zadovoljena pretpostavka o nezavisnosti gresaka')
else:
    print('vrednosti nisu validne')


# **Zadatak 3.**
# učitamo podatke
df = pd.read_csv('data/train.csv', sep=',')
# interpolacija umesto brisanja vrednosti zadovoljava sve pretpostavke
df['zvanje'] = df['zvanje'].interpolate(method='spline', order=4, limit_direction='both')
df['godina_doktor'] = df['godina_doktor'].interpolate(method='linear', limit_direction='both')

# brišemo kolonu pol Muski (ili pol Zenski) kako ne bi imali savršenu kolinearnost
df = df.drop(columns=['pol Muski', 'pol Zenski'])

# delimo podatke u odnosu 80-20
x = df.drop(columns=['plata'])
y = df['plata']
x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.8, shuffle=True, random_state=42)

# fitujemo model
model = get_fitted_model(x_train,y_train)

# proveravamo da li su zadovoljenepretpostavke (pogledaj objašnjenje)
print(are_assumptions_satisfied(model, x, y))

# gledamo meru na validacionom skupu kako bi našli najbolji model
val_rmse = get_rmse(model, x_val, y_val)
print(f'validation rmse: {val_rmse:.2f}')

# prijavljujemo meru na test skupu
df_test = pd.read_csv('data/test.csv', sep=',')
x_test = df_test.drop(columns=['plata', 'pol Muski', 'pol Zenski'])
y_test = df_test['plata']
test_rmse = get_rmse(model, x_test, y_test)
print(f'test rmse: {test_rmse:.2f}')