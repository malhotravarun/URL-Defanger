import sys

if ((len(sys.argv)) < 1):
    print("Pass the url as argument. For example:\n-> python3 defang.py https://www.cnn.com")
    sys.exit()
else:
    url = sys.argv[1]
    defang = url.replace("http", "hxxp")
    defang = defang.replace(".", "[.]")
    print(defang)
