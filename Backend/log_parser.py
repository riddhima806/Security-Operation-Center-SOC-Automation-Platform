# Security Log Parser - Version 1
# This program reads security logs and finds suspicious activity

def parse_log_line(line):
    """
    Takes one log line and breaks it into parts
    Example: "192.168.1.100 10:30:00 LOGIN_FAILED"
    """
    parts = line.split()
    return {
        'ip': parts[0] if len(parts) > 0 else 'unknown',
        'timestamp': parts[1] if len(parts) > 1 else 'unknown',
        'action': parts[2] if len(parts) > 2 else 'unknown'
    }

def detect_suspicious(logs):
    """
    Counts failed login attempts per IP address
    This helps us find potential hackers trying to break in
    """
    failed_attempts = {}
    
    for log in logs:
        if 'FAILED' in log['action']:
            ip = log['ip']
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    
    return failed_attempts

# Test with fake security logs
print("🔒 Security Monitor - Testing Log Parser\n")

fake_logs = [
    "192.168.1.100 10:30:00 LOGIN_SUCCESS",
    "192.168.1.101 10:31:00 LOGIN_FAILED",
    "192.168.1.101 10:32:00 LOGIN_FAILED",
    "192.168.1.101 10:33:00 LOGIN_FAILED",
    "192.168.1.102 10:34:00 LOGIN_SUCCESS",
    "192.168.1.101 10:35:00 LOGIN_FAILED",
]

print("Analyzing logs...")
parsed = [parse_log_line(log) for log in fake_logs]
suspicious = detect_suspicious(parsed)

print("\n SUSPICIOUS ACTIVITY DETECTED:")
for ip, count in suspicious.items():
    print(f"   IP {ip}: {count} failed login attempts")
