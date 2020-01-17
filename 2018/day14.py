
data = "37"

recipes = [int(x) for x in data]

indexes = [0, 1]

f = 920831 + 11
j = f

while j := j - 1:
    recipe_sum = sum(recipes[index] for index in indexes)

    for new_recipe in str(recipe_sum):
        recipes.append(int(new_recipe))

    for i in range(len(indexes)):
        indexes[i] = (indexes[i] + recipes[indexes[i]] + 1) % len(recipes)

    if f - j - 10 == 5:
        print(recipes[f - j - 10: f - j])
    elif f - j - 10 == 18:
        print(recipes[f - j - 10: f - j])
    elif f - j - 10 == 2018:
        print(recipes[f - j - 10: f - j])
    elif f - j - 10 == f - 11:
        print(recipes[f - j - 10: f - j])
