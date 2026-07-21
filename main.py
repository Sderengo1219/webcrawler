from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html


test_soup = '''
<html>
  <body>
    <h1>Welcome to Boot.dev</h1>
    <main>
      <p>Learn to code by building real projects.</p>
      <p>This is the second paragraph.</p>
    </main>
  </body>
</html>'''

def main():
    print("Hello from webcrawler!")
    print(get_heading_from_html(test_soup))



if __name__ == "__main__":
    main()
