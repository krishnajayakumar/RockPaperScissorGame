'''
first_num = input("First number ")
second_num = input("Second number ")
sum = float(first_num)+float(second_num)
print("Sum is : ",sum)
'''
'''
course = "PYTHON for BEGINNERS "
print(course.upper())
'''
'''
course = "PYTHON FOR BEGINNERS"
print(course.find("G"))
'''
'''
course = "PYTHON FOR BEGINNERS"
print(course.replace('BEGINNERS','PROFESSIONALS')) '''

#COMPARISON OPERATOR
''' 
X = 3>2
print(X)
Y = 3==2
print(Y)
'''
weight = input("Weight : ")
unit = input("(K)g or (L)bs : ")
if unit.upper()== "K" :
    print(float(weight) * 2.20462 ,"Lbs")
else: print(float(weight)/2.20462, "Kg")
