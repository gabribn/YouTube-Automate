import os
from yt_dlp import YoutubeDL

destino = "Vidios"

os.makedirs(destino, exist_ok=True)

try:
    with open("links.txt", "r", encoding="utf-8") as arquivo:
        links = [linha.strip() for linha in arquivo if linha.strip()]
except FileNotFoundError:
    print("Arquivo 'links.txt' não encontrado no diretório atual.")
    exit(1)

opcoes = {
    'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
    'format': 'best',
    'quiet': False
}

with YoutubeDL(opcoes) as ydl:
    for link in links:
        try:
            print(f"\nBaixando: {link}")
            ydl.download([link])
        except Exception as e:
            print(f"Erro ao baixar {link}: {e}")
