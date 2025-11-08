# Security Monitor - Main Program
# This brings together all our components

from log_parser import parse_log_line, detect_suspicious
from threat_detector import ThreatDetector
from storage import save_alert


def monitor_logs():
    """Main security monitoring function"""
    
    print("🔒 Security Monitor Started!")
    print("=" * 50)
    print()
    
    # Step 1: Create our threat detector
    detector = ThreatDetector()  # Hire our security guard!
    print("✓ Threat detector ready")
    
    # Step 2: Get some logs to analyze
    # (For now, we'll use fake logs. Later we'll read from real files)
    sample_logs = [
        "192.168.1.100 10:30:00 LOGIN_SUCCESS",
        "192.168.1.101 10:31:00 LOGIN_FAILED",
        "192.168.1.101 10:32:00 LOGIN_FAILED",
        "192.168.1.101 10:33:00 LOGIN_FAILED",
        "192.168.1.102 10:34:00 LOGIN_SUCCESS",
        "192.168.1.101 10:35:00 LOGIN_FAILED",
        "192.168.1.103 10:36:00 LOGIN_FAILED",
        "192.168.1.103 10:37:00 LOGIN_FAILED",
        "192.168.1.103 10:38:00 LOGIN_FAILED",
        "192.168.1.103 10:39:00 LOGIN_FAILED",
    ]
    
    print(f"✓ Loaded {len(sample_logs)} log entries")
    print()
    
    # Step 3: Parse the logs (turn messy text into organized data)
    print("Parsing logs...")
    parsed_logs = [parse_log_line(log) for log in sample_logs]
    print("✓ Logs parsed")
    
    # Step 4: Look for suspicious activity
    print("Detecting suspicious activity...")
    suspicious_ips = detect_suspicious(parsed_logs)
    print(f"✓ Found {len(suspicious_ips)} suspicious IPs")
    print()
    
    # Step 5: Check if any are real threats
    print("Analyzing threats...")
    alerts = detector.check_brute_force(suspicious_ips)
    print(f"⚠️  Generated {len(alerts)} alerts!")
    print()
    
    # Step 6: Save all alerts
    if alerts:
        print("Saving alerts to database...")
        for alert in alerts:
            save_alert(alert)
        print("✓ All alerts saved")
    else:
        print("✓ No threats detected - all clear!")
    
    print()
    print("=" * 50)
    print(f"✅ Monitoring complete. Found {len(alerts)} threats.")


# This is the starting point of the program
if __name__ == "__main__":
    monitor_logs()
