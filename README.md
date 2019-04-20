# rock-paper-scissors
A basic Rock Paper Scissors game created for a Udacity Nanodegree Program. Right now its pretty embarassing and I need to go back and clean it up when I have less pressing projects.

Under default behavior it runs you through "tournament" where you must beat 4 computer controlled opponents in a best of 5 match of rock, paper, scissors. 

## Players
### Player
The parent class of other players. It always plays rock and does not "learn"

### HumanPlayer
A human controlled player. Allows, rock, paper, and scissors (**not** case sensitive) as inputs. 

### RandomPlayer
Choses plays at random.

### ReflectPlayer
Choses a random move the first round, then mimics its opponent's last move in further rounds.

### CyclePlayer
Plays rock, paper, scissors in order.
