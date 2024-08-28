class Game:
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
        print("Let's play a classic game of TIC-TAC-TOE!")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()

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
                # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
                print("Invalid input. Try again.")

    def check_for_winner(self):
        b = self.board

        if b["a1"] and b["a1"] == b["b1"] == b["c1"]:
            self.winner = b["a1"]
        elif b["a2"] and b["a2"] == b["b2"] == b["c2"]:
            self.winner = b["a2"]
        elif b["a3"] and b["a3"] == b["b3"] == b["c3"]:
            self.winner = b["a3"]
        elif b["a1"] and b["a1"] == b["a2"] == b["a3"]:
            self.winner = b["a1"]
        elif b["b1"] and b["b1"] == b["b2"] == b["b3"]:
            self.winner = b["b1"]
        elif b["c1"] and b["c1"] == b["c2"] == b["c3"]:
            self.winner = b["c1"]
        elif b["a1"] and b["a1"] == b["b2"] == b["c3"]:
            self.winner = b["a1"]
        elif b["c1"] and b["c1"] == b["b2"] == b["a3"]:
            self.winner = b["c1"]

    def check_for_tie(self):
        if None not in self.board.values() and not self.winner:
            self.tie = True

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"


game_instance = Game()
game_instance.play_game()
