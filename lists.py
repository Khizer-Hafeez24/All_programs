print('names of list')
names=["Khurram", "Ali","Ahmed","Arif"]
print(names)
print('\n')
#replace names
print("replace name on index 1")
names=["Khurram", "Ali","Ahmed","Arif"]
names[1] = 'shafqat'
print(names)
#append a new name
names=["Khurram", "Ali","Ahmed","Arif"]
names.append("Ashraf")
print(names)
#insert  a new name on index2
print("insert name on index 2")
names=["Anisa", "sundas","maria","sidra"]
names.insert(4,"saiqa")
print(names)
print('\n')
print("extend list 1")
names=["Anisa", "sundas","maria","sidra"]
numbers=[1,2,3,4,5]
names.extend(numbers)
print(names)
list= names.copy()
print(list)


