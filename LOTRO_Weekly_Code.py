# Retrieve LOTRO Weekly Coupon Code

import urllib3

urllib3.disable_warnings()
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
http = urllib3.PoolManager(cert_reqs='CERT_NONE')

r = http.request('GET', 'https://forums.lotro.com/index.php?forums/sales-and-promotions.8/index.rss')

def str_between(string, start, end):
    return (string.split(start))[1].split(end)[0]

try:
    result = str_between(str(r.data), 'Coupon Code: ', '<br />')
except:
    print("ERROR: Unable to retrieve Coupon Code.")

print(result)
