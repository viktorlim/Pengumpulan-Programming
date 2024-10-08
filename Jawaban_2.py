import random
import time
class Robot:
    def __init__(self, name) -> None:
        self.name = name;

    health = 100;

print("Choose robots for the battle:");
print("1. RoboVic \n2. RoboTor \n3. RoboLim");

num_name = {1:"RoboVic", 2: "RoboTor", 3:"RoboLim"}

first_robot = Robot(num_name[int(input("Select the first robot: "))])
second_robot = Robot(num_name[int(input("Select the second robot: "))])

while first_robot.health > 0 and second_robot.health > 0:
    first_damage = random.randint(1, 20)
    second_damage = random.randint(1, 20)
    print(f"{first_robot.name} attacks {second_robot.name} for {first_damage} damage")
    if first_damage < 10:
        print("basic attack")
    elif first_damage < 15:
        print ("superb attack")
    elif first_damage < 20:
        print("head-shot")
    time.sleep (1)
    print(f"{second_robot.name} attacks {first_robot.name} for {second_damage} damage")
    if second_damage < 10:
        print("basic attack")
    elif second_damage < 15:
        print ("superb attack")
    elif second_damage < 20:
        print("head-shot")
    time.sleep (1)

    first_robot.health = first_robot.health - second_damage;
    second_robot.health = second_robot.health - first_damage;

if first_robot.health < 0:
    first_robot.health = 0
if second_robot.health < 0:
    second_robot.health = 0

print(f"{first_robot.name}'s health: {first_robot.health}\n{second_robot.name}'s health: {second_robot.health}")

health_list = sorted([first_robot.health, second_robot.health])
dict_winner = {first_robot.health:first_robot.name, second_robot.health:second_robot.name}

if first_robot.health == second_robot.health:
    print("Its a Tie!");
else:
    print(f"the winner is: {dict_winner[health_list[-1]]}\n and unfortunetly, {dict_winner[health_list[0]]} loses")

