from typing import List, Literal
class Square:
    def __init__(self, rank, file, occupied=False) -> None:
        self.rank = rank
        self.file = file
        self.isOccupied=occupied
    rank: int
    file: Literal['a'] | Literal['b'] | Literal['c'] | Literal['d'] | Literal['e'] | Literal['f'] | Literal['g'] | Literal['h']
    isOccupied: bool
    def __repr__(self) -> str:
        return f"{self.file}{self.rank}"
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Square):
            return False
        return self.rank == value.rank and self.file == value.file
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
def otherColor(color: str) -> str:
    if color == 'b':
        return 'w'
    if color == 'w':
        return 'b'
    raise ValueError("Invalid color")

class Piece:
    """
    Base class for a chess piece
    """
    color: Literal['w'] | Literal['b']
    location: Square
    possibleMoves: List[Square] = []
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Piece):
            return False
        return self.color==value.color and self.location == value.location
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

class Pawn(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=2, file=file)
        else:
            self.location = Square(rank=7, file=file)
        self.color = color
    
    def __str__(self) -> str:
        return "♙" if self.color=='w' else "♟"

class Knight(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=1, file=file)
        else:
            self.location = Square(rank=8, file=file)
        self.color = color
    def __str__(self) -> str:
        return "♘" if self.color=='w' else "♞"

class Bishop(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=1, file=file)
        else:
            self.location = Square(rank=8, file=file)
        self.color = color
    def __str__(self) -> str:
        return "♗" if self.color=='w' else "♝"

class Rook(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=1, file=file)
        else:
            self.location = Square(rank=8, file=file)
        self.color = color
    def __str__(self) -> str:
        return "♖" if self.color=='w' else "♜"

class Queen(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=1, file=file)
        else:
            self.location = Square(rank=8, file=file)
        self.color = color
    def __str__(self) -> str:
        return "♕" if self.color=='w' else "♛"

class King(Piece):
    def __init__(self, color, file) -> None:
        if color == 'w':
            self.location = Square(rank=1, file=file)
        else:
            self.location = Square(rank=8, file=file)
        self.color = color
    def __str__(self) -> str:
        return "♔" if self.color=='w' else "♚"

def majorByFile(color, file) -> Piece:
    if file == 'a' or file == 'h':
        return Rook(color, file)
    if file == 'b' or file == 'g':
        return Knight(color, file)
    if file == 'c' or file == 'f':
        return Bishop(color, file)
    if file == 'd':
        return Queen(color, file)
    if file == 'e':
        return King(color, file)
    raise ValueError("Invalid file")
