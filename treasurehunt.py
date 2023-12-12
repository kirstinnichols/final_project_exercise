from argparse import ArgumentParser 
import sys 
import random



class Player:
    """
    Represents a player in the Treasure Hunt game.
    
    Attributes: 
    - name(str): the name of the player.
    - item(str): the item to be placed.
    - row(str): the row where the item is placed (letter A-J).
    - col(int): the column where the item is placed (1-10).
    
    """

    def __init__(self, name):
        """
        Initializes a new Player instance.

        Args:
        - name (str): The name of the player.
        
        Side effect: 
        - instantiates self.items, self.extra_turn, and self.skips_turn

        Primary Author: Remington Nelson
        Technique: List Comprehension
        """
        self.name = name
        self.items = {item: None for item in ['Treasure Chest', 'Broken Glass', 'Shovel', 'Bomb']}
        self.extra_turn = False
        self.skips_turn = False
    
    def place_item(self, item, new_coords):
        """ Places an item in the player's grid
        
        Args: 
            item (str): The item to be placed 
            new_coords (tuple): the row and the column placed
        """
        row, col = new_coords

        if any(coords == new_coords for coords in self.items.values() if coords is not None):
            return ValueError
        
        else:
            self.items[item] = new_coords
       
    
    def guess_location(self, grid_size, board):
        """
        Takes input from the player to guess the location of the treasure chest.
 
        Parameters:
        - grid_size (int): The size of the game grid.
        - board (Board): The game board.

        Returns:
        tuple: The player's guess in the format (row, column).

        Primary Author: Remington Nelson
        Technique: F-Strings
        """

        
        while True:
            row = input(f'''{self.name}, what ROW do you think the treasure chest is at?
            Enter a letter A-{chr(65 + grid_size - 1)}: ''').upper()

            if 'A' <= row <= chr(65 + grid_size - 1) and len(row) == 1:
                col = input(f'''What COLUMN do you think the treasure chest is at?
            Enter a number 1-{grid_size}: ''')

                if col.isdigit() and 1 <= int(col) <= grid_size:
                    col = int(col)
                    guess = (row, col)
                    if guess not in board.guesses:
                        return guess
                    else:
                        print("You already guessed this location. Try again.")
                else:
                    print(f"Invalid input. Please enter a valid integer for the column (1-{grid_size}).")
            else:
                print(f"Invalid input. Please enter a valid row (A-{chr(65 + grid_size - 1)}).")

 

class Computer(Player):
    """
    primary author Deandre Germany
    Represents a computer player in the Treasure Hunt game.
    """
    def __init__(self, name):
        """Initializes class
        Args: name(str): name of player"""
        super().__init__(name)

    def place_items_randomly(self, grid_size):
        """
        Places items randomly on the computer player's grid.

        Args:
        - grid_size (int): The size of the game grid.
        """
        self.place_item('Treasure Chest', (chr(random.randint(65, 65 + grid_size - 1)), random.randint(1, grid_size)))
        self.place_item('Broken Glass', (chr(random.randint(65, 65 + grid_size - 1)), random.randint(1, grid_size)))
        self.place_item('Shovel', (chr(random.randint(65, 65 + grid_size - 1)), random.randint(1, grid_size)))
        self.place_item('Bomb', (chr(random.randint(65, 65 + grid_size - 1)), random.randint(1, grid_size)))
        
    def guess_location(self, grid_size, board):
        """
        Generates a random guess for the computer player.

        Args:
        - grid_size (int): The size of the game grid.
        - board (Board): The game board.

        Returns:
        tuple: The computer player's guess in the format (row, column).
        """
        while True:
            row = chr(random.randint(65, 64 + grid_size))
            col = random.randint(1, grid_size)
            guess = (row, col)
            
            if guess not in board.guesses:
                print(f"Hunter's guess was {guess}")
                return guess
      
        
