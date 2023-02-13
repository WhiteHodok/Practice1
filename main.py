import numpy as np
import pandas as pd
N = 1
data = {
    'Name' : ['Lion', 'Tiger', 'Elephant', 'Giraffe'],
    'Species' : ['Carnivore', 'Carnivore', 'Herbivore', 'Herbivore'],
    'Weight' : [190, 160, 600, 1000],
    'Count' : [5, 4, 8, 15],

}

colonka = ['Name', 'Species', 'Weight', 'Count']

animals = pd.DataFrame(data, columns=colonka)

#animals.to_csv('animals.csv', index=True) команда для создания CSV-таблицы



#df[start:end]
#df.groupby('column_name').agg({'column_name': 'function'})
#df.fillna(value)
#df.dropna()
#df.sort_values(by='column_name', ascending=False)
#df[df['column_name'] > value]
#df.rename(columns={'Name': 'Full Name'})
print('Пункт 1')
print(animals.tail(N))
print('\n')
print('Пункт 2')
print(animals.head(N))
print('\n')
print('Пункт 3')
print(animals.describe(), animals['Count'])
print('\n')
print('Пункт 4')
print(animals.fillna(method="ffill"))
print('\n')
print('Пункт 5')
print(animals.dropna(axis='columns'))
print('\n')
print('Пункт 6')
print(animals.sort_values(by='Count', ascending=False))
print('\n')
print('Пункт 7')
print(animals.rename(index={0: "x", 1: "y", 2: "z"}))

