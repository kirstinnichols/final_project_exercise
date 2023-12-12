# Treasure Hunt!

## Instructions to run the program:

With the command line open, type "python \'Final Project Check-in.py\'"
(or on mac type "python3 \'Final Project Check-in.py\'") and the game should begin!

## Instructions on how to use the program:

The game will start by welcoming the user and asking them to enter their name, which can be anything, for the first player. Then, the user will be asked how many players are playing. If only one player is playing then the second player will be the computer, while having two players will prompt the second user to enter their name. Next, the players will be asked if they want ‘easy’ mode or ‘hard’ mode. Then, the first player will be prompted to enter the column, and then the row, of each item that they need to place. For example, if the player wants to place their first item at A4, they would enter 'a' or 'A' when asked for the column, then '4' when asked for the row. If there is only one player then the computer will randomly place the items, if there are two players then the second player will be asked to place their items. Now, the game begins! The terminal will display a board so that the player can keep track of the locations they've already guessed (however, if a player guesses a place they've already guessed they just get another try). Each guess will have an 'X' marked on that coordinate and the baord will update after each turn. The first player will be prompted to enter a column, then row, of their guess as to where the treasure is. For example: if the player wants to guess the coordinate 'D1' they would enter 'd' or 'D' when asked fro the column, then '1' when asked for the row. If there are two players, the second player will get their turn,  otherwise the computer will guess randomly. The game will go back and forth between the players until someone finds either the Treasure or the Bomb, ending the game.

## Other Files:

Our program does not require other files so this is the only other file
    
## Attribution: 

| Method/Function | Primary Author | Technique Demonstrated |
| --- | --- | --- |
| parse_args & Player.place_item | Adom-Ahima Amissah | Argument Parser |
| Player.place_item | Adom-Ahima Amissah | Sequence Unpacking |
| BLANK | Aileen Ham | Set Operations |
| Main | Aileen Ham | Optional Parameters |
| ComputerPlayer Class | Deandre Germany | Super |
| TreasureHuntGame.set_up_game | Deandre Germany | Conditional Expressions |
| TreasureHuntGame.\_\_str\_\_ | Kirstin Nichols | Magic Methods |
| TreasureHuntGame and Board Classes | Kirstin Nichols | Composition of Two Custom Classes |
| Player.Guess_location | Remington Nelson | F-Strings |
| Player.\_\_init\_\_ | Remington Nelson | List Comprehension |