class Game:
    """Allows user to play Game based on their own input and either the input of 
    either a second user or the computer. 
    
    Attributes:
        players(list): list of players 
        grid_size(int): the size of the game grid. 5 or 10.
        boards(list): list of Board objects.
        
    """
    
    def __init__(self, players):
        self.players = players
        self.grid_size = 0
        self.boards = [Board(0), Board(0)]

    def set_up_game(self):
        """
        primary author Deandre Germany
        Sets up the initial difficulty level and item placement of the Treasure Hunt game.

        Side effects: 
            defines row, col, and self.grid_size depending on user input
            prints invalid coordinates statement if contains Value error
        """
        
        difficulty = input('''Would you like to play on easy (5x5 grid) or hard mode (10x10 grid)? 
        Enter 'easy' or 'hard: ''')
        
        while not (difficulty == "easy" or difficulty == "hard"):
            difficulty = input("Please ONLY enter 'easy' or 'hard': ")
        
        self.grid_size = 5 if difficulty == "easy" else 10

        print("\nLet's begin by hiding our items on the island:")
        
        for player in self.players:
            if isinstance(player, Computer):
                player.place_items_randomly(self.grid_size)
            else:
                print(f"{player.name}, please enter the coordinates for each item in the following format 'A1'.\n")
                
                for item in player.items:
                    while True:
                        coords = input(f"{item}: ").strip().upper()
                        
                        if len(coords) < 2 or not coords[0].isalpha() or not coords[1:].isdigit():
                            print("Invalid format. Please enter coordinates in this format 'A1'.")
                            continue
                        
                        row = coords[0]
                        col = int(coords[1:])

                        if difficulty == "easy":
                            if row not in "ABCDE" or col not in range(1, 6):
                                print("Invalid coordinates. Please enter coordinates within A1-E5 range")
                                continue
                        elif difficulty == "hard":
                            if row not in "ABCDEFGHIJ" or col not in range(1, 11):
                                print("Invalid coordinates. Please enter coordinates within A1-J10 range")
                                continue

                        if player.place_item(item, (row, col)) == ValueError:
                            print("This coordinate is already assigned to another item. Please choose a different set of coordinates")
                            continue
                        else:
                            break
    def play_game(self):
        """Determines result of player action
        
        Side effects: determines value of player.skips_turn based on player action
                      adds guess to self.boards
                      changes value of item_at_guess depending on user choice
                      changes value of item_at_new_guess depending on user choice
                      prints statement if player won or loses
        
        Returns:
            Nothing, quits the game
                      
                      
        """
        print("\nNow that we have buried our items, time to start digging and find each other's treasure chest!")
        
        while True:
            for i, player in enumerate(self.players):
                
                if player.skips_turn:
                    print(f"{player.name} skips a turn from digging up the broken glass.")
                    player.skips_turn = False
                    continue
                print(f"\n{player.name}'s turn!\n")
                
                if not isinstance(player, Computer):
                    print(self.__str__(i))

                player_guess = player.guess_location(self.grid_size, self.boards[i])
                self.boards[i].add_guess(player_guess)
                

                if player_guess == self.players[1 - i].items['Treasure Chest']:
                    print(f"Congratulations {player.name}! You found the treasure chest and won the game!")
                    self.boards[i].item_reveal(player, self.players[1 - i], self.boards[1 - i])
                    return
                elif player_guess == self.players[1 - i].items['Bomb']:
                    print(f"Oh no, {player.name}! You uncovered the bomb. Game over!")
                    self.boards[i].item_reveal(player, self.players[1 - i], self.boards[1 - i])
                    return
                else:
                    item_at_guess = None
                    for item, coords in self.players[1 - i].items.items():
                        if player_guess == coords:
                            item_at_guess = item
                            break

                    if item_at_guess is not None:
                        self.handle_event_type(item_at_guess.lower() + '_found', player)
                        if player.extra_turn:
                            player.extra_turn = False
                            new_guess = player.guess_location(self.grid_size, self.boards[i])
                            self.boards[i].add_guess(new_guess)
                            
                            if new_guess == self.players[1 - i].items['Treasure Chest']:
                                print(f"Congratulations {player.name}! You found the treasure chest and won the game!")
                                self.boards[i].item_reveal(player, self.players[1 - i], self.boards[1 - i])
                                return
                            elif player_guess == self.players[1 - i].items['Bomb']:
                                print(f"Oh no, {player.name}! You uncovered the bomb. Game over!")
                                self.boards[i].item_reveal(player, self.players[1 - i], self.boards[1 - i])
                                return
                            else:
                                item_at_new_guess = None
                                for item, coords in self.players[1 - i].items.items():
                                    if new_guess == coords:
                                        item_at_new_guess = item
                                        break

                                if item_at_new_guess is not None:
                                    self.handle_event_type(item_at_new_guess.lower() + '_found', player)
                                else:
                                    print(f"Sorry {player.name}, that's not where the treasure chest is. Good luck on your next try!\n")
                                    

                    else:
                        print(f"Sorry {player.name}, that's not where the treasure chest is. Good luck on your next try!\n")
                        
                        
    def handle_event_type(self, event_type, player):
        """
        Handles the case where a bomb, shovel, or broken glass is found by the player, 
        resulting in the player losing the game (bomb), getting an extra turn (shovel),
        or losing a turn (broken glass).
        
        Args: 
        - event_type(str): string representing found item
        - player(str): string representing the player
        
        Side effects: changes value of player.extra_turn and player.skips_turn 
        based on event type
        """
        if event_type == 'bomb_found':
            print(f"Sorry {player.name}, you found the bomb placed your opponent. You lose!") 
        
        elif event_type == 'shovel_found':
            print(f"{player.name}, you found a shovel! You get an extra turn to dig again!")
            player.extra_turn = True
            
        elif event_type == 'broken glass_found':
            print(f'''Ouch! {player.name}, you found broken glass and injured yourself.
            Skip a turn while you bandage yourself up!''')
            player.skips_turn = True 
    



    def __str__(self, player_index):
        """Prints display board as formal string representation, determining how 
        to represent glass '[G]' and user choices '[X]'
        
        Args: player_index(str): index of the current player in the list of players
        """
        result = ""
        result += "    " + "   ".join(str(i) for i in range(1, self.grid_size + 1)) + "\n"
        for row in range(ord('A'), ord('A') + self.grid_size):
            result += chr(row) + "  "
            for col in range(1, self.grid_size + 1):
                current_position = (chr(row), col)

                if current_position in self.boards[player_index].guesses:
                    for item, coords in self.players[1 - player_index].items.items():
                        if current_position == coords:
                            if "glass" in item.lower():
                                result += "[G] "
                            else:
                                result += f"[{item[0]}] "
                            break
                    else:
                        result += "[X] "
                else:
                    result += "[ ] "
            result += "\n"
        return result
    



