class State():

    def __init__(self, num_pizzas, num_teams_2, num_teams_3, num_teams_4) -> None:
        self.value = None
        self.num_pizzas = num_pizzas
        self.num_teams_2 = num_teams_2
        self.num_teams_3 = num_teams_3
        self.num_teams_4 = num_teams_4
        self.pizzas = []
        self.pizza_allocation = {
            '2': [],
            '3': [],
            '4': []
        }

    def select_pizza_for_team(self, current_allocation):
        if len(self.pizzas) < 1:
            return None

        best_pizza = None
        max_ings = 0
        for pizza in self.pizzas:
            cur_ings = len(current_allocation.diff_ings | pizza.ingredients)
            if max_ings < cur_ings:
                max_ings = cur_ings
                best_pizza = pizza

        self.pizzas.remove(best_pizza)
        return best_pizza


    def calc_random_solution(self):
        """Calculates a random solution for the problem."""
        pass

    def get_all_neighbours(self, generator=True) -> list('State'):
        """Generates all neighbors of the current state."""
        return []

    def get_random_neighbour(self) -> 'State':
        """Generates a random neighbor."""
        return None

    def get_value(self) -> float:
        """Gets the value of the current state."""
        if self.value is None:
            self.value = self.calc_value()

        return self.value

    def calc_value(self):
        """Calculates the value for the current state."""
        val = 0
        for allocation in self.pizza_allocation['2']:
            val += len(allocation.diff_ings)**2

        for allocation in self.pizza_allocation['3']:
            val += len(allocation.diff_ings)**2

        for allocation in self.pizza_allocation['4']:
            val += len(allocation.diff_ings)**2

        return val

    def print(self):
        """Prints information about the current state."""
        print('*' * 50)
        print('Number of pizzas: {}'.format(self.num_pizzas))
        print('Number of teams of 2: {}'.format(self.num_teams_2))
        print('Number of teams of 3: {}'.format(self.num_teams_3))
        print('Number of teams of 4: {}'.format(self.num_teams_4))
        print('Pizzas:')
        for pizza in self.pizzas:
            print(pizza)
        print('Allocations: ')
        print('*' * 50)

    def __eq__(self, o: 'State') -> bool:
        return self.get_value() == o.get_value()

    def __lt__(self, o: 'State') -> bool:
        return self.get_value() < o.get_value()
