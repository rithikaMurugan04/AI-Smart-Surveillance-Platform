# Code Inventory

## Purpose

This document provides an overview of all the important files and folders in the project. It helps us understand the current codebase before we start refactoring it into a production-ready AI application.

At this stage, no files have been moved or modified. This document serves as a reference during development.

# Existing Files

## button.py

This file is the main entry point of the application. It provides a graphical interface that allows the user to launch different AI detection modules such as fight detection, theft detection, and live monitoring.



## demo.py

This file performs real-time video processing using the AI models. It acts as one of the core detection scripts of the current project.


## final fight.py

This file is responsible for detecting fight-related activities using computer vision techniques.


## Thief.py

This module detects suspicious theft-related activities.



## YOLO Model Files

These files contain the trained YOLO models used for object detection.

Files:

- yolov8n.pt
- yolov8s.pt
- yolov8m.pt


## voice.mp3

Audio file used for generating alert sounds whenever suspicious activity is detected.


## videos/

Contains sample videos used for testing the detection system.


## mobilenet/

Contains MobileNet-related files used by the existing implementation.


# New Project Structure

The following folders were created as part of the project restructuring process.

## app/

Will contain the main application entry point.


## src/

Will contain all AI and Computer Vision source code.



## api/

Will contain the FastAPI backend.



## dashboard/

Will contain the Streamlit web application.


## database/

Will contain database configuration and models.


## configs/

Will store project configuration files.



## assets/

Will contain images, icons, sounds, and UI resources.


## models/

Will store AI model files.


## outputs/

Will store processed videos and generated outputs.


## logs/

Will contain application log files.


## tests/

Will contain unit tests and integration tests.


# Current Project Status

The project is currently functional but follows a script-based structure.

The next phase of development will focus on reorganizing the project into a modular and production-ready architecture without changing its existing functionality.

This document will be updated throughout the development process as new modules are created and old components are refactored.