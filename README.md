# Treasure Hunt Island!

## Instructions to run the program:

With the command line open, type "python \'treasurehunt.py\ -p1 name -p2 name'"
(or on mac type "python3 \'treasurehunt.py\ -p1 name -p2 name'") with -p2 being optional and the game should begin!

## Instructions on how to use the program:

Once command line is entered, the gmae will start with an introduction to the game such as the goal and description of each item's consequnecs. Given that player2 is an optional parameter of the main function, player2 should default to Hunter, our computer player. In that case, the player will be let known that they are playing against Hunter. However, if two players were written in the command line, then the program will be greet the two players. The game will start by welcoming the user and asking them to enter their name as the first player. As set_up_game method gets called, the user must type 'easy' or 'hard' when prompted what difficulty they want. If the second player is computer player, it will place its coordinates randomly. All human players must manually type in the coordinate for each item when prompted. For example, if the player wants to place their first item at A4, they would type 'a4' or 'A4'. If coordinates are invalid for the difficulty type, then an error will be raised in which the players would need to re-enter the coordinates.


## Now, the game begins! 

The terminal will display a board so that the player can keep track of the locations they've already guessed (however, if a player guesses a place they've already guessed they just get another try). Each "miss" will have an 'X' marked on that coordinate and each "hit" will have a letter appear that corresponds to the item that was found, the board will update after each turn. The first player will be prompted to enter a column, then row, of their guess as to where the treasure is. For example: if the player wants to guess the coordinate 'D1' they would enter 'd' or 'D' when asked for the column, then '1' when asked for the row. If there are two players, the second player will get their turn, otherwise the computer will guess randomly. The game will go back and forth between the players until someone finds either the Treasure or the Bomb, ending the game.

## Other Files:

Our program does not require other files so this is the only other file
    
## Attribution: 

| Method/Function | Primary Author | Technique Demonstrated |
| --- | --- | --- |
| parse_args & Player.place_item | Adom-Ahima Amissah | Argument Parser |
| Player.place_item | Adom-Ahima Amissah | Sequence Unpacking |
| Board.item_reveal | Aileen Ham | Set Operations |
| Main | Aileen Ham | Optional Parameters |
| ComputerPlayer Class | Deandre Germany | Super |
| TreasureHuntGame.set_up_game | Deandre Germany | Conditional Expressions |
| TreasureHuntGame.\_\_str\_\_ | Kirstin Nichols | Magic Methods |
| TreasureHuntGame and Board Classes | Kirstin Nichols | Composition of Two Custom Classes |
| Player.Guess_location | Remington Nelson | F-Strings |
| Player.\_\_init\_\_ | Remington Nelson | List Comprehension |
