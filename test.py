import chess

board = chess.Board("r2qkbnr/ppp1pppp/2n5/3p1b2/2PP1B2/1Q6/PP2PPPP/RN2KBNR b KQkq - 2 4")
alt_board = chess.Board("r2qkbnr/ppp1pppp/2n5/3p1b2/2PP1B2/1Q6/PP2PPPP/RN2KBNR w KQkq - 2 4")
check_board = chess.Board("rnbqkbnr/ppp1pppp/8/1B6/3Pp3/8/PPP2PPP/RNBQK1NR b KQkq - 1 3")

with open("chess-doc.txt", "w", encoding="utf-8") as f:
    f.write("black to move:\n")
    f.write(board.__str__())
    f.write("\n\n")

    f.write("chess.Board.turn\n")
    f.write(board.turn.__str__())
    f.write("\n\n")

    f.write("white to move:\n")
    f.write(alt_board.__str__())
    f.write("\n\n")

    f.write("chess.Board.turn\n")
    f.write(alt_board.turn.__str__())
    f.write("\n\n")

    f.write("(now the black-to-move version is used again)\n\n")

    f.write("chess.Board.attackers(chess.Board.turn, chess.D4)\n")
    f.write(board.attackers(board.turn, chess.D4).__str__())
    f.write("\n\n")

    f.write("chess.Board.attackers_mask(chess.Board.turn, chess.C4)\n")
    f.write(board.attackers_mask(board.turn, chess.C4).__str__())
    f.write("\n\n")

    f.write("chess.Board.attacks(chess.B1)\n")
    f.write(board.attacks(chess.B1).__str__())
    f.write("\n\n")

    f.write("chess.Board.attacks(chess.B3)\n")
    f.write(board.attacks(chess.B3).__str__())
    f.write("\n\n")

    f.write("chess.Board.bishops\n")
    f.write(board.bishops.__str__())
    f.write("\n\n")

    f.write("chess.Board.can_claim_draw()\n")
    f.write(board.can_claim_draw().__str__())
    f.write("\n\n")

    f.write("chess.Board.captures_compulsory\n")
    f.write(board.captures_compulsory.__str__())
    f.write("\n\n")

    f.write("chess.Board.pieces(chess.BISHOP, chess.WHITE)\n")
    f.write(board.pieces(chess.BISHOP, chess.WHITE).__str__())
    f.write("\n\n")

    f.write("chess.Board.piece_at(chess.A1)\n")
    f.write(board.piece_at(chess.A1).__str__())
    f.write("\n\n")

    f.write("chess.Board.checkers()\n")
    f.write(board.checkers().__str__())
    f.write("\n\n")

    f.write("=== new board just for .checkers() ===\n")
    f.write(check_board.__str__())
    f.write("\n\n")

    f.write("chess.Board.checkers()\n (with the above board)")
    f.write(check_board.checkers().__str__())
    f.write("\n\n")

    f.write("chess.Board.checkers_mask()\n")
    f.write(check_board.checkers_mask().__str__())
    f.write("\n=== (other board again) ===")
    f.write("\n\n")

    f.write("chess.Board.checkers_mask()\n")
    f.write(board.checkers_mask().__str__())
    f.write("\n\n")

    f.write("chess.Board.status()\n")
    f.write(board.status().__str__())
    f.write("\n\n")
