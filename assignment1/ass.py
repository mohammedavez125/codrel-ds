#Python basics

#1) Assign values to variables "name' 'age' 'height' then print
name = "avez"
age = 19
height = "5'10"
print(f"my name is: {name} \nmy age is: {age} \nmy height is: {height}")

"""
OUTPUT:-
my name is: avez 
my age is: 19 
my height is: 5'10
"""

#2) Convert a float value into an integer and print out the type of the result.
float_num = 6.9
int_num=int(float_num)
print(float_num)
print(int_num)

"""
OUTPUT:-
6.9
6
"""

#List
#3) create a list which includes a) even months and b) odd months

odd_months=["january","march","may","july","september","november"]
even_months=["february","april","june","august","october","december"]

#4) Access 3rd element from even months list and 4th element from odd months list

print(odd_months[4]+" "+even_months[3])

"""
OUTPUT:-
september august
"""

#5) Access 1 to 5 elements from even-months list

print(even_months[slice(5)])

"""
OUTPUT:-
['february', 'april', 'june', 'august', 'october']
"""

#6) Add days (ex:monday) to the even month list

days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for i in range(len(days)):
    even_months.append(days[i])
print(even_months)

"""
OUTPUT:-
['february', 'april', 'june', 'august', 'october', 'december','monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
"""

#Functions

#7) Print the length of the odd-month list

print(len(odd_months))

#8)Print the type of odd-month list

print(type(odd_months))

#9) Delete the 5th element of the odd-month list

odd_months.pop(4)
print(odd_months)

#10) Replace the 6th 2 element of the odd list with saturday



"""
OUTPUT:-
6
<class 'list'>
['january','march','may', 'july', 'november']
"""
