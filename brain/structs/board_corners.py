# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

class BoardCorners:
    """The very corners of the chess board,
    named by the square they are adjacent to.
    The exact square names don't matter,
    but a1 and h8 must be black, and a8 and
    h1 must be white."""

    def __init__(self, a1_corner: (int, int, int), a8_corner: (int, int, int), h1_corner: (int, int, int), h8_corner: (int, int, int)):
        self._a1_corner = a1_corner
        self._a8_corner = a8_corner
        self._h1_corner = h1_corner
        self._h8_corner = h8_corner

    def get_a1_corner():
        return self._a1_corner
    def get_a8_corner():
        return self._a8_corner
    def get_h1_corner():
        return self._h1_corner
    def get_h8_corner():
        return self._h8_corner
