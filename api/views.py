from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup

# Function to scrape specific sections from the compliance policy page
def scrape_compliance_policy():
    try:
        # Fetch the page content from Stripe's documentation
        url = "https://stripe.com/docs/treasury/marketing-treasury"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the "Terms to Avoid" section
        terms_to_avoid_section = soup.find(id="terms-to-avoid") 
        terms_to_avoid_list = terms_to_avoid_section.find_next('ul').get_text(separator="\n")
        
        # Extract the "Don’t use the following terms" under FDIC insurance eligibility
        fdic_section = soup.find(text="Don’t use the following terms:")
        if fdic_section:
            # Extract the following list of terms
            fdic_table = fdic_section.find_next('ul').get_text(separator="\n")
        else:
            fdic_table = "FDIC section not found."


        # Combine the two parts to form the compliance policy
        policy_content = f"Terms to Avoid:\n{terms_to_avoid_list}\n\nFDIC Terms:\n{fdic_table}"
        return policy_content

    except Exception as e:
        return f"Error: {str(e)}"

# Function to scrape the target webpage content
def scrape_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract only the text content
        page_text = soup.get_text(separator=" ", strip=True)
        return page_text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to check the compliance of the target webpage against the scraped policy
def check_compliance(page_content, policy_content):
    non_compliance = []

    # Split the policy content into individual terms or phrases
    policy_lines = policy_content.splitlines()

    # Check each line from the policy in the target page content
    for line in policy_lines:
        clean_line = line.strip()  
        if clean_line and clean_line.lower() in page_content.lower():
            non_compliance.append(f"Found non-compliant content: '{clean_line}'")

    if non_compliance:
        return non_compliance
    else:
        return ["No non-compliance found."]

# API view to check compliance
@api_view(['POST'])
def check_compliance_api(request):
    url = request.data.get('url')
    if not url:
        return Response({"error": "Please provide a URL"}, status=400)

    # Scrape the compliance policy
    policy_content = scrape_compliance_policy()
    if "Error" in policy_content:
        return Response({"error": "Unable to fetch the policy content"}, status=500)

    # Scrape the target webpage content
    page_content = scrape_webpage(url)
    if "Error" in page_content:
        return Response({"error": "Unable to fetch the webpage content"}, status=500)

    # Check compliance
    findings = check_compliance(page_content, policy_content)

    # Return the findings
    return Response({"findings": findings})
