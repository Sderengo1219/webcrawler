from urllib.parse import urlsplit

def normalize_url(url):
    url_parts = urlsplit(url)

    if url_parts.netloc:
        normal_url = url_parts.netloc + url_parts.path
    else:
        normal_url = url_parts.path

    normal_url = normal_url.rstrip("/")

    return normal_url