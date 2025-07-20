#Homework
#1
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
def rename_col(col_name):
    return col_name.lower().replace(' ','_')
df.rename(columns=rename_col,inplace=True)
print(df)
#2
print(df.head(3))
#3
mean_age=df['age'].mean()
print("Mean age: ", mean_age)
#4
print(df[['first_name', 'city']])
#5
import numpy as np
df['salary']=np.random.randint(50000,100001, size=len(df))
print(df)
#6
print(df.describe())
#2.1
import pandas as pd 
data={
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
se=pd.DataFrame(data)
print(se)
#2.2
maxexpenses=se['Expenses'].max()
maxsales=se['Sales'].max()
print(maxexpenses)
print(maxsales)
#2.3
minexpenses=se['Expenses'].min()
minsales=se['Sales'].min()
print(minexpenses)
print(minsales)
#2.4
meanexpenses=se['Expenses'].mean()
meansales=se['Sales'].mean()
print(meanexpenses)
print(meansales)
#3.1
data={
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses=pd.DataFrame(data)
print(expenses)
#3.2
expenses.set_index('Category', inplace=True)
maxcategory=expenses.max(axis=1)
print(maxcategory)
#3.3
expenses.set_index('Category', inplace=True)
mincategory=expenses.min(axis=1)
print(mincategory)
#3.4
expenses.set_index('Category', inplace=True)
meancategory=expenses.mean(axis=1)
print(meancategory)