class Board:
    """
    Represents the game board in the Treasure Hunt game.
    """
    
    def __init__(self, grid_size):
            """
            Initializes a new Board instance.

            Args:
            - grid_size (int): The size of the game grid.
            """
            self.grid_size = grid_size
            self.all_coords = {(chr(row), col) for row in range(65, 65 + grid_size) for col in range(1, grid_size + 1)}
            self.guesses = set()
            self.missed_items = set()

    
    def item_reveal(self, player, other, otherPlayerBoard):
        """ Reveals location of remaining items 
        
        Args:
            player(Player): name of player that won/lost
            other(Player): name of other player
            otherPlayerBoard(Board): other player's board guesses
        
        Side effects:
            prints the location of the items for each player's board
            
        Aileen Ham, set operations
        """
            
        player_missed_items = set(other.items.values()) - self.guesses

        other_missed_items = set(player.items.values()) - otherPlayerBoard.guesses

        print(f'''Here are the locations of the items {player.name} has missed on {other.name}'s board: {player_missed_items}''')
        print(f'''and locations of items {other.name} has missed on {player.name}'s board: {other_missed_items}''')
    
    
    def add_guess(self, guess):
         
        """
        Adds a guess to the set of previous guesses on the board.

        Parameters:
        - guess (tuple): The guess to be added in the format (row, column).
        """
        unguessed_coords = self.all_coords - self.guesses
        if guess not in unguessed_coords:
            self.guesses.add(guess)
            


def main(player1, player2=None):
    """Creating instances of players to classes and set up and play game
    
    Args: 
        player1(str): name of player 1
        player2(str): name of player 2, default to None
    
    Side effects: 
        Prints intro to Treasure Hunt Island
        Changes player1 and player2 value based on user input
    
    Aileen Ham, optional parameters
    
    """
    
    print('''\n
    Welcome to Treasure Hunt Island! \n
    The objective of this game is to outwit your opponent and find their hidden treasure chest. \n
    But be cautious! The island is full of surprises ... \n
        * Shovel --- Dig it up for an extra turn. \n
        * Broken Glass --- Beware, it skips your next turn. \n
        * Bomb --- Uncover this and BOOM, it's game over. \n
    Find the treasure chest before your opponent does to win the game! Good luck!\n''')

    if player2 == None:
        print(f"Hello {player1}! You will be playing against our computer player, Hunter.")
        player1 = Player(player1)
        player2 = Computer("Hunter")

    else:
        print(f"Hello {player1} and {player2}! ")
        player1 = Player(player1)
        player2 = Player(player2)
        
    players = [player1, player2]


    game = Game(players)
    game.set_up_game()
    game.play_game()

def parse_args(arglist): 
    """ Parse command-line arguments
    
    Allow optional second player if applicable 
        - p1, --player1: name of the player
        - p2, --player2: name of the second player, if specified
    """
    parser = ArgumentParser()
    parser.add_argument("-p1", "--player1", help="name of player 1")
    parser.add_argument("-p2", "--player2", help="add a second player", default=None)
    
    args = parser.parse_args(arglist)
    return args.player1, args.player2

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(*args)
