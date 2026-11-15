# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

from brain.tasks.wait import Wait
from brain.tasks.think import Think
from brain.tasks.move import Move

# TODO: Define the component classes used here/wait/think/move

async def run():
    camera: Camera = None
    piece_squares_calculator: PieceSquaresCalculator = None
    chess_engine: ChessEngine = None
    arm: Arm = None

    wait = new Wait(camera, piece_squares_calculator)
    think = new Think(camera, piece_squares_calculator, chess_engine)
    move = new Move(camera, arm)

    try:
        while True:
            board_state = await wait()

            (board_state, square_to_move_from, square_to_move_to) = await think(board_state)

            await move(board_state, square_to_move_from, square_to_move_to)

    except KeyboardInterrupt:
        print("Shutting down gracefully")
        del wait; del think; del move
        del camera; del piece_squares_calculator; del chess_engine
        print("Shut down gracefully")

run()
