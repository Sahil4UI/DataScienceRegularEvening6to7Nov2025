from pyscript import when
from pyscript import document

import random
player1Choice = "0"
player2Choice = "X"
wincombs = [[1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9]]

grid = document.querySelectorAll("button")

def player2Input():
    pos = random.randint(1,9)
    document.getElementById(f"btn-{pos}").innerText=player2Choice
    

for i in range(1, 10):
    @when("click", f"#btn-{i}")
    def handler(event, current_i=i):
        clicked_button = event.target
        
        # Change the text inside that specific button
        clicked_button.innerText = player1Choice

        player2Input()
        winnerCheck()

def winnerCheck():
    for comb in wincombs:
        if (grid[comb[0]-1].innerText==player1Choice) and (grid[comb[1]-1].innerText==player1Choice) and (grid[comb[2]-1].innerText==player1Choice):
            pass

