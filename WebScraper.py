from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def buscar_youtube_shorts(palavras_chave, limite_por_palavra=10):
    options = Options()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    todos_links = set()

    for palavra in palavras_chave:
        query = palavra.replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={query}&sp=EgIYAQ%253D%253D"

        driver.get(url)
        time.sleep(3)

        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)

        elementos = driver.find_elements(By.XPATH, '//a[contains(@href, "/shorts/")]')

        count = 0
        for e in elementos:
            href = e.get_attribute('href')
            if href and href.startswith("https://www.youtube.com/shorts/") and href not in todos_links:
                todos_links.add(href)
                count += 1
            if count >= limite_por_palavra:
                break

    driver.quit()

    with open("links.txt", "w", encoding="utf-8") as f:
        for link in todos_links:
            f.write(link + "\n")

    return todos_links

if __name__ == "__main__":
    entrada = input("Digite as palavras-chave separadas por espaço: ")
    palavras = entrada.strip().split()
    links_coletados = buscar_youtube_shorts(palavras)
    print(f"{len(links_coletados)} links salvos no arquivo 'links.txt'.")
