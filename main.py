import requests, os, threading

def main():
    os.system("cls")
    print(" > Proxy Scraper & Checker \n")
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all"
    open(f"{os.getenv('TEMP')}\\proxies.txt", "wb").write(requests.get(url).content)
    with open("proxies.txt", "w") as file:
        proxies = open(f"{os.getenv('TEMP')}\\proxies.txt", "r")
        for i in range(10): threading.Thread().start()
        for line in proxies:
            proxy = line.strip("\n")
            proxydict = {
                "https": f"socks5://{proxy}"
            }
            try:
                request = requests.get("https://api.ipify.org", proxies=proxydict, timeout=3)
                print(request.text)
                file.write(proxy)
            except Exception:
                pass

if __name__ == "__main__":
    main()