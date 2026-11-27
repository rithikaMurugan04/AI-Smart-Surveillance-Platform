# AI Smart Surveillance Platform

A real-time AI surveillance system that monitors live video from a webcam to detect people, analyse crowd behaviour, identify potential abnormal situations, and display the results through an interactive dashboard.

The project was developed to understand the complete workflow of a computer vision application, from capturing live video to running AI-based detection and presenting the results in a user-friendly interface.


# Project Overview

Traditional CCTV systems require continuous human monitoring, which becomes difficult in crowded public places. This project demonstrates how artificial intelligence can assist surveillance by automatically analysing video frames and highlighting suspicious situations.

The application processes each video frame in real time using YOLOv8 for person detection. Based on the detected people, the system analyses crowd density, identifies possible fight situations using simple overlap logic, generates movement heatmaps, triggers alarms for abnormal behaviour, and displays all information on a Streamlit dashboard.

The project follows a modular architecture so that every component can be improved independently in future versions.


# Features

- Real-time webcam monitoring
- Person detection using YOLOv8
- Live crowd counting
- Crowd density detection
- Basic fight-alert heuristic based on overlapping person boxes (not a trained fight classifier)
- Theft-detection placeholder (not implemented in this version)
- Behaviour status analysis
- Automatic alarm triggering
- Heatmap generation
- Live Streamlit dashboard
- Modular and scalable project structure


# System Workflow

```
Camera
   │
   ▼
Camera Manager
   │
   ▼
YOLOv8 Person Detection
   │
   ▼
Behaviour Analysis
   │
   ├── Crowd Detection
   ├── Fight Detection
   └── Theft Detection
           │
           ▼
Alarm Manager
           │
           ▼
Heatmap & Overlay
           │
           ▼
Streamlit Dashboard
```


# Project Structure

```
AI-Smart-Surveillance-Platform/
├── app/
│   └── main_old.py
├── backup_old/
│   ├── legacy Python examples
│   └── mobilenet/
├── dashboard/
│   └── app.py
├── docs/
│   └── project documentation
├── src/
│   ├── alerts/
│   ├── analytics/
│   ├── camera/
│   ├── detection/
│   ├── pipeline/
│   ├── tracking/
│   ├── utils/
│   └── visualization/
├── requirements.txt
├── voice.mp3
├── README.md
└── .gitignore
```


# Technologies Used

### Programming Language

- Python

### Computer Vision

- OpenCV

### Deep Learning

- YOLOv8
- PyTorch

### Dashboard

- Streamlit

### Data Processing

- NumPy
- Pandas

### Other Libraries

- Playsound


# Installation

### Clone the repository

```bash
git clone https://github.com/rithikaMurugan04/AI-Smart-Surveillance-Platform.git
```

### Navigate to the project

```bash
cd AI-Smart-Surveillance-Platform
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows

```bash
.venv\Scripts\activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

# Running the Application

Use **one option at a time** because both options access the same webcam.

### Option 1: Desktop video window

```bash
python -m src.main
```

Press `q` in the video window to stop.

### Option 2: Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

Open the local URL printed by Streamlit, then select **Start Surveillance** in the sidebar.

# Dashboard

The dashboard displays

- Live camera feed
- Number of people detected
- Current system status
- Alarm status
- Camera status
- Frames per second (FPS)
- Total alerts generated
- Recent alert history


# Sample Output

You can add screenshots after running the application.

Example:

```
docs/dashboard.png
docs/live_detection.png
```


# Skills Demonstrated

This project helped me gain practical experience in:

- Python programming
- Object-Oriented Programming
- Modular software architecture
- Real-time video processing
- Computer vision using OpenCV
- Deep learning with YOLOv8
- Building dashboards using Streamlit
- Logging and debugging
- Git and GitHub project management


# Current Limitations

- The theft detector currently returns `False` for every frame; theft detection is not implemented yet.
- Fight alerts are based only on bounding-box overlap, so close positioning can cause false alerts.
- The YOLOv8 weights file (`yolov8s.pt`) is downloaded by Ultralytics on first use if it is not already available.
- A working webcam and permission to access it are required for live monitoring.

# Future Improvements

The current version focuses on building a complete end-to-end surveillance application.

Possible future enhancements include:

- Person tracking using DeepSORT or ByteTrack
- AI-based fight detection models
- Intelligent theft detection using object tracking
- Database integration for alert history
- Email and SMS notifications
- Multi-camera monitoring
- Docker deployment
- Cloud deployment
- User authentication


# Learning Outcomes

While developing this project, I learned how to:

- Design a modular AI application
- Process live video streams
- Integrate YOLOv8 into a Python project
- Build reusable detection modules
- Create a real-time monitoring dashboard
- Connect multiple components into a complete end-to-end application
- Structure an AI project for maintainability and scalability


# Project Maintainer

**Rithika**

This is a collaborative team project; the repository is maintained here for Rithika's portfolio.

B.Tech – Artificial Intelligence and Machine Learning

GitHub: https://github.com/rithikaMurugan04

If you found this project helpful, feel free to ⭐ the repository.