import requests

if __name__ == "__main__":
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    source = requests.get(url)
    source.encoding = "utf-8"
    source = source.text
    
    with open("index.json", "w") as f:
        f.write(source)