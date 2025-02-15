import re
import string
import tldextract
def clean_text(text):
    """
    Remove special characters, URLs, and convert to lowercase.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    return text.strip()

def extract_links(text):
    """
    Finds all URLs in the text and extracts their domains.
    """
    url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    urls = re.findall(url_pattern, text)
    
    domains = [tldextract.extract(url).domain for url in urls]
    return domains

