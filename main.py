import sys
import chess
import chess.polyglot
import chess.syzygy

GM_2001_BOOK_PATH = "donna_opening_books/gm2001.bin"
KOMODO_BOOK_PATH = "donna_opening_books/komodo.bin"
RODENT_BOOK_PATH = "donna_opening_books/rodent.bin"

ENDGAME_TABLEBASES_PATH = "syzygy"

def main():
    while True:
        input = sys.stdin.readline().strip()

        if (input.startswith("position fen")):
            fen = input.split("position fen ")[1].split(" moves")[0]
            move_as_uci_string = find_move(chess.Board(fen))
            print(f"bestmove {move_as_uci_string}")
            sys.stdout.flush()
        elif input == "quit":
            break

        else:
            print("Usage:")
            print("\tposition fen <FEN str> # to get the best move")
            print("\tquit                   # to exit program")
            sys.stdout.flush()



def find_move(board: chess.Board):
    # play opening move
    with chess.polyglot.open_reader(GM_2001_BOOK_PATH) as reader:
        for entry in reader.find_all(board):
            return entry.move.uci()
    
    # play endgame move
    best_move = None

    with chess.syzygy.open_tablebase(ENDGAME_TABLEBASES_PATH) as tablebase:
        distance_to_zero = tablebase.get_dtz(board)

        lowest_positive_dtz = 0
        lowest_negative_dtz = 0

        # draw
        if (distance_to_zero != None):

            if (distance_to_zero == 0):
            
                for move in board.legal_moves:
                    board.push(move)
                
                    if (tablebase.get_dtz(board) == 0):
                        return move.uci()
                
                    board.pop()

            # losing position  
            elif (distance_to_zero <= -1):
            
                for move in board.legal_moves:
                    board.push(move)
                    new_dtz = -tablebase.get_dtz(board)
                
                    if (new_dtz < lowest_negative_dtz):
                        lowest_negative_dtz = new_dtz
                        best_move = move
                
                    board.pop()

            # winning position
            elif (1 <= distance_to_zero):
                lowest_positive_dtz = distance_to_zero
            
                for move in board.legal_moves:
                    board.push(move)
                    new_dtz = abs(tablebase.get_dtz(board))

                    if (board.is_checkmate()):
                        return move.uci()

                    if (0 < new_dtz and new_dtz < lowest_positive_dtz):
                        lowest_positive_dtz = new_dtz
                        best_move = move

                    board.pop()

    if (best_move != None):
        return best_move.uci()
    
    # play middle game
    for move in board.legal_moves:
        return move.uci()

    
    
if (__name__ == "__main__"):
    main()
