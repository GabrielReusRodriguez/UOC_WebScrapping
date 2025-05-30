import whois

urls = ['https://www.uoc.edu', 'https://www.gencat.cat']

for url in urls:
    print(f"whois de la url {url}  es:\n\t {whois.whois(url)}", end= '\n\n')