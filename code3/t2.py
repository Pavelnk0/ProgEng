import random

def dice_roll():
    value = random.randint(1, 6)
    print(f"Выпало: {value}")
    if value == 5 or value == 6:
        print("Вы победили")
    elif value == 3 or value == 4:
        dice_roll()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    dice_roll()