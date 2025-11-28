import subprocess
import unittest
import chess

POSITION_FEN_PREFIX = "position fen "

class StartPosTest(unittest.TestCase):

    def test_start_pos(self):
        
        cmd = ["python", "main.py"]
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        board = chess.Board(fen)
        print(board)
        print("")

        proc = subprocess.Popen(
            ["python", "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

        while (not board.is_game_over()):

            proc.stdin.write(POSITION_FEN_PREFIX + board.fen() + "\n")
            proc.stdin.flush()

            output = proc.stdout.readline().strip()
            uci_move = output.split()[-1]
            
            board.push_uci(uci_move)
            print(board)
            print("")

        proc.stdin.write("quit\n")
        proc.stdin.flush()
        proc.wait()
        proc.stdin.close()
        proc.stdout.close()

        print("Test passed: game ended successfully.")



if __name__ == "__main__":
    unittest.main()
