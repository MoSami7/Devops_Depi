import json

def analyze_visits(log_file='users_visits.json'):
    try:
        with open(log_file, 'r') as f:
            data = json.load(f)  # Load log data
        ip_addresses = {entry['ip_address'] for entry in data}  # Extract unique IP addresses
        unique_visits = len(ip_addresses)  # Count unique visits
        print(f'Unique visits: {unique_visits}')
    except FileNotFoundError:
        print('Log file not found.')  # Handle missing log file

if __name__ == "__main__":
    analyze_visits()  # Run analysis when script is executed