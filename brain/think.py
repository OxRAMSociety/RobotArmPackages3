# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Oliver Geer

from task_planning.task import Task

class Think(Task[(PieceSquares, PieceName, Square)]):
    """Use a camera, piece squares calculator, and chess engine to input nothing and output
    the piece-to-squares correspondence, the piece to move, and the square to move it to."""

    def on_init(camera: Camera, piece_squares_calculator: PieceSquaresCalculator, chess_engine: ChessEngine) -> None:
        self._camera = camera
        self._piece_squares_calculator = piece_squares_calculator
        self._chess_engine = chess_engine

    def on_call(piece_squares: PieceSquares) -> (PieceSquares, PieceName, Square):
        # TODO
        pass

    def on_del() -> None:
        del self._camera
        del self._piece_squares_calculator
        del self._chess_engine
