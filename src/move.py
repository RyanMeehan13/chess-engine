from typing import Literal
from src.piece import Bishop, King, Knight, Pawn, Piece, Queen, Rook, Square

class AbstractMove:
    """
    Representation of a chess move
    """
    piece: Piece
class Move(AbstractMove):
    """
    Representation of a standard chess move
    """
    target: Square
    def __init__(self, p, t) -> None:
        self.piece = p
        self.target = t
    def __repr__(self) -> str:
        return f"{self.piece.location}{self.target}"
    
class CastleMove(AbstractMove):
    """
    Representation of a castling move
    """
    side: Literal['q'] | Literal['k']
    def __init__(self, p, s) -> None:
        if not isinstance(p, King) or (s != 'q' or s != 'k'):
            raise ValueError("Invalid castle move")
        self.piece = p
        self.side = s
    def __repr__(self) -> str:
        if self.side == 'q':
            return 'O-O-O'
        if self.side == 'k':
            return 'O-O'
        raise ValueError("Invalid castle move")
    
class PromotionMove(Move):
    promoteTo: Knight | Bishop | Rook | Queen
    def __init__(self, p, t, to) -> None:
        if not isinstance(p, Pawn):
            raise ValueError("Non-Pawn types cannot promote")
        if not self._isCorrectPromotionRankByColor(p.color, t):
            raise ValueError("Invalid promotion move: Pawns cannot promote on this rank")

        super().__init__(p, t)
        self.promoteTo = to
    
    def __repr__(self) -> str:
        return f"{self.target}={self._getLetterByPiece()}"

    def _isCorrectPromotionRankByColor(self, color, target):
        if color == 'w':
            return target.rank == 8
        if color == 'b':
            return target.rank == 1
        raise ValueError("Invalid promotion move")
    def _getLetterByPiece(self):
        if self.promoteTo == Knight:
            return 'N'
        if self.promoteTo == Bishop:
            return 'B'
        if self.promoteTo == Rook:
            return 'R'
        if self.promoteTo == Queen:
            return 'Q'
        raise ValueError("Invalid promotion move")