#1
fruits=['apple','banana','strawberry','orange','grape']
print(fruits[3])
#2
l1=[2,12,16,24,29]
l2=[29,24,16,12,2]
l1.extend(l2)
print(l1)
#3
numbers=[2,12,16,24,29]
first=numbers[0]
middle=numbers[len(numbers)//2]
last=numbers[-1]

new_list=[first,middle,last]
print(new_list)
#4
favourite_movies=['Uyda yolgiz','Moviy dengiz afsonasi','Hayat bazen tatlidir','Conjuring','Conjuring2',]
f_m_tuple=tuple(favourite_movies)
print(f_m_tuple)
type(f_m_tuple)
#5
cities=['Paris','Almalyk','Toshkent',]
if 'Paris' in cities:
    print("Paris in the list")
else:
    print("paris is NOT in the list")
  #6
numbers=[2,12,16,24,29]
duplicated=numbers*2
print(duplicated)
#7
numbers=[2,12,16,24,29]
numbers[0],numbers[4]=numbers[4],numbers[0]
print(numbers)
#8
numbers=tuple(range(1,11))
print(numbers[3:8])
#9
Colors=['blue','pink','yellow','blue']
count_blue=Colors.count('blue')
print(count_blue)
#10
animals=('dog','cat','squirrel','lion',)
index_animals=animals.index('lion')
print(index_animals)
#11
t1=(1,2,)
t2=(3,4,)
merged=(*t1,*t2)
print(merged)
#12
l=[1,2,3,4]
t=(5,6,7,8,)
len_list=len(l)
len_tuple=len(t)
print(len_list,len_tuple)
#13
numbers_tuple=(2,12,16,24,29,)
numbers_list=list(numbers_tuple)
print(numbers_list)
#14
numbers=(2,12,16,24,29,)
numbers_max=max(numbers)
numbers_min=min(numbers)
print("max_value:",numbers_max)
print("min_value:",numbers_min)
#15
words=("Sitora","is","name","My")
reversed=words[::-1]
print("reversed_words:",reversed)
