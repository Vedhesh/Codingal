fruits = ["apple","banana","cherry"]
marks = (45,56,23,55)
student = {"name": "Aarav","age": 13}
colours = {"red","green","blue"}

#list operation
fruits.append("watermelon")
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.sort()
fruits.reverse()
print(fruits)
fruits.clear()

#dictionary operation
print(student.get("grade", "Error"))

student["grade"] = 7
print(student.get("grade", "Error"))

student.pop("grade")
print(student.get("grade", "Error"))

fruits = ["apple","banana","cherry"]
fruit_code = ["a", "b", "c"]

fruit_basket = list(zip(fruit_code, fruits))
print(fruit_basket)