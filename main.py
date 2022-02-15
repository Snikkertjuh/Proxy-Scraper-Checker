import requests, os, threading

os.system("cls")
print(" > Proxy Scraper & Checker \n")
url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all"
open(f"{os.getenv('TEMP')}\\proxies.txt", "wb").write(requests.get(url).content)
file = open("proxies.txt", "w")
proxies = open(f"{os.getenv('TEMP')}\\proxies.txt", "r")
for i in range(50): threading.Thread().start()
for line in proxies:
    proxy = line.strip("\n")
    proxydict = {
        "https": f"socks5://{proxy}"
    }
    try:
        request = requests.get("https://api.ipify.org", proxies=proxydict, timeout=3)
        print(f" > Not working > {request.text}")
        file.write(proxy)
    except Exception:
        print(f" > Not working > {proxy}")
        pass