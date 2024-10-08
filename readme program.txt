import random //impor library untuk pengacakan angka
import time //impor library untuk countdown waktu
class Robot: //membuat suatu kelas baru 
    def __init__(self, name) -> None: 
        self.name = name; //mendefinisikan nama

    health = 100; //pemberian nyawa robot

print("Choose robots for the battle:"); //text pemilihan robot untuk player
print("1. RoboVic \n2. RoboTor \n3. RoboLim"); //opsi robot yang dapat dipilih

num_name = {1:"RoboVic", 2: "RoboTor", 3:"RoboLim"} //mendefinisikan angka untuk setiap robot

first_robot = Robot(num_name[int(input("Select the first robot: "))]) //pemilihan robot player 1
second_robot = Robot(num_name[int(input("Select the second robot: "))]) //pemilihan robot player 2

while first_robot.health > 0 and second_robot.health > 0: //membuat suatu loop yang bekerja sampai nyawa robot <=0
    first_damage = random.randint(1, 20) //damage robot 1 random antara 1-20
    second_damage = random.randint(1, 20) //damage robot 2 random antara 1-20
    print(f"{first_robot.name} attacks {second_robot.name} for {first_damage} damage") //teks penyerangan
    if first_damage < 10: 
        print("basic attack") //apabila damage random kurang dari 10, serangan berupa basic attack
    elif first_damage < 15:
        print ("superb attack") //apabila damage random kurang dari 15, serangan berupa superb attack
    elif first_damage < 20:
        print("head-shot") //apabila damage random kurang dari 20, serangan berupa head-shot
    time.sleep (1) //delay 1 detik
    print(f"{second_robot.name} attacks {first_robot.name} for {second_damage} damage") //pengulangan seperti diatas
    if second_damage < 10:
        print("basic attack")
    elif second_damage < 15:
        print ("superb attack")
    elif second_damage < 20:
        print("head-shot")
    time.sleep (1)

    first_robot.health = first_robot.health - second_damage; //nyawa akhir robot 1 adalah nyawa awal-total serangan robot 2
    second_robot.health = second_robot.health - first_damage; //nyawa akhir robot 2 adalah nyawa awal-total serangan robot 1

if first_robot.health < 0:
    first_robot.health = 0 //apabila nyawa robot 1 kurang dari 0, nyawa yang ditulis tetap 0, karena tidak mungkin negatif
if second_robot.health < 0:
    second_robot.health = 0 //apabila nyawa robot 2 kurang dari 0, nyawa yang ditulis tetap 0, karena tidak mungkin negatif

print(f"{first_robot.name}'s health: {first_robot.health}\n{second_robot.name}'s health: {second_robot.health}") //output nyawa kedua robot

health_list = sorted([first_robot.health, second_robot.health]) //pengurutan agar nyawa robot dioutput mulai dari yang lebih kecil
dict_winner = {first_robot.health:first_robot.name, second_robot.health:second_robot.name}

if first_robot.health == second_robot.health:
    print("Its a Tie!"); //menuliskan seri apabila nyawa kedua robot sama
else:
    print(f"the winner is: {dict_winner[health_list[-1]]}\n and unfortunetly, {dict_winner[health_list[0]]} loses") //menuliskan robot yang menang dan kalah
