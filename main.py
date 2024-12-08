
from src.board import Board
from src.gameState import GameState
from src.move import Move, PromotionMove
from src.piece import Queen, Square


def main() -> None:
    g = GameState()
    print(g)
    m1 = Move(g.board.getPieceAt(Square(rank=2, file='e')), Square(rank=4, file='e'))
    g.ply(m1)
    print(g)
    m2 = Move(g.board.getPieceAt(Square(rank=7, file='e')), Square(rank=5, file='e'))
    g.ply(m2)
    print(g)
    m3 = Move(g.board.getPieceAt(Square(rank=1, file='g')), Square(rank=3, file='f'))
    g.ply(m3)
    print(g)
    m4 = Move(g.board.getPieceAt(Square(rank=8, file='g')), Square(rank=6, file='f'))
    g.ply(m4)
    print(g)
    m5 = PromotionMove(g.board.getPieceAt(Square(rank=2, file='a')), Square(rank=8, file='a'), Queen)
    g.ply(m5)
    print(g)

    
    

if __name__ == "__main__":
    main()