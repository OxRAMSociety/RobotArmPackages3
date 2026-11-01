from task_planning.wait import Wait
from task_planning.think import Think
from task_planning.move import Move

# TODO: Define the component classes used here/wait/think/move

async def run():
    camera: Camera = None
    piece_squares_calculator: PieceSquaresCalculator = None
    chess_engine: ChessEngine = None
    arm: Arm = None

    wait = new Wait(camera, piece_squares_calculator)
    think = new Think(camera, piece_squares_calculator, chess_engine)
    move = new Move(camera, arm)

    while True:
        piece_squares = await wait()
        (piece_squares, piece_to_move, square_to_move_to) = await think(piece_squares)
        await move(piece_squares, piece_to_move, square_to_move_to)

run()
