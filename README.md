ExtractDomainNames.py
Author: Norman Strassner
Date: 7/14/2025
Version: 1.0

Imports, via pipe or text file, a list of email addresses like:
 Investment Inspirations <inspo@inspirationalinvestment.com>
 Costco Member <CostcoMember@bahrainjc.com>
and returns a list of only the domain names as:
 inspirationalinvestment
 bahrainjc

I wanted to take a list of email address, which may include other text, and get back a list of domain names.
The reason is that I create a list of SPAM email addresses that I want to create rules for, run the list through this script, and get a list of only the domain names so I can cut and paste them easily into MSOutlook's email filters.

