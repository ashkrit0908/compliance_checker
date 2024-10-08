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
2. **Run Migrations and server**
   ```bash
   python manage.py migrate
   python manage.py runserver

## Testing
1. **Using Bash**

   ```bash
   curl -X POST http://127.0.0.1:8000/api/check_compliance/ \
   -H "Content-Type: application/json" \
   -d '{"url": "https://mercury.com"}'

2. **Using Postman**
- Open Postman and set the request type to POST.
- Enter the URL: http://127.0.0.1:8000/api/check_compliance/.
- In the Headers tab, add:
- Key: Content-Type
- Value: application/json
- In the Body tab, select raw and enter the following JSON

```json
   {
     "url": "https://mercury.com"
   }

