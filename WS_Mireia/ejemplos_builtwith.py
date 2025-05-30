import builtwith as bw

urls = ['https://www.gencat.cat', 'https://www.uoc.edu', 'http://microsoft.com']

for url in urls:
    print(f"url: {url} made with: \n\t{bw.builtwith(url)}", end='\n\n')