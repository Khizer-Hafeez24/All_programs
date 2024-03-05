#print this list
alpha=['a','b','c','d']
print(alpha)
#extent lists
alpha=['a','b','c','d'];
beta=['e','f'];
gama=alpha.extend(beta)
print(alpha)
#list length
alpha=['a','b','c','d'];
print(len(alpha))
#append data
alpha=[1,2,3,4,5,6]
x=[7,8,9,10,11,12,13]
gama=(alpha+x)
print(gama)
#remove data
x=[7,8,9,10,11,12,13]
x.remove(8)
#loop list print all list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#dictionary functions
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["year"]=2018
#year change
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#add some item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#remove item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#del dictionary
