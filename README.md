# AI Smart Surveillance Platform

A real-time AI surveillance project that analyses video streams to detect people, monitor crowd behaviour, identify potentially abnormal situations, and present results through an interactive dashboard.

This repository is Rithika's copy of a collaborative project. The implementation is based on the team's project repository and is intended for learning, demonstration, and further development.

## Features

- Real-time camera monitoring
- Person detection using YOLO-based computer vision
- Crowd counting and density monitoring
- Basic fight and theft detection modules
- Behaviour analysis
- Alarm triggering
- Heatmap and visual overlays
- Streamlit monitoring dashboard
- Modular Python project structure

## Technology Stack

- Python
- OpenCV
- Ultralytics YOLO
- PyTorch
- Streamlit
- NumPy and Pandas

## Project Structure

```text
AI-Smart-Surveillance-Platform/
├── dashboard/
├── docs/
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
└── README.md
```

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/rithikaMurugan04/AI-Smart-Surveillance-Platform.git
   cd AI-Smart-Surveillance-Platform
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run

Start the processing pipeline:

```bash
python -m src.main
```

Launch the dashboard in a separate terminal:

```bash
streamlit run dashboard/app.py
```

Camera access, model weights, and optional media assets may need to be configured locally before running the application.

## Learning Areas

- Python application development
- Computer vision and video processing
- Object detection
- Modular software design
- Streamlit dashboards
- Logging and debugging
- Git and GitHub collaboration

## Contributor

**Rithika M**  
B.Tech – Artificial Intelligence and Machine Learning  
GitHub: [@rithikaMurugan04](https://github.com/rithikaMurugan04)

## Project Credit

This is a personal repository copy of a collaborative project. The original team repository is available at:
https://github.com/varshini19-s/AI-Smart-Surveillance-Platform
