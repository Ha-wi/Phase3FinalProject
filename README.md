Chronicles of Aluposiak

Welcome to Chronicles of Aluposiak, an interactive text-based RPG game where you embark on thrilling quests, battle fierce enemies, and grow your character.
Features

-Character Creation: Create a new character and choose from three different classes: Warrior, Mage, or Rogue.
-Character Management: View all characters, choose an existing character to play, save progress, and delete characters.
-Quest System: Engage in quests to gain experience and level up your character.
-Combat System: Battle enemies with class-specific abilities.
File Descriptions

main.py

The entry point of the game. It initializes and starts the game.

models/player.py

Defines the Player class, including attributes and methods for creating, saving, deleting, and managing player characters.

models/enemy.py

Defines the Enemy class, including attributes and methods for creating, saving, deleting, and managing enemies.

database/setup.py

Contains the create_tables function to initialize the database and create necessary tables.

game/game_logic.py

Contains the core game logic, including the main game loop, quest handling, and combat system.

How to Play

1.Main Menu:

1. Create a new character: Follow the prompts to create a new character and start playing.
2. View all characters: Display all saved characters.
3. Choose an existing character: Select a character by ID to continue playing with.
4. Delete a character: Delete a character by ID.
5. Exit: Exit the game.
   
2.In-Game:

Quest 1: The Goblin Menace: Accept the quest and battle goblins. Use your class-specific abilities to defeat enemies.
Save and Exit: Save your progress and return to the main menu.

Installation

Clone the repository
git clone https://github.com/yourusername/chronicles_of_aluposiak.git

Install required packages:
pip install sqlite3

Usage

Run the game:
python main.py

License
This project is licensed under the MIT License.

