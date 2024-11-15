# Retrieve LOTRO Weekly Coupon Code

import urllib3
import pyclip

urllib3.disable_warnings()
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
http = urllib3.PoolManager(cert_reqs='CERT_NONE')

r = http.request('GET', 'https://forums.lotro.com/index.php?forums/sales-and-promotions.8/&last_days=7&order=post_date&direction=desc')

def str_between(string, start, end, occurrence):
    return (string.split(start))[occurrence].split(end)[0]

i = 1
url = ''
coupon_code = ''

try:
    while True:
        url = str_between(str(r.data), 'data-preview-url="', '">', i)
        if "sales" not in url:
            i+=1
        else:
            break
except:
    print("ERROR: Unable to retrieve URL.")

r = http.request('GET', 'https://forums.lotro.com' + url)

try:
    coupon_code = str_between(str(r.data), 'Coupon Code: ', '<br />', 1)
except:
    print("ERROR: Unable to retrieve coupon code.")

# Print to terminal and copy to clipboard for easy pasting
print(coupon_code)
pyclip.copy(coupon_code)
