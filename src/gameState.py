
from typing import List, Tuple
from src.board import Board
from src.move import Move


class GameState:
    """
    Overall representation of the game state.
    """
    board: Board
    isWhiteTurn = True
    turn: int = 1
    history : List[List[str]] = []

    def __init__(self) -> None:
        self.board = Board()

    def __repr__(self) -> None:
        return str(self.board)+self.getHistory()
    def ply(self, m: Move) -> None:
        if self.isWhiteTurn:
            self.history.append([])
        self.history[self.turn-1].append(str(m))
        self.board.applyMove(m)
        self.isWhiteTurn = not self.isWhiteTurn
        if self.isWhiteTurn:
            self.turn+=1
    def getHistory(self) -> str:
        if len(self.history) == 0:
            return "Game start"
        s = ""
        for i, turn in enumerate(self.history):
            l = len(turn)
            if l == 0:
                break
            if l == 1:
                s+=f"{i+1}: {turn[0]}, ..."
                break
            s+=f"{i+1}: {turn[0]}, {turn[1]} "
        return s
    def start(self) -> None:
        # for each player
        # for p in pieces , get all legal moves
        # eval all moves
        # pick best move
        # apply move
        # switch turns
        # check game end conditions
        # return if game_end else continue
        pass