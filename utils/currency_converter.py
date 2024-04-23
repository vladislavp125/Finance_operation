import asyncio

import requests
from bs4 import BeautifulSoup



async def get_currency():
    DOllAR_RUB = "https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&sca_esv=5d0811d5ae0715ef&sca_upv=1&sxsrf=ACQVn08TFVOEDVhRpMpVkOGpjBNdXOwYTw%3A1713891055423&ei=7-YnZoCsGYPZwPAP8_yPsAk&udm=&ved=0ahUKEwjA36rc5diFAxWDLBAIHXP-A5YQ4dUDCBA&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&gs_lp=Egxnd3Mtd2l6LXNlcnAiDNC00L7Qu9C70LDRgDIPEAAYgAQYQxiKBRhGGIICMg0QABiABBixAxhDGIoFMhAQABiABBixAxhDGIMBGIoFMhAQABiABBixAxhDGIMBGIoFMg0QABiABBixAxhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMhsQABiABBhDGIoFGEYYggIYlwUYjAUY3QTYAQFI-BdQog1YgBNwAngBkAEAmAFWoAGwA6oBATa4AQPIAQD4AQGYAgigAuQDwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAhAQABiABBiwAxhDGMkDGIoFwgIOEAAYgAQYsAMYkgMYigXCAgQQIxgnwgIKECMYgAQYJxiKBcICBRAAGIAEwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICBRAuGIAEwgIOEC4YgAQYxwEYjgUYrwGYAwDiAwUSATEgQIgGAZAGCroGBggBEAEYE5IHATigB6s7&sclient=gws-wiz-serp"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

    full_page = requests.get(DOllAR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})

    currency = str(convert[0].text).replace(",", ".")
    return currency

c = (asyncio.run(get_currency()))

