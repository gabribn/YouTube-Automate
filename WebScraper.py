from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def buscar_youtube_shorts(palavra_chave, limite=10):
    options = Options()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    query = palavra_chave.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}&sp=EgIYAQ%253D%253D"  

    driver.get(url)
    time.sleep(3)

    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)

    elementos = driver.find_elements(By.XPATH, '//a[contains(@href, "/shorts/")]')

    links = set()
    for e in elementos:
        href = e.get_attribute('href')
        if href and href.startswith("https://www.youtube.com/shorts/"):
            links.add(href)
        if len(links) >= limite:
            break

    driver.quit()

    with open("links.txt", "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")

    return links

if __name__ == "__main__":
    palavra = input("Digite a palavra-chave: ")
    links_coletados = buscar_youtube_shorts(palavra)
    print(f"{len(links_coletados)} links salvos no arquivo 'links.txt'.")
