from pyscript import when
from pyscript import document
from js import console
import random
player1Choice = "0"
player2Choice = "X"
wincombs = [[1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9]]

occupied = []

grid = document.querySelectorAll("button")
win = document.getElementById("wins")

def player2Input():
    pos = random.randint(1,9)
    document.getElementById(f"btn-{pos}").innerText=player2Choice
    occupied.append(pos-1)
    

for i in range(1, 10):
    
    @when("click", f"#btn-{i}")
    def handler(event):
        clicked_button = event.target
        
        # Change the text inside that specific button
        
        if int(clicked_button.id[-1])-1 in occupied:
            print("Try AGAIN")
            return
        
        clicked_button.innerText = player1Choice
        occupied.append(int(clicked_button.id[-1])-1)  
        player2Input()
        winnerCheck()
        print(occupied)
        console.log("*********")

def winnerCheck():

    if len(occupied)==9:
        win.innerText = "DRAW"
    else:
        for comb in wincombs:
            if (grid[comb[0]-1].innerText==player1Choice) and (grid[comb[1]-1].innerText==player1Choice) and (grid[comb[2]-1].innerText==player1Choice):
                win.innerText=player1Choice

            elif (grid[comb[0]-1].innerText==player2Choice) and (grid[comb[1]-1].innerText==player2Choice) and (grid[comb[2]-1].innerText==player2Choice):
                win.innerText=player2Choice   
     
    
    return
