class ThreatDetector:
    def __init__(self):
        self.threshold = 3  # Alert after 3 failed attempts
    
    def check_brute_force(self, failed_attempts):
        """Find IPs trying to break in"""
        alerts = []
        for ip, count in failed_attempts.items():
            if count >= self.threshold:
                alerts.append({
                    'type': 'BRUTE_FORCE',
                    'ip': ip,
                    'attempts': count,
                    'severity': 'HIGH'
                })
        return alerts

# Test it
detector = ThreatDetector()
test_data = {'192.168.1.101': 5, '192.168.1.102': 2}
alerts = detector.check_brute_force(test_data)
print("Alerts:", alerts)
