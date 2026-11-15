# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

# TODO: Use chess engine's square class instead: https://python-chess.readthedocs.io/en/v1.11.2/core.html#squares

from chess import Piece
from typing import List

class BoardState:
    """A complete or incomplete list of pieces on the board,
    with at most one per square
    TODO Docstring; what x and y refer to
    """

    _piece_per_square: List[Piece | None] = [None]*64

    def __init__(self):
        pass

    def square_free(self, square: Square) -> bool:
        assert(0 <= x && x < 8 && 0 <= y && y < 8)
        return (_piece_per_square[(y * 8) + x] is None)

    def add_piece(self, x: int, y: int, square: Square):
        """TODO Docstring"""
        assert(0 <= x && x < 8 && 0 <= y && y < 8 && self.square_free(x, y))
        _piece_per_square[(y * 8) + x] = piece

    def get_fen(self)
        """Get the FEN format of the board, for the chess engine.
        See https://python-chess.readthedocs.io/en/v1.11.2/core.html#chess.Board"""
        # TODO
