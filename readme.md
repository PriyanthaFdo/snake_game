# Snake game
A classic Snake game implemented in Python using the Pygame library.

## Features
- Grid based movement: The snake moves on a grid using arrow keys.
- Boundry: The snake moves through the boundry to the other end of the screen without dying
- scoring: Each Food item gives +1 to the score
- Super food: A super food will appear randomly after 5 - 10 normal food. This item is time limited and consuming it within the given time will increase score by +3
- Growth: The snake will increase its length by 1 for each consumed food item (normal or super)
- Death: The game will end (sole method of ending) when snake bites itself

## Controls
- Arrow keys

## Installation
- Clone the repository or download the zip <br />
Clone Url: https://github.com/PriyanthaFdo/snake_game.git
Zip: (Click Here)[https://github.com/PriyanthaFdo/snake_game/archive/refs/heads/main.zip]

- Create a python virtual enviornment (optional)
Create: `python -m venv env`
Activate: `env\scripts\activate`

- Install requried modules
`python -m pip install -r requirements.txt`

- Run the game
`python game.py`