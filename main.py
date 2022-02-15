import requests, os

def main():
    os.system("cls")
    print(" > Proxy Scraper & Checker \n")
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all"
    open(f"{os.getenv('TEMP')}\\proxies.txt", "wb").write(requests.get(url).content)
    with open("proxies.txt", "w") as file:
        for line in open(f"{os.getenv('TEMP')}\\proxies.txt", "r"):
            proxy = line.strip("\n")
            file.write(f"{proxy} \n")

if __name__ == "__main__":
    main()