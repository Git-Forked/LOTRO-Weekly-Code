# LOTRO Weekly Coupon Code

import urllib3

urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
http = urllib3.PoolManager()
r = http.request('GET', 'https://forums.lotro.com/forums/external.php?type=RSS2&forumids=819')

def str_between(string, start, end):
    return (string.split(start))[1].split(end)[0]

result = str_between(str(r.data), 'Coupon Code: ', '<br />')

print(result)
