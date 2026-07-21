from urllib.parse import urlsplit, urljoin
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

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    potential_urls = soup.find_all("a")
    list_urls = []

    for url in potential_urls:
        working_url = url.get("href")
        if working_url:
            list_urls.append(urljoin(base_url, working_url))
    
    return list_urls

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    potential_img = soup.find_all("img")
    list_img = []

    for img in potential_img:
        working_url = img.get("src")
        if working_url:
            list_img.append(urljoin(base_url, working_url))
        
    return list_img

def extract_page_data(html, page_url):
    page_data = {
        "url": page_url,
        "heading": get_heading_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
        "outgoing_links": get_urls_from_html(html, page_url),
        "image_urls": get_images_from_html(html, page_url)
    }

    return page_data
    