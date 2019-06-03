import panas as pd


path_train = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/data_proyecto/train.csv
train = pd.read_csv(path_train, engine = 'python')
train.head()
print(train.shape)
print(train.columns)
print(train.info())
train.describe()


group_by_tarjeta = data1.groupby(['numerotarjeta', 'CLIENTE'])['SALDO'].sum()
group_by_tarjeta = data1.groupby('numerotarjeta')
group_by_tarjeta.describe()
group_by_tarjeta.mean()
