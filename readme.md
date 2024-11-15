# Snake game
A classic Snake game implemented in Python using the Pygame library.

## Features
- **Grid based movement:** The snake moves on a grid using arrow keys.
- **Boundry:** The snake moves through the boundry to the other end of the screen without dying
- **scoring:** Each Food item gives +1 to the score
- **Super food:** A super food will appear randomly after 5 - 10 normal food. This item is time limited and consuming it within the given time will increase score by +3
- **Growth:** The snake will increase its length by 1 for each consumed food item (normal or super)
- **Death:** The game will end (sole method of ending) when snake bites itself

## Controls
- Arrow keys

## Installation
- Clone the repository or download the zip <br />
  - Clone Url: https://github.com/PriyanthaFdo/snake_game.git <br />
  - Zip: [Click Here](https://github.com/PriyanthaFdo/snake_game/archive/refs/heads/main.zip)

- Create a python virtual enviornment (optional)<br />
  1. Create: `python -m venv env`<br />
  2. Activate: `env\scripts\activate`

- Install requried modules<br />
`python -m pip install -r requirements.txt`

- Run the game<br />
`python game.py`

## Screenshots
<img src="https://github.com/user-attachments/assets/6e783539-7479-4d9b-8da2-8c80a37c0822" width="24%">
<img src="https://github.com/user-attachments/assets/961ca197-f05a-4c4f-89a8-ec2ab928cd9b" width="24%">
<img src="https://github.com/user-attachments/assets/1f2a7d23-488f-4a04-84a7-138af74255ac" width="24%">
<img src="https://github.com/user-attachments/assets/bbe20325-c5fd-48eb-a45d-4c34112a4b09" width="24%">

***
## //TODO:
- Parameterize as much variables as possible
    - [ ] Show/hide grid
    - [ ] Super food min-max thresholds (default: 5 - 10)
    - [ ] Scores (default: normal - 1, super - 3)
    - [ ] Tick speed: (defaut: 10)
    - [ ] Move configuration variables into seperate file




