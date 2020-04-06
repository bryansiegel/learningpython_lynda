import urllib.request

webUrl = urllib.request.urlopen("https://bryansiegel.com")
print("result code" + str(webUrl.getcode()))

data = webUrl.read()
print(data)
