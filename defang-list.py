import sys

if ((len(sys.argv)) < 1):
    print("Pass the list as argument. For example:\n-> python3 defang-list.py file.txt")
    sys.exit()
else:
    ioc_list = open(sys.argv[1],"r")
    for url in ioc_list:
        defang = url.replace("http", "hxxp")
        defang = defang.replace(".", "[.]")
        defang = defang.rstrip('\n')
        print(defang)
        
