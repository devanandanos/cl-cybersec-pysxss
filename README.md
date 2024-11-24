# cl-cybersec-pysxss
CSRF Vulnerability Scanner

This script scans a given URL for potential Cross-Site Request Forgery (CSRF) vulnerabilities by analyzing the forms on the webpage.

How It Works
1 Fetch the Webpage:
-Uses requests to retrieve the page's HTML content.
-Handles errors such as invalid URLs or network issues.

2 Parse HTML Forms:
-Uses BeautifulSoup to find all <form> elements on the page.

3 Check for CSRF Protection:
-Each form is checked for a hidden field with the name csrf_token (or similar).
-If a form lacks this field, it is flagged as potentially vulnerable.

4 Output Results:
-Displays the action URL of each potentially vulnerable form and its full HTML structure.

Example Usage
-Run the script.
-Enter the target URL when prompted.
-If vulnerabilities are found, the script lists:
-Action URL: Where the form submits data.
-Form HTML: The entire HTML of the vulnerable form.

Notes
-Modify the csrf_token field name if the target site uses a custom name for CSRF tokens.
-Always have permission before scanning websites, as unauthorized scanning may be illegal.
