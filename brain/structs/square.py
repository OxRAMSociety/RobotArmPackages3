# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

# TODO: Use chess engine's square class instead: https://python-chess.readthedocs.io/en/v1.11.2/core.html#squares

class Square:
    """A square on the board, represented by x from 0 through 7 and y from 0 through 7."""

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __repr__(self):
        return ("abcdefgh"[x])+("12345678"[y])
