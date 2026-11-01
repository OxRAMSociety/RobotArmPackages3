from task_planning.task import Task

class Wait(Task[PieceSquares]):
    """Use a camera and piece squares calculator to input nothing, wait until a piece is
    moved by the human, and output the piece-to-squares correspondence."""

    def on_init(camera: Camera, piece_squares_calculator: PieceSquaresCalculator) -> None:
        self._camera = camera
        self._piece_squares_calculator = piece_squares_calculator

    def on_call() -> PieceSquares:
        # TODO
        pass

    def on_del() -> None:
        del self._camera
        del self._piece_squares_calculator
        del self._chess_engine
