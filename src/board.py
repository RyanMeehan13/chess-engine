from typing import Dict, List, Tuple
from src.move import AbstractMove, CastleMove, Move, PromotionMove
from src.piece import Bishop, King, Knight, Pawn, Piece, Queen, Rook, Square, majorByFile, otherColor
RANKS = [1,2,3,4,5,6,7,8]
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
FILE_TO_INDEX_MAP = {f:i for i,f in enumerate(FILES)}
def getDefaultBoard() -> List[List[Piece|None]]:
        return [
        [ majorByFile('b', f) for f in FILES], 
        [Pawn(color='b', file=f) for f in FILES],
        [None for i in range(8) ],
        [None for i in range(8) ],
        [None for i in range(8) ],
        [None for i in range(8) ],
        [Pawn(color='w', file=f) for f in FILES],
        [majorByFile('w', f) for f in FILES]
    ]

def getIndexBySquare(s: Square) -> Tuple[int]:
     r = s.rank
     f = s.file
     return 8-r, FILE_TO_INDEX_MAP[f]

class Board:
    """
    A representation of the state of a chess board.
    """
    state: List[List[Piece|None]]
    pawns: Dict[str, List[Pawn]] = {'b': [], 'w': []}
    knights: Dict[str, List[Knight]] = {'b': [], 'w': []}
    bishops: Dict[str, List[Bishop]] = {'b': [], 'w': []}
    rooks: Dict[str, List[Rook]] = {'b': [], 'w': []}
    queens: Dict[str, List[Queen]] = {'b': [], 'w': []}
    kings: Dict[str, List[King]] = {'b': [], 'w': []}

    def __init__(self, state=getDefaultBoard()) -> None:
        self.state = state
        self._init_piece_lists()

    def getPieceAt(self, square: Square) -> Piece:
        r,c = getIndexBySquare(square)
        return self.state[r][c]
    
    def removePiece(self, p: Piece) -> None:
        color = p.color
        if isinstance(p, Pawn):
            self.pawns[color].remove(p)
        elif isinstance(p, Bishop):
            self.bishops[color].remove(p)
        elif isinstance(p, Knight):
            self.knights[color].remove(p)
        elif isinstance(p, Rook):
            self.rooks[color].remove(p)
        elif isinstance(p, Queen):
            self.queens[color].remove(p)
        else:
            raise ValueError("Removing invalid or null piece")



    def applyMove(self, move: Move | CastleMove | PromotionMove) -> None:
        if isinstance(move, Move):
            self._handleStandardMove(move)
        elif isinstance(move, CastleMove):
            self._handleCastleMove(move)
        elif isinstance(move, PromotionMove):
            self._handlePromotionMove(move)
        else:
            raise ValueError("Invalid move type passed to apply move")

    def _handleStandardMove(self, move: Move) -> None:
        cur_r, cur_c = getIndexBySquare(move.piece.location)
        new_r, new_c = getIndexBySquare(move.target)
        # check if enemy piece is at target (cant be our piece since would not be generated) 
        if isinstance(self.state[new_r][new_c], Piece) and self.state[new_r][new_c].color == otherColor(move.piece.color):
            # remove enemy piece from board 
            self.removePiece(self.state[new_r][new_c])
        elif isinstance(self.state[new_r][new_c], Piece) and self.state[new_r][new_c].color == move.piece.color:
            raise RuntimeError(f"Cannot capture friendly piece. ({self.state[new_r][new_c].color} capturing { move.piece.color})")
        self.state[cur_r][cur_c] = None
        self.state[new_r][new_c] = move.piece
        move.piece.location = move.target

    def _handleCastleMove(move: CastleMove) -> None:
        # TODO
        pass

    def _handlePromotionMove(move: PromotionMove) -> None:
        # TODO
        pass

    def __repr__(self) -> str:
        s = ""
        for row in self.state:
            for item in row:
                if item is not None:
                    s+=str(item)
                else:
                    s+="·"
                s+=" "
            s+="\n"
        return s
    
    def _init_piece_lists(self) -> None:
        self.__init_pawns()
        self.__init_knights()
        self.__init_bishops()
        self.__init_rooks()
        self.__init_queens()
        self.__init_kings()

    def __init_pawns(self) -> None:
        for b_pawn in self.state[1]:
            self.pawns['b'].append(b_pawn)
        for w_pawn in self.state[6]:
            self.pawns['w'].append(w_pawn)
        
    def __init_knights(self) -> None:
        for b_big_piece in self.state[0]:
            if isinstance(b_big_piece, Knight):
                self.knights['b'].append(b_big_piece)
        for w_big_piece in self.state[7]:
            if isinstance(w_big_piece, Knight):
                self.knights['w'].append(w_big_piece)
    def __init_bishops(self) -> None:
        for b_big_piece in self.state[0]:
            if isinstance(b_big_piece, Bishop):
                self.bishops['b'].append(b_big_piece)
        for w_big_piece in self.state[7]:
            if isinstance(w_big_piece, Bishop):
                self.bishops['w'].append(w_big_piece)
    def __init_rooks(self) -> None:
        for b_big_piece in self.state[0]:
            if isinstance(b_big_piece, Rook):
                self.rooks['b'].append(b_big_piece)
        for w_big_piece in self.state[7]:
            if isinstance(w_big_piece, Rook):
                self.rooks['w'].append(w_big_piece)
    def __init_queens(self) -> None:
        for b_big_piece in self.state[0]:
            if isinstance(b_big_piece, Queen):
                self.queens['b'].append(b_big_piece)
        for w_big_piece in self.state[7]:
            if isinstance(w_big_piece, Queen):
                self.queens['w'].append(w_big_piece)
    def __init_kings(self) -> None:
        for b_big_piece in self.state[0]:
            if isinstance(b_big_piece, King):
                self.kings['b'].append(b_big_piece)
        for w_big_piece in self.state[7]:
            if isinstance(w_big_piece, King):
                self.kings['w'].append(w_big_piece)