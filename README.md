# 🌍 Live Cyber Threat Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Chart.js](https://img.shields.io/badge/Chart.js-3.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A real-time security operations center (SOC) dashboard that aggregates and visualizes cyber threat intelligence. It simulates the ingestion of IOCs (Indicators of Compromise) from sources like AbuseIPDB and VirusTotal to provide a live view of the global threat landscape.

## 🧐 The Problem

Security analysts are often overwhelmed by raw logs and disconnected data streams. To make rapid decisions, they need a "Single Pane of Glass"—a unified dashboard that visualizes attack volume, threat types, and geographical origins in real-time.

## 💡 The Solution

This dashboard provides a high-level situational awareness view.

It features:
- **Real-Time Telemetry**: Simulates live data ingestion with auto-refreshing UI.
- **Dynamic Visualizations**: Interactive line charts and doughnut graphs using Chart.js.
- **Threat Feed**: A scrolling list of recent attacks with confidence scores and source locations.
- **Demo Mode**: Comes pre-configured with a realistic mock data generator, so you can see it in action immediately without needing API keys.

## 🚀 Features

- **Global Threat Level**: Dynamic status indicator.
- **Attack Volume Tracking**: Line chart showing trends over the last 12 hours.
- **Vector Analysis**: Breakdown of threats by type (Malware, Phishing, DDoS, etc.).
- **Responsive Dark Mode UI**: Designed to look like a professional SOC monitor.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CyberShuriken/threat-dashboard.git
    cd threat-dashboard
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  **Start the Dashboard**:
    ```bash
    python app.py
    ```

2.  **View in Browser**:
    Open `http://localhost:5000`.

    *The dashboard will automatically refresh every 5 seconds with new "live" data.*

## 🧠 Skills Demonstrated

- **Full-Stack Development**: Integrating a Python/Flask backend with a Bootstrap/JS frontend.
- **Data Visualization**: Using Chart.js to render complex datasets into actionable insights.
- **API Simulation**: Designing a modular data collector that mimics real-world threat intelligence feeds.
- **SOC Operations**: Understanding the key metrics (IOCs, Confidence Scores) relevant to security analysts.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
