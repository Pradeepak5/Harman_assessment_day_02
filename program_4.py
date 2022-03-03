
name_list=[]
age_list=[]
des_list=[]
salary_list=[]
count=int(input("how many person are there : "))
for i in range(0,count):
    name=input("enter the name :")
    age=input("enter the age :")
    des=input("enter designation of the person :")
    salary=int(input("enter the salary :"))
    name_list.append(name)
    age_list.append(age)
    des_list.append(des)
    salary_list.append(salary)

print(name_list)
print(age_list)
print(des_list)
print(salary_list)