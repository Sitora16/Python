!pip install matplotlib
import matplotlib.pyplot as plt
#Homework
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1
#1
df1['avg']=df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1['avg'])
#2
max_avg=df1['avg'].max()
top=df1[df1['avg']==max_avg]
print(top)
#3
df1['Total']=df1['Math']+df1['English']+df1['Science']
print(df1)
#4
import matplotlib.pyplot as plt
avggrade=df1[['Math', 'English', 'Science']].mean()
avggrade.plot(kind='bar', color=['pink', 'purple', 'yellow'])
plt.title('Average grade by subject')
plt.ylabel('Average Score')
plt.xlabel('Subjects')
plt.show()

#2
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2
#2.1
df2['Total']=df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
print(df2['Total'])
#2.2
maxtotal=df2['Total'].max()
datemax=df2[df2['Total']==maxtotal]['Date']
print(datemax)
#2.3
df2['Product_A_%_change']=df2['Product_A'].pct_change()*100
df2['Product_B_%_change']=df2['Product_B'].pct_change()*100
df2['Product_C_%_change']=df2['Product_C'].pct_change()*100
print(df2[['Date','Product_A_%_change','Product_B_%_change', 'Product_C_%_change']])
#2.4
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_A'], marker='s', label='Product A')
plt.plot(df2['Date'], df2['Product_A'], marker='^', label='Product A')
plt.title('Sales Trends over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()
#3
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
df3
#3.1
avgsalary=df3.groupby('Department')['Salary'].mean()
print(avgsalary)
#3.2
exp=df3['Experience (Years)'].max()
emp_exp=df3[df3['Experience (Years)']==exp]
print(emp_exp)
#3.3
min_salary=df3['Salary'].min()
df3['Salary Increare']=((df3['Salary']-min_salary)/min_salary)*100
print(df3[['Name', 'Salary', 'Salary Increare']])
#3.4
dept_counts = df3['Department'].value_counts()
dept_counts.plot(kind='bar',color='pink')
plt.title('Employees distribution across department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()
#4
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4
#4.1
total_revenue=df4['Total_Price'].sum()
print(total_revenue)

#4.2
maxord=df4['Quantity'].max()
maxordered=df4['Quantity']==maxord
print(maxord)
#4.3
avgquantity=df4['Quantity'].mean()
print(avgquantity)
#4.4
import matplotlib.pyplot as plt
sales=df4.groupby('Product')['Total_Price'].sum()
sales.plot.pie()
plt.title('Sales distribution by product')
plt.ylabel('')
plt.show()
