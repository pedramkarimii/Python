import re

def extract_domains_from_urls(url_list):
    # Define a regex pattern for extracting domain names
    domain_regex = re.compile(r'https?://(?:www\.)?([a-zA-Z0-9.-]+)')

    # Initialize an empty list to store extracted domains
    extracted_domains = []

    # Iterate through the list of URLs
    for url in url_list:
        # Use regex to find all matches in the URL
        matches = domain_regex.findall(url)

        # If matches are found, add them to the list
        if matches:
            extracted_domains.extend(matches)

    return extracted_domains

# Example usage with the provided URL
example_url = "https://google.com"
result = extract_domains_from_urls([example_url])

# Print the extracted domains
print("Extracted domains:", result)

