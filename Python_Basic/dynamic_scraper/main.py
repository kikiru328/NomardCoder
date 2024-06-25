from playwright.sync_api import sync_playwright

url = "https://google.com"

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()  # headless mode
page.goto(url)

page.screenshot(path="./a.png")

content = page.content()
p.stop()
