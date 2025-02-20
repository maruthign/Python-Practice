#dictionary
# A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
# Example
# Create and print a dictionary:

car={
    "brand":"volkswagan",
    "model":"polo",
    "year":2019
}
print(type(car))
print(car["year"])
#print(car["company"])
print(car.get("sudeep","not found"))
print(car.get("brand","not found"))
print(car)

# adding dictionary
car["color"]="red"
print(car)

# changing value
car["color"]="blue"
print(car)

# removing item
car.pop("color")
print(car)
del car["model"]
print(car)

# clear
car.clear()
print(car)

# dictionary methods
car={
    "brand":"volkswagan",
    "model":"polo",
    "year":2019
}
print(car.keys())
print(car.values())
print(car.items())

# update dictionary
cars={
    "color":"red",
    "varient":"top"
}
car.update(cars)
print(car)


# Nested dictionary

item1={
    "brand":"volkswagan",
    "model":"polo",
    "year":2019,
    "price":200000
}
item2={
    "brand":"maruti",
    "model":"swift",
    "year":2018,
    "price":100000
}
item3={
    "brand":"honda",
    "model":"city",
    "year":2017,
    "price":150000
}
items=[item1,item2,item3]
print(items)
print(f"total price : {item1['price']+item2['price']+item3['price']}rs")
