class Tomato:
    _states = {0: 'отсутсвует',
               1: 'цветение',
               2: 'зелёный',
               3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._states = self._states[0]

    def grow(self):
        key_value_now = list(Tomato._states.values()).index(self._states) + 1
        if key_value_now>3:
            key_value_now = 0
        self._states = Tomato._states[key_value_now]
        print(self._states)
    def is_ripe(self):
        if self._states==Tomato._states[3]:
            print(f"Помидорка {self._index} созрела!")
        else:
            print(f"Помидорка {self._index} ещё не созрела.")

class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(i) for i in range(amount)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        count = 0
        for i in self.tomatoes:
            if i._states == Tomato._states[3]:
                count = count+1
            else:
                break
        return count == self.amount

    def give_away_all(self):
        self.tomatoes = [Tomato(i) for i in range(self.amount)]

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print(f"{self.name} ухаживает за помидорками.")
    def harvest(self):
        if self._plant.all_are_ripe():
            print("Ура, всё созрело! Идём собирать урожай!")
        else:
            print("Ещё рано собирать урожай, остались зелёные помидорки!")
    @staticmethod
    def knowladge_base():
        print("Справка по садоводству:")
        print("1) Помидорки имеют 4 стадии созревания: отсутсвует, цветение, зелёные, красные")
        print("2) Садовник может за ними ухаживать или их собирать")
        print("3) Растение считается спелым, когда все помидорки на кусте покраснели")

tomatoBush = TomatoBush(5)
gardener = Gardener("Павел", tomatoBush)
Gardener.knowladge_base()
print(" ")
gardener.work()
print(" ")
gardener.harvest()
print(" ")
gardener.work()
print(" ")
gardener.work()
print(" ")
gardener.harvest()