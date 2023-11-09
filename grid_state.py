import random

class GameBoard:
    def __init__(self, difficulty="easy"):
        """
        Initialize the game board with the specified difficulty.

        Args:
        difficulty (str): Either "easy" (default) or "hard" to determine the grid size.
        """
        self.difficulty = difficulty
        self.grid_size = 8 if difficulty == "easy" else 10
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.items = [(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) for _ in range(self.grid_size)]

    def grid_state(self, guess):
        """
        Update the game board based on the player's guess.

        Args:
        guess (tuple): A tuple containing the player's guess as (row, column).

        Returns:
        str: A string representing the game board's current state.
        """
        row, col = guess

        if guess in self.items:
            self.items.remove(guess)
            self.grid[row][col] = 'X'  # Mark the item as found
        else:
            self.grid[row][col] = 'O'  # Mark the guess as a miss

    def __str__(self):
        """
        Provide a string representation of the game board's current state.

        Returns:
        str: A string representing the game board.
        """
        game_state = ""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) in self.items:
                    game_state += ' '
                else:
                    game_state += self.grid[i][j]
                game_state += ' '
            game_state += '\n'

        return game_state


difficulty = "hard"  
game = GameBoard(difficulty)

print(game)  
game.grid_state((1, 2))  
print(game)  
