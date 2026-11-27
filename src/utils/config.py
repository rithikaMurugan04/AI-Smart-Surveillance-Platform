"""
Project Configuration

AI Smart Surveillance Platform

Project Maintainer : Rithika
"""

# -----------------------------
# YOLO Model
# -----------------------------

YOLO_MODEL = "yolov8s.pt"

# -----------------------------
# Camera
# -----------------------------

CAMERA_ID = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# -----------------------------
# Crowd Detection
# -----------------------------

ALERT_THRESHOLD = 5

CLUSTER_DISTANCE = 75

CLUSTER_SIZE_THRESHOLD = 3

# -----------------------------
# Fight Detection
# -----------------------------

ATTACK_CONFIRM_FRAMES = 6

PUSH_DISTANCE_THRESHOLD = 120

PUSH_SPEED_THRESHOLD = 45

# -----------------------------
# Alarm
# -----------------------------

ALARM_COOLDOWN = 3

ALARM_SOUND = "voice.mp3"

# -----------------------------
# Heatmap
# -----------------------------

HEATMAP_BLUR = 51

HEATMAP_ALPHA = 0.6

FRAME_ALPHA = 0.4

# -----------------------------
# Display
# -----------------------------

WINDOW_NAME = "AI Smart Surveillance"

WINDOW_WIDTH = 1280

WINDOW_HEIGHT = 720