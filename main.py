import sys
from crawl import (
    normalize_url, 
    get_heading_from_html, 
    get_first_paragraph_from_html,
    get_urls_from_html,
    get_images_from_html,
    extract_page_data,
    get_html
)

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    print(f"starting crawl of: {sys.argv[1]}")
    print(get_html(sys.argv[1]))

if __name__ == "__main__":
    main()
