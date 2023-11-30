def read_recipes(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    cook_book = {}
    current_recipe = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.isdigit():
            num_ingredients = int(line)
            current_recipe = []
            continue

        if current_recipe is not None and len(current_recipe) < num_ingredients:
            ingredient = line.split(' | ')
            ingredient_name = ingredient[0]
            quantity = int(ingredient[1])
            measure = ingredient[2]

            current_recipe.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        if current_recipe is not None and len(current_recipe) == num_ingredients:
            recipe_name = current_recipe[0]['ingredient_name']
            cook_book[recipe_name] = current_recipe
            current_recipe = None

    return cook_book


cook_book = read_recipes('recipes.txt')

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        recipe = cook_book.get(dish)
        if recipe:
            for ingredient in recipe:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count)

for ingredient, info in shop_list.items():
    print(f"{ingredient}: {info['quantity']} {info['measure']}")