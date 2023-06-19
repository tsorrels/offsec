import requests

post_url = 'http://192.168.191.141:81/admin/login.php'
get_url = 'http://192.168.191.141:81/admin/index.php'

data_dict = {'username' : 'root', 'password' : 'root', 'login' : ''}
post_headers_dict = {'Cookie' : 'PHPSESSID=rci94g40jqhj5jnnkv5m75nmvp'}
get_headers_dict = {'Cookie' : 'PHPSESSID=rci94g40jqhj5jnnkv5m75nmvp', 'Referer' : 'http://192.168.191.141:81/admin/index.php', 'Upgrade-Insecure-Requests' : '1', 'Connection' : 'close', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5'}

post_ret = requests.post(post_url, data = data_dict, headers = post_headers_dict, allow_redirects = False)
print(post_ret)


get_ret = requests.post(get_url, headers = get_headers_dict, allow_redirects = False)
print(get_ret)
