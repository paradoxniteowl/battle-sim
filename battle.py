from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # health points
        self.hpmax = self.hp
        self.ap = 3 # action points
        self.atk1 = 2 # first attack
        self.atk1ap = 1 # ap for atk1
        self.atk2 = 8 # second attack
        self.atk2ap = 3 # ap for atk2

player = Actor()
enemy = Actor()

def attack():
    while enemy.hp > 0:
        is_blocked = False
        print(f"Player: HP - {player.hp}, AP - {player.ap}")
        print(f"Enemy: HP - {enemy.hp}")
        print(f"1. Weak attack - (AP={player.atk1ap}, DMG<={player.atk1})")
        print(f"2. Strong attack - (AP={player.atk2ap}, DMG<={player.atk2})")
        print(f"3. Block (AP = 0, success chance = 80%)")
        print(f"4. Wait (AP + 1)")
        action = input(">> ")

        if action == "1" and player.ap >= player.atk1ap:
            print(f"You did {player.atk1} damage.")
            enemy.hp -= player.atk1
            player.ap -= player.atk1ap
        elif action == "2" and player.ap >= player.atk2ap:
            damage = randint(player.atk2/2, player.atk2)
            print(f"You did {damage} damage.")
            enemy.hp -= damage
            player.ap -= player.atk2ap
        elif action == "3":
            chance = randint(1,100)
            if chance >= 20:
                print("You successfully blocked the enemy's attack")
                is_blocked = True
            else:
                print("You failed to block the enemy's attack")
                is_blocked = False
        elif action == "4":
            player.ap += 2
        else:
            print("You are too exhausted to perform that action.")
        return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked and enemy > 0 and enemy.ap > 0:
        print(f"The enemy did {enemy.atk1} damage")
        player.hp -= enemy.atk1
        enemy.ap -= enemy.atk1ap
    if enemy.ap == 0:
        enemy.ap += 2

def start():
    print("This is the battle system")
    while enemy.hp > 0 or player.hp > 0:
        enemy_attack(attack())
    if enemy.hp <= 0:
        print("The enemy died")
        print(f"player HP - {player.hp}")
    elif player.hp <= 0:
        print("You died!")
    input("Press Enter to return to the Main Menu")