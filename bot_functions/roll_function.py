from numpy import random

def roll_dice(dado):
    dice_formatted_results = []
    dice_list = dado.replace(" ", "").split("+")
    print(dice_list)
    for dice in dice_list:
        dice_result = []
        try:
            amount, sides = map(int, dice.split('d'))
        except:
            amount = 1
            sides = int(dice[1:])
        for i in range(0,amount):    
            dice_result.append(random.randint(1,sides+1))
        dice_formatted = f"{dice_result} {dice}"
        dice_formatted_results.append(dice_formatted)
    dice_formatted_results = " + ".join(dice_formatted_results)
    return dice_formatted_results