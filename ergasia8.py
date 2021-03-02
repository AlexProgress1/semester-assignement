import urllib.request
import json

def get_keys(lex):

    line = []
    for key in lex.keys():

        line.append(key)
    return line

def price(symbolism, symbols_comp="EUR"):

    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbolism.upper(), ','.join(symbols_comp).upper())
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html)
    return data


file = input("Enter file location: ")
fil1 = open(file,'r')
fil1 = fil1.read()
fil1 = json.loads(fil1)
k = get_keys(fil1)
tmp = {}
for i in k:
    tmp1 = price(i)
    tmp[i] = tmp1["EUR"]*fil1[i]

print('Your cryptocurrency is: ')
print(fil1)
print('Which corresponds to : ')
print(tmp)
