# ExtractDomainNames.py
# Author: Norman Strassner
# Date: 7/14/2025
# Version: 1.0
#
# Imports, via pipe or text file, a list of email addresses like:
#  Investment Inspirations <inspo@inspirationalinvestment.com>
#  Costco Member <CostcoMember@bahrainjc.com>
# and returns a list of only the domain names as:
#  inspirationalinvestment
#  bahrainjc
#

import sys
import re
from urllib.parse import urlparse

def extract_root_domain(email):
    match = re.search(r'@([\w.-]+)', email)
    if not match:
        return None
    domain = match.group(1)
    # Split by '.' and return the second-level domain
    parts = domain.split('.')
    if len(parts) >= 2:
        return parts[-2]
    return domain

def process_lines(lines):
    domains = set()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        root_domain = extract_root_domain(line)
        if root_domain:
            domains.add(root_domain)
    for domain in sorted(domains):
        print(domain)

def main():
    if not sys.stdin.isatty():
        # Input is piped
        lines = sys.stdin.readlines()
        process_lines(lines)
    elif len(sys.argv) == 2:
        # Input file provided as an argument
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                process_lines(lines)
        except FileNotFoundError:
            print(f"File not found: {filename}", file=sys.stderr)
    else:
        print("Usage:")
        print("    cat file.txt | python extract_domains.py")
        print("    python extract_domains.py file.txt")

if __name__ == '__main__':
    main()

