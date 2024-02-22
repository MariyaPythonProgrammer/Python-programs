'''#Data Type
inputvalue=78
print(type(inputvalue))

inputvalue=78.89
print(type(inputvalue))

inputvalue="maryam"
print(type(inputvalue))

inputvalue=9.09877665443221890
print(type(inputvalue))

#String concatenation
firstname="mariya"
secondname="  masood"
print(firstname+secondname)

#F String
days=365
print(f"there are {days} in a year")

#Escaping String
value="Hello \"Mariya\" here"
print(value)

#converting data type
price=45
new_price=float(price)
print("Price",new_price)
      
percentage=78.98
round=int(percentage)
print("percentage",round)

#Arithmatic operators
num1=2
num2=3
print("add",num1+num2)
print("sub",num1-num2)
print("mul",num1*num2)
print("expo",num1**num2)
print("div",num1/num2)

#short hand operator
num=5
num+=5
print(num)
num-=2
print(num)
num*=3
print(num)

#errors
#syntax error
print("hello"))
#name error
int=23
Int+=2
#zero devision
print(5%0)

#Function with input
def CalculateSum(var1,var2):
    print("Sum=",var1+var2)
CalculateSum(3,2)

#Function with output
def CalSum(var1,var2):
    return("Sum=",var1+var2)
print (CalSum(3,4)

#variable scope
rollno=105
def ShowVarScope():
    rollno=101
    print(rollno)
print(rollno)
ShowVarScope()

#conditions
#if conditions
number=int(input("check wather the number is positive or not"))
if number >= 0:
    print("Number is positive")

#else
number=float(input("check wather the number is positive or negative"))
if number >= 0:
    print("Number is positive")
else:
    print("Number is negative")

#elif
signal=input("what is traffic signal").lower()
if signal=="green":
    print("Car is allowed to go")
elif signal=="yellow":
    print("car has to wait")
elif signal=="red":
    print("Car has to stop")
else:
    print("invalid input")

#Multiple conditions
Eng_Marks=float(input("Enter your english sub marks"))
math_Marks=float(input("Enter your Math sub marks"))
Sci_Marks=float(input("Enter your Sci sub marks"))
percentage=((Eng_Marks+math_Marks+Sci_Marks)/300)*100
if percentage<0 or percentage>100:
    print("\"Invalid Input\"please enter proper value")
elif percentage<45:
    print("Grade= fail ):")
elif percentage==45 or percentage<=60:
    print("Grade= pass :)")
elif percentage==60 or percentage<=75:
    print("Grade= good :)")
elif percentage==75 or percentage<=85:
    print("Grade= very good :)")
elif percentage==85 or percentage<=100:
    print("Grade= excellent :)")


#loops
#for loop
total=0
number=int(input("Enter a number"))
for i in range(number):
    total=i+total
print(total)

#while loop
number=int(input("enter a number"))
while number<10:
    print(number)
    number+=1

#break
score=[11,43,46,12,678]
for s in score:
    if s>100:
        print("invalid")
        break
    print(s)

#_in a for loop
for value in range(1,10):
    print(value)

#list
list1=[1,11,1,'number',1]
print(list1[1])
print(type(list1))

#update list insert append
n=2
list1.append(n)
print(list1)
list2=[1,11,1,'number',1]

n=2
list2=[1,11,1,'number',1]
print(list2)
list2.insert(1,n)#(index_value,value)
print(list2)

#clear method
list1=[1,2,3]
list1.clear()
print(list1)
#shallow copy
list=[1,7,6]
list2=list.copy()
list2.insert(1,8)
print(list2)

#count() function
n=2
list1=[1,2,[1,11],[2,22]]
n1=list1.count(n)
print(n1)

list1=[1,2,'h','i']
co=0
for i in list1:
    co+=1
print(co)

city=['mumbai',' pune',]
newcity=['panvel']
city.extend(newcity)
print(city)

#extend
numbers=[1,2,3,4]
newnumbers=(5,6,7)
numbers.extend(newnumbers)
print(numbers)

numbers=[1,2,3,4]
newnumbers=[5,6,7]
numbers.extend(newnumbers)
print(numbers)


#insert
list1=[1,3,4]
list1.insert(1,2)
print(list1)

#pop
list1=[1,11,111,1111,11111]
print(list1)
print(list1.pop())
print(list1)
print(list1.pop(2))

#index
list1=[1,1,11,2,11,22,33,11]
pos=list1.index(11)
print(pos)
pos1=list1.index(11,pos+3)
print(pos1)

#remove
list1=[1,12,13,14,15,16]
list1.remove(15)
print(list1)

#reverse
list1=[5,4,3,2,1]
list1.reverse()
print(list1)

#slicing
list1=['mariya','maroof','masood','nuzhat']
#n=list1[::-2]
n=list1[1:3]  #[start index: end index -1]
print(n)

#sort
list1=[2,3,1,5,7,5]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#round
n=12.6
print(round(n))

#absolute
n=-2.36
print(abs(n))


class Animal:
    def breathe(self):
        print("breathing")
class Fish(Animal):
    def breathe(self):
        #super.breathe()
        print("under water")
n=Fish()
n.breathe()


n="""hello world"""
print(n)


#split in string
name="mariya masood shaban"
new=name.split()
print(new)

name='mariya masood shaban'
firstName,2ndName,Lastname=name.split(' ')
print(1stName)

print('mariya',end='')
print('shaban',end='')


#join
#dictionaries
numbers={'one':1,'two':2,'three':3}
print(numbers)
print(numbers['two'])
numbers['four']=4
print(numbers)
numbers['one']=0
print(numbers)

name='mariya'
print(name[-3:])

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print('/'.join([month, day, year]))

#format
name='mariya'
print(name+'hello')
rollno=234
print('hello '+name+' your rollno is '+str(rollno))


#converting from 1 data type to other
l=[1,2,3,4,1]
newtuple=tuple(l)
print(newtuple)
newset=set(l)
print(newset)
l1=['name','id']
l2=['Mariya','1432']
newd=dict(zip(l1,l2))
print(newd)
'''

















