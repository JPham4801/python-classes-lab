class Game:
    round_id = 1

    def __init__(self, turn="X", winner=None, tie=False):
        self.turn = turn
        self.winner = winner
        self.tie = tie
        # fmt: off
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        # fmt: on

    def play_game(self):
        print(f"Round {Game.round_id}")

    def print_board(self):
        b = self.board
        print(
            f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """
        )

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        VALID_INPUTS = [
            "a1",
            "b1",
            "c1",
            "a2",
            "b2",
            "c2",
            "a3",
            "b3",
            "c3",
        ]

        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            # If the input is valid, update the board and break the loop
            if (
                move in VALID_INPUTS
                and self.board[move] is None
                and not self.winner
                and not self.tie
            ):
                self.board[move] = self.turn
                break
            else:
                print("Invalid input. Try again.")
            # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
        
    def check_winner(self):
        b = self.board
        # Check rows
        


game_instance = Game()
game_instance.render()
