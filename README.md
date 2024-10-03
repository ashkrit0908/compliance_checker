# Compliance Checker API

The Compliance Checker API is a Django-based application that scrapes compliance policy content from Stripe's documentation and checks for non-compliance against a specified target webpage. This tool is designed to help organizations ensure their messaging aligns with compliance standards.

## Features

- Scrapes compliance policy from the Stripe documentation.
- Checks webpage content against compliance terms.
- Returns findings of any non-compliant content.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework
- Requests library
- BeautifulSoup4

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/compliance_checker.git
   cd compliance_checker

## Testing
1. **Bash**

```bash
curl -X POST http://127.0.0.1:8000/api/check_compliance/ \
-H "Content-Type: application/json" \
-d '{"url": "https://mercury.com"}'

