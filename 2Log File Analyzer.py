'''2.Log File Analyzer:
    Create a script that analyzes web server logs (e.g., Apache, Nginx) for
common patterns such as the number of 404 errors, the most requested
pages, or IP addresses with the most requests. The script should output a
summarized report.'''

import re
from collections import defaultdict

# Define the log file path
log_file_path = 'path_to_your_log_file.log'

# Patterns to match
pattern_404 = re.compile(r'404')
pattern_request = re.compile(r'"GET (.*?) HTTP')
pattern_ip = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

# Initialize counters
num_404_errors = 0
requested_pages = defaultdict(int)
ip_requests = defaultdict(int)

# Read and analyze the log file
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        # Count 404 errors
        if pattern_404.search(line):
            num_404_errors += 1
        
        # Count requested pages
        match_request = pattern_request.search(line)
        if match_request:
            requested_pages[match_request.group(1)] += 1
        
        # Count IP addresses
        match_ip = pattern_ip.search(line)
        if match_ip:
            ip_requests[match_ip.group(1)] += 1

# Summarize the report
most_requested_pages = sorted(requested_pages.items(), key=lambda item: item[1], reverse=True)
most_requests_ips = sorted(ip_requests.items(), key=lambda item: item[1], reverse=True)

# Print the summary
print("Summary Report:")
print(f"Number of 404 errors: {num_404_errors}")
print("Most Requested Pages:")
for page, count in most_requested_pages[:10]:
    print(f"{page}: {count} requests")
print("IP Addresses with the Most Requests:")
for ip, count in most_requests_ips[:10]:
    print(f"{ip}: {count} requests")