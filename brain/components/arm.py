# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Oliver Geer

from brain.component import Component

class Arm(Component):
    """The brain-side code of the arm itself.
    Note that the code to run on the Arduino motor
    controller is outside this brain package."""

    def on_init():
        print("Creating arm")
        # TODO

    def on_del():
        print("Deleting arm")
        # TODO
