pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biriyani", "Indian", 45, "Hard")
print("Recipe 1: ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])
print("\nRecipe 2: ", biryani)
print("Name: ", biryani[0])
print("Cuisine: ", biryani[1])
print("Difficulty: ", biryani[-1])

recipes = (pasta, biryani)
print("\nFirst recipe name: ", recipes[0][0])
print("Second recipe time: ", recipes[1][2])
print("Pasta details (summary): ", recipes[0][1:3])
for detail in recipes[0]:
    print("-\t", detail)

pasta_ing = {"tomato", "garlic", "olive oil", "chilli", "garlic", "pasta"}
print("\n To make pasta (OLD): ", pasta_ing)
biryani_ing = {"tomato", "garlic", "chilli", "chicken", "rice", "spices"}
print(" To make biryani: ", biryani_ing)

pasta_ing.add("parmesan")
pasta_ing.discard("chilli")
print("\n To make pasta (NEW): ", pasta_ing)

both = pasta_ing.union(biryani_ing)
common = pasta_ing.intersection(biryani_ing)
pasta_exclusive = pasta_ing.difference(biryani_ing)
unique = pasta_ing.symmetric_difference(biryani_ing)

print("\nIngredients to make both ", both)
print("Ingredients that are common ", common)
print("Ingredients that are exclusive to pasta ", pasta_exclusive)
print("Ingredients that are unique to each ", unique)