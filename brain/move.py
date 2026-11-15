# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Oliver Geer

from task_planning.task import Task

class Move(Task[(PieceSquares, PieceName, Square)]):
    """Use a camera and arm to input the piece squares, the piece to move, and the square to
    move to, wait until the moving is done, and output nothing."""

    def on_init(camera: Camera, arm: Arm) -> None:
        self._camera = camera
        self._arm = piece_squares_calculator

    def on_call(piece_squares: PieceSquares, piece_to_move: PieceName, square_to_move_to: Square) -> None:
        # TODO
        pass

    def on_del() -> None:
        del self._camera
        del self._arm
