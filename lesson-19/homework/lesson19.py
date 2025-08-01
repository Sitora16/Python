#Homework
import pandas as pd
cust_ord=pd.read_csv("customer_orders.csv")
print(cust_ord)

sal_date=pd.read_csv("sales_data.csv")
print(sal_date)
#1
categ=sal_date.groupby('Category').agg(
    TotalQuantity=('Quantity', 'sum'),
    AvgPrice=('Price', 'mean'),
    MaxQuantity=('Quantity', 'max')
).reset_index()
print(categ)
#2
grouped=sal_date.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
topProducts=grouped.sort_values('Quantity', ascending=False).groupby('Category').first().reset_index()
print(topProducts)
#3
sal_date['Sales']=sal_date['Quantity']*sal_date['Price']
daily=sal_date.groupby('Date')['Sales'].sum().reset_index()
maxsales=daily.loc[daily['Sales'].idxmax()]
print(maxsales)
#2.1
counts=cust_ord.groupby('CustomerID')['OrderID'].nunique().reset_index(name='OrderCount')
filt=counts[counts['OrderCount']>=20]["CustomerID"]
filtered=cust_ord[cust_ord["CustomerID"].isin(filt)]
print(filtered)

#2.2
c=cust_ord.groupby('CustomerID')['Price'].mean()
avg=c[c>120].index
print(avg)
#2.3
totalQuantity=cust_ord.groupby('Product')['Quantity'].sum()
cust_ord['Revenue']=cust_ord['Quantity']*cust_ord['Price']
totalrevenue=cust_ord.groupby('Product')['Revenue'].sum()
filtquantity=totalQuantity[totalQuantity>=5]
result=pd.DataFrame({
    'Total_quantity': filtquantity,
    'Total_Revenue': totalrevenue[filtquantity.index]
})
print(result)
#3.1
import sqlite3
conn=sqlite3.connect('population (1).db')
population=pd.read_sql_query('SELECT*FROM population',conn)
conn.close()
population.reset_index()

pop_sal=pd.read_excel('population_salary_analysis.xlsx')

pop_sal

#3.2
pop_sal=pd.read_excel('population_salary_analysis.xlsx')

pop_sal
def categorize(s):
    if  s<200000:
        a='till $200,000'
    elif s<400000:
        a='$200,001 - $400,000'
    elif s<600000:
        a='$400,001 - $600,000'
    elif s<800000:
        a='$600,001 - $800,000'
    elif s<1000000:
        a='$800,001 - $1,000,000'
    elif s<1200000:
        a='$1,000,001 - $1,200,000'
    elif s<1400000:  
        a='$1,200,001 - $1,400,000'
    elif s<1600000:  
        a='$1,400,001 - $1,600,000'
    elif s<1800000:  
        a='$1,600,001 - $1,800,000'
    elif s>1800000:  
        a='over'
    return a
population['salary_category']=population['salary'].apply(categorize)


population['salary_category'].value_counts().reset_index()

population['salary_category'].value_counts().pct_change()

population
salary_category_percent = population['salary_category'].value_counts(normalize=True) * 100

print(salary_category_percent.reset_index().rename(columns={'index':'salary_category', 'salary_category':'percent'}))
