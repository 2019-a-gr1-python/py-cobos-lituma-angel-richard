import pandas as pd


path_train = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/data_proyecto/train.csv'
train = pd.read_csv(path_train, engine = 'python')
train.plot()

train['Age'].min()
train['Age'].max()
train['Age'].mean()
train['Age'].std()
train['Age'].count()


train['Age'].plot()
train['Age'].hist()
train['Pclass'].plot(kind='pie')

train.groupby('Sex').mean()["Age"].plot(kind='bar')



# Numero de sobrevivientes
train.groupby('Survived').count()["Sex"].plot(kind='bar')
# Numero de sobrevivientes por sexo y por clase
group_by_train = train.groupby(['Pclass', 'Sex'])['Survived'].sum()
#grafico
group_by_train = train.groupby(['Pclass', 'Sex'])['Survived'].sum().plot(kind='bar')
# dateframe de otras columnas
columnas_a_usar = ['Pclass', 'Name', 'Sex', 'Age', 'Survived']
train1 = pd.read_csv(path_train,  usecols = columnas_a_usar)

# numero de edad maxima de personas que sobrevivio y de personas que no
train1.groupby('Survived').max()["Age"].plot(kind='bar')
#numero de edad minima de personas que no sobrevivieron
train1.groupby('Survived').min()["Age"].plot(kind='bar')



