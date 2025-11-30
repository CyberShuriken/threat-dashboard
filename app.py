from flask import Flask, render_template, jsonify
from collector import ThreatCollector

app = Flask(__name__)
collector = ThreatCollector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    stats = collector.get_global_stats()
    return jsonify(stats)

@app.route('/api/feed')
def get_feed():
    threats = collector.get_recent_threats(10)
    return jsonify(threats)

@app.route('/api/charts')
def get_charts():
    data = collector.get_chart_data()
    return jsonify(data)

if __name__ == '__main__':
    print("Starting Threat Dashboard...")
    app.run(debug=True, port=5000)
