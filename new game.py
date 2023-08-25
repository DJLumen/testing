import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.inventory = {}

    def add_to_inventory(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def show_inventory(self):
        print("\nInventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! You're about to embark on an adventure.")

    while player.health > 0:
        print("\nChoose an action:")
        print("1. Explore")
        print("2. Show Inventory")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            location = random.choice(["Forest", "Cave", "Town"])
            print(f"You've entered the {location}.")

            if location == "Forest":
                enemy = Enemy("Goblin", 30, 10)
                print(f"You encounter a {enemy.name}!")

                while enemy.health > 0 and player.health > 0:
                    action = input("What will you do? (attack/run): ")
                    if action == "attack":
                        player_attack = random.randint(0, player.attack)
                        enemy_attack = random.randint(0, enemy.attack)
                        enemy.health -= player_attack
                        player.health -= enemy_attack
                        print(f"You dealt {player_attack} damage to the {enemy.name}.")
                        print(f"The {enemy.name} dealt {enemy_attack} damage to you.")
                    elif action == "run":
                        break

                if enemy.health <= 0:
                    print(f"You defeated the {enemy.name}!")
                    player.add_to_inventory("Gold", random.randint(10, 20))

            elif location == "Cave":
                print("You find a treasure chest!")
                player.add_to_inventory("Treasure Chest")

            elif location == "Town":
                print("You've arrived at a peaceful town.")
                player.add_to_inventory("Bread", random.randint(1, 5))

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
