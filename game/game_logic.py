import random
from models.player import Player
from models.enemy import Enemy
from database.setup import create_tables

def start_game():
    create_tables()
    print("Welcome to Chronicles of Eldoria!\n")
    
    while True:
        print("\nMain Menu:")
        print("1. Create a new character")
        print("2. View all characters")
        print("3. Choose an existing character")
        print("4. Delete a character")
        print("5. Exit")
        
        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            name = input("Enter your character's name: ")
            print("Choose your character's class:")
            print("1. Warrior")
            print("2. Mage")
            print("3. Rogue")
            class_choice = input("Enter your choice: ")

            character_classes = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
            character_class = character_classes.get(class_choice, "Warrior")

            player = Player(name, character_class)
            player.save()

            print(f"\nWelcome, {player.name} the {player.character_class}!")
            game_loop(player)

        elif main_choice == "2":
            players = Player.get_all()
            print("\nAll Characters:")
            for p in players:
                print(f"ID: {p.id}, Name: {p.name}, Class: {p.character_class}, Level: {p.level}, Health: {p.health}, Experience: {p.experience}")

        elif main_choice == "3":
            players = Player.get_all()
            print("\nChoose a character to play:")
            for p in players:
                print(f"ID: {p.id}, Name: {p.name}, Class: {p.character_class}, Level: {p.level}, Health: {p.health}, Experience: {p.experience}")
            player_id = int(input("Enter the ID of the character to play: "))
            player = Player.find_by_id(player_id)
            if player:
                print(f"\nWelcome back, {player.name} the {player.character_class}!")
                game_loop(player)
            else:
                print("Character not found.")

        elif main_choice == "4":
            player_id = int(input("Enter the ID of the character to delete: "))
            player = Player.find_by_id(player_id)
            if player:
                Player.delete(player_id)
                print(f"Player {player.name} has been deleted.")
            else:
                print("Character not found.")
                
        elif main_choice == "5":
            print("Thank you for playing Chronicles of Eldoria!")
            break
        else:
            print("Invalid choice. Please try again.")

def game_loop(player):
    while True:
        print("\n**Quest 1: The Goblin Menace**")
        print("Description: Reports have surfaced of goblin raids on nearby villages. The townsfolk are in need of a brave hero to eliminate the goblin threat.")
        print("Options:")
        print("1. Accept the quest and head towards the Goblin-infested forest.")
        print("2. Decline the quest and explore the town further.")
        print("3. Save and exit to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            goblin = Enemy("Goblin", 50, random.randint(5, 15))
            goblin.save()
            print("\nYou accept the quest and venture into the dense forest. Soon, you encounter a group of goblins preparing for their next raid.\n")
            while goblin.health > 0 and player.health > 0:
                print("**Combat Interface:**")
                print(f"Your Health: {player.health}")
                print(f"Enemy Health: {goblin.health}")
                print("Options:")
                print("1. Attack")
                if player.character_class == "Mage":
                    print("2. Cast Spell")
                elif player.character_class == "Rogue":
                    print("3. Sneak Attack")

                combat_choice = input("Enter your choice: ")

                if combat_choice == "1":
                    damage = player.attack()
                    goblin.health -= damage
                    print(f"You attack the goblin and deal {damage} damage!")

                elif combat_choice == "2" and player.character_class == "Mage":
                    damage = player.cast_spell()
                    goblin.health -= damage
                    print(f"You cast a spell and deal {damage} damage!")

                elif combat_choice == "3" and player.character_class == "Rogue":
                    damage = player.sneak_attack()
                    goblin.health -= damage
                    print(f"You perform a sneak attack and deal {damage} damage!")

                else:
                    print("Invalid choice. The goblin takes advantage and attacks you!")
                    enemy_damage = goblin.attack()
                    player.health -= enemy_damage
                    print(f"The goblin attacks you and deals {enemy_damage} damage!")

                if goblin.health > 0:
                    enemy_damage = goblin.attack()
                    player.health -= enemy_damage
                    print(f"The goblin attacks you and deals {enemy_damage} damage!")

            if player.health <= 0:
                print("You were defeated by the goblins. Game Over.")
                break
            else:
                print("You defeated the goblins! Quest completed.")
                player.experience += 50
                if player.experience >= 100:
                    player.level_up()
                player.save()

                print(f"\nDo you want to continue your adventure or end the game?")
                print("1. Continue")
                print("2. End Game")

                next_choice = input("Enter your choice: ")
                if next_choice == "2":
                    print("Thank you for playing Chronicles of Eldoria!")
                    break

        elif choice == "2":
            print("You decide to explore the town further. (More content coming soon...)")
            break
        elif choice == "3":
            player.save()
            print("Game saved. Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")
