CSRF Vulnerability Scanner  

This script scans a given URL for potential Cross-Site Request Forgery (CSRF) vulnerabilities by inspecting the `<form>` elements present on the webpage.  

---

How It Works  

1. Fetch the Webpage  
   - Uses the `requests` library to retrieve the HTML content of the target page.  
   - Includes error handling to manage scenarios like invalid URLs or network issues.  

2. Parse HTML Forms  
   - Utilizes `BeautifulSoup` to locate all `<form>` elements on the page.  

3. Check for CSRF Protection  
   - Examines each `<form>` for the presence of a hidden input field with a name like `csrf_token` or similar.  
   - Forms without this field are flagged as potentially vulnerable to CSRF attacks.  

4. Output Results  
   - For each potentially vulnerable form, the script displays:  
     - Action URL: The endpoint where the form submits data.  
     - Form HTML: The complete HTML structure of the form.  

---

Example Usage  

1. Run the script.  
2. Provide the target URL when prompted.  
3. If vulnerabilities are detected, the script will output:  
   - Action URL: The submission endpoint of the form.  
   - Form HTML: The complete HTML of the flagged form.  

---

Notes  

- If the target website uses a custom name for CSRF tokens, update the script to check for that specific field name.  
- Always obtain proper authorization before scanning any website, as unauthorized scanning may be illegal and could result in legal consequences.  

---

Disclaimer:  
This scanner is intended for ethical testing and educational purposes only. Use responsibly and ensure you have proper permissions before performing any scans.  
