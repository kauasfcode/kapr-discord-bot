from numpy import random
def roll_initiative(entity_list):
    print(entity_list)
    entities = entity_list.split(" ")
    initiative_dict = {}
    reply = ""
    for entity in entities:
        entity_dice_value = random.randint(1,21)
        initiative_dict[entity] = entity_dice_value
    initiative_dict = sorted(initiative_dict.items(), 
                             key=lambda x: x[1], 
                             reverse=True)
    for user_and_result in initiative_dict:
        reply += f"👉 {user_and_result[0]} 🎯 {user_and_result[1]}\n"    
    return reply