import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import time
from datetime import datetime

import cv2
import streamlit as st

from src.pipeline.video_pipeline import VideoPipeline


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="AI Smart Surveillance",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 AI Smart Surveillance Platform")
st.caption("Real-time Crowd, Fight, Theft and Anomaly Monitoring")


# -----------------------------------------------------
# Session State Initialization
# -----------------------------------------------------

if "pipeline" not in st.session_state:
    st.write("Loading Video Pipeline...")

    st.session_state.pipeline = VideoPipeline()

    st.write("Video Pipeline Loaded Successfully")

if "running" not in st.session_state:
    st.session_state.running = False

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "alerts" not in st.session_state:
    st.session_state.alerts = []

if "total_alerts" not in st.session_state:
    st.session_state.total_alerts = 0

if "fps" not in st.session_state:
    st.session_state.fps = 0

if "last_frame_time" not in st.session_state:
    st.session_state.last_frame_time = time.time()


# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

with st.sidebar:

    st.header("🎮 Control Panel")

    if st.button("▶ Start Surveillance"):
        st.session_state.running = True

    if st.button("⏹ Stop Surveillance"):
        st.session_state.running = False

    st.markdown("---")

    if st.session_state.running:
        st.success("🟢 Surveillance Running")
    else:
        st.info("🔵 Surveillance Stopped")


# -----------------------------------------------------
# Dashboard Metrics
# -----------------------------------------------------

col1, col2, col3, col4, col5, col6 = st.columns(6)

people_metric = col1.empty()
status_metric = col2.empty()
alarm_metric = col3.empty()
alerts_metric = col4.empty()
fps_metric = col5.empty()
camera_metric = col6.empty()

st.markdown("---")

camera_placeholder = st.empty()

st.markdown("---")

st.subheader("📋 Recent Alerts")

alerts_placeholder = st.container()


# -----------------------------------------------------
# Live Surveillance
# -----------------------------------------------------

if st.session_state.running:

    result = st.session_state.pipeline.process_frame()

    if result is not None:

        st.session_state.last_result = result

        # ----------------------------------
        # FPS Calculation
        # ----------------------------------

        current_time = time.time()

        elapsed = current_time - st.session_state.last_frame_time

        if elapsed > 0:
            st.session_state.fps = int(1 / elapsed)

        st.session_state.last_frame_time = current_time

        # ----------------------------------
        # Dashboard Metrics
        # ----------------------------------

        people_metric.metric(
            "👥 People",
            result["people_count"]
        )

        status_metric.metric(
            "📌 Status",
            result["behavior"]
        )

        alarm_metric.metric(
            "🚨 Alarm",
            "ON" if result["alarm"] else "OFF"
        )

        if result["behavior"] != "NORMAL":

            st.session_state.total_alerts += 1

            timestamp = datetime.now().strftime("%H:%M:%S")

            alert_message = (
                f"{timestamp} | {result['behavior']}"
            )

            if (
                not st.session_state.alerts
                or st.session_state.alerts[0] != alert_message
            ):
                st.session_state.alerts.insert(
                    0,
                    alert_message
                )

            st.session_state.alerts = (
                st.session_state.alerts[:10]
            )

        alerts_metric.metric(
            "📋 Alerts",
            st.session_state.total_alerts
        )

        fps_metric.metric(
            "⚡ FPS",
            st.session_state.fps
        )

        camera_metric.metric(
            "📷 Camera",
            "ONLINE"
        )

        frame_rgb = cv2.cvtColor(
            result["frame"],
            cv2.COLOR_BGR2RGB
        )

        camera_placeholder.image(
            frame_rgb,
            channels="RGB",
            use_container_width=True
        )

        st.caption(
            f"Last Updated: {datetime.now().strftime('%H:%M:%S')}"
        )

    with alerts_placeholder:

        if not st.session_state.alerts:

            st.success("No alerts detected.")

        else:

            for alert in st.session_state.alerts:

                st.warning(alert)

    time.sleep(0.05)

    st.rerun()


# -----------------------------------------------------
# Dashboard When Stopped
# -----------------------------------------------------

else:

    if st.session_state.last_result is not None:

        result = st.session_state.last_result

        people_metric.metric(
            "👥 People",
            result["people_count"]
        )

        status_metric.metric(
            "📌 Status",
            result["behavior"]
        )

        alarm_metric.metric(
            "🚨 Alarm",
            "ON" if result["alarm"] else "OFF"
        )

    else:

        people_metric.metric(
            "👥 People",
            0
        )

        status_metric.metric(
            "📌 Status",
            "NORMAL"
        )

        alarm_metric.metric(
            "🚨 Alarm",
            "OFF"
        )

    alerts_metric.metric(
        "📋 Alerts",
        st.session_state.total_alerts
    )

    fps_metric.metric(
        "⚡ FPS",
        0
    )

    camera_metric.metric(
        "📷 Camera",
        "OFFLINE"
    )

    camera_placeholder.info(
        "Press 'Start Surveillance' to begin monitoring."
    )

    st.caption(
        f"Last Updated: {datetime.now().strftime('%H:%M:%S')}"
    )

    with alerts_placeholder:

        if not st.session_state.alerts:

            st.info("No alerts yet.")

        else:

            for alert in st.session_state.alerts:

                st.warning(alert)