import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('CarPrice.csv')

X = df[['horsepower', 'curbweight', 'enginesize', 'highwaympg']]  
y = df['price']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_regresi = LinearRegression()
model_regresi.fit(X_train, y_train)

filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))

print(f"Model berhasil disimpan sebagai {filename}")