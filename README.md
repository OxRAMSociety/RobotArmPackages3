# RobotArmPackages3

This is the third iteration of code for OxRAM's Robotic Arm project. This iteration uses native
Python concurrency libraries and not a framework like ROS2.

## Setup

1. First, create the virtual environment: `python -m venv .venv`
2. Then, activate it:
  * For Windows, use `.venv\Scripts\activate`
  * For Linux, use `source .venv/bin/activate`
3. Then install the necessary packages.
* For Windows, use 
  ```sh
  python.exe -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
* For Linux, use
  ```sh
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

