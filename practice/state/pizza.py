class Pizza():
    def __init__(self, index, num_ingredients, ingredients):
        self.index = index
        self.ingredients = set(ingredients)
        self.num_ingredients = num_ingredients

    def __str__(self):
        return "{} ".format(self.index) + " ".join(self.ingredients)

class PizzaAllocation():
    def __init__(self):
        self.pizzas_for_team = []
        self.diff_ings = set()

    def add_pizza(self, pizza):
        if pizza is None:
            return False

        self.pizzas_for_team.append(pizza)
        self.diff_ings = self.diff_ings | pizza.ingredients
        return True