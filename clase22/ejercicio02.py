import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'Ventas': np.random.normal(100, 20, 5).round(2),
    'Gastos': np.random.normal(80, 10, 5).round(2),
    'Ganancia': np.random.normal(20,30,5).round(2),
})
df['Margen']=(df['Ganancia']/df['Ventas']*100).round(2)
df['Estado']=np.where(df['Ganancia']>0, 'Ganancia', 'Perdida')

new_df = df.style.format({
    'Ventas':"${:,.2f}",
    'Gastos':"${:,.2f}",
    'Ganancia':"${:,.2f}",
    'Margen':"{:.2f}"
})

print(df)

# Opción 1: Usar .map() solo en las columnas específicas
new = df[['Ganancia', 'Margen']].map(
    lambda v: 'Color:red' if v < 0 else None
)

print(new_df)