import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()

class ThreatCollector:
    def __init__(self):
        # In a real app, you'd load API keys here
        self.api_keys = {
            'abuseipdb': None,
            'virustotal': None
        }

    def get_global_stats(self):
        """
        Returns high-level stats for the dashboard.
        """
        # Mocking global threat levels
        return {
            'threat_level': random.choice(['Low', 'Moderate', 'High', 'Critical']),
            'active_attacks': random.randint(50, 500),
            'top_country': fake.country_code(),
            'last_updated': datetime.now().strftime('%H:%M:%S')
        }

    def get_recent_threats(self, count=10):
        """
        Generates a list of mock IOCs (Indicators of Compromise).
        """
        threats = []
        threat_types = ['Malware', 'Phishing', 'Botnet', 'DDoS', 'Ransomware']
        
        for _ in range(count):
            threat = {
                'id': fake.uuid4()[:8],
                'type': random.choice(threat_types),
                'source_ip': fake.ipv4(),
                'target_port': random.choice([80, 443, 22, 3389, 53]),
                'location': fake.country(),
                'confidence': random.randint(60, 99),
                'timestamp': datetime.now().strftime('%H:%M:%S')
            }
            threats.append(threat)
            
        return threats

    def get_chart_data(self):
        """
        Generates mock data for charts.
        """
        # Attacks per hour (last 12 hours)
        labels = [f"{i}:00" for i in range(12)]
        data = [random.randint(10, 100) for _ in range(12)]
        
        # Threat distribution
        distribution = {
            'Malware': random.randint(20, 50),
            'Phishing': random.randint(10, 30),
            'DDoS': random.randint(5, 20),
            'Other': random.randint(5, 15)
        }
        
        return {
            'line_chart': {'labels': labels, 'data': data},
            'doughnut_chart': distribution
        }
