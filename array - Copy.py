#arrays
fruits = ["apple", "mango","cherry","banana"]
x = fruits[0]
print(x)

#length
x = len(fruits)
print(x)

#loop
for x in fruits:
    print(x)
    
    
#add any element
fruits.append("kiwi")
print(fruits)

#remove
fruits.remove("banana")
print(fruits)

#pop
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)

#clear
fruits.clear()
print(fruits)

# copy
fruits = ["apple", "mango","cherry","banana"]
fruits.copy()
print(fruits)


#count
fruits.count(1)
print(fruits)


#extend
fruits.extend("strawberry")
print(fruits)


#index
x=fruits.index("banana")
print(x)

#reverse
fruits.reverse()
print(fruits)

#sort
fruits.sort()
print(fruits)