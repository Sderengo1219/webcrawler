from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url):
    url_parts = urlsplit(url)

    if url_parts.netloc:
        normal_url = url_parts.netloc + url_parts.path
    else:
        normal_url = url_parts.path

    normal_url = normal_url.rstrip("/")

    return normal_url

def get_heading_from_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    
    header = soup.find("h1")
    if not header:
        header = soup.find("h2")
    
    if header:
        return header.get_text()
    return ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    main_tag = soup.find("main")

    if main_tag:
        paragraph = main_tag.find("p")
        if not paragraph:
            paragraph = soup.find("p")
    else:
        paragraph = soup.find("p")

    if paragraph:
        return paragraph.get_text()
    
    return ""