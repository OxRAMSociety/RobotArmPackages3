# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

from brain.component import Component

class ChessEngine(Component):
    """The code to interface with the chess-playing engine and decide next
    moves based on the board state."""

    def on_init():
        print("Creating chess engine")
        # TODO

    def on_del():
        print("Deleting chess engine")
        # TODO
