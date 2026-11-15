# Computer Vision
## Repository Organisation
### computer_vision
board_detection.py - Contains a ROS2 node that takes an image of a chessboard and identify the inner and outer corners of the chessboard, publishing whether coordinates have been found and their 2D image coordinates

### config
Contains camera configuration for the club webcam if using.

### test
3 images of random chessboards

### train
chess_piece_detection.py - Contains code to load data from roboflow and train a yolov8n model with it


## Setup

1. (Optional) If you are planning on training the YOLO model, copy `.roboflow_key.example` to `.roboflow_key`, get your Roboflow key and write it into the file
2. Get camera calibration and parameter files and put them into `config/cam_params.yaml` and `config/camera_info.yaml`. This can be done in 2 ways:
- Copy over the templates `config/cam_params_template.yaml` and `config/camera_info_template.yaml`. This is done by default in `install.py`.
- Calibrate the camera by yourself (see ticket [5](https://github.com/OxRAMSociety/RobotArmPackages3/issues/5))


## Resources
### YOLO
YOLOv8 Model Specification - https://github.com/ultralytics/ultralytics/blob/main/docs/en/models/yolov8.md

### Roboflow
Roboflow Guide - https://blog.roboflow.com/train-yolov8-obb-model/

### Webcams
Using Android phone as a webcam - https://adityatelange.in/blog/android-phone-webcam-linux/
Physical Webcam model - https://amzn.eu/d/99ZbQrP

