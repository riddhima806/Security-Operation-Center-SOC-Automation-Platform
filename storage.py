import json
from datetime import datetime

def save_alert(alert):
    """Save security alerts to a file"""
    alert['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('alerts.json', 'a') as f:
        f.write(json.dumps(alert) + '\n')
    
    print(f"⚠️ ALERT SAVED: {alert['type']} from {alert['ip']}")

def read_all_alerts():
    """Read all saved alerts"""
    try:
        with open('alerts.json', 'r') as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []
    




















    # Test storage
if __name__ == "__main__":
    print("🗄️  Testing Storage System\n")
    
    # Create a fake alert
    test_alert = {
        'type': 'BRUTE_FORCE',
        'ip': '192.168.1.101',
        'attempts': 5,
        'severity': 'HIGH'
    }
    
    print("Saving alert...")
    save_alert(test_alert)
    
    print("\nReading all alerts:")
    all_alerts = read_all_alerts()
    
    for i, alert in enumerate(all_alerts, 1):
        print(f"\nAlert #{i}:")
        print(f"  Time: {alert['timestamp']}")
        print(f"  Type: {alert['type']}")
        print(f"  IP: {alert['ip']}")
        print(f"  Attempts: {alert['attempts']}")