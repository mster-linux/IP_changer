import time
import os

os.system("clear")
print('''\033[31m  _____ _____         _                                 
 |_   _|  __ \       | |                                
   | | | |__) |   ___| |__   __ _ _ __   __ _  ___ _ __ 
   | | |  ___/   / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|\033[0m''')
print("\033[37m  _| |_| |      | (__| | | | (_| | | | | (_| |  __/ |   \033[0m")
print('''\033[32m |_____|_|       \___|_| |_|\__,_|_| |_|\__, |\___|_|   
       ______                            __/ |          
      |______|                          |___/         
\033[0m''')
time.sleep(1)
print("\033[36m        |-------------------------------------------------|\033[0m")
print("\033[36m        | github  :https://github.com/shirazklay          |\033[0m")
print("\033[36m        |-------------------------------------------------|\033[0m")
print("\033[36m        | inst :https://www.instagram.com/shiraz_ab_klay  |\033[0m")
print("\033[36m        |-------------------------------------------------|\033[0m")
print("\033[37m        | sudo apt-get install tor                        |\033[0m")
print("\033[37m        | sudo apt-get install privoxy                    |\033[0m")
print("\033[37m        | change your sockes to (127.0.0.1:9050)          |\033[0m")
print("\033[36m        |-------------------------------------------------|\033[0m")
print("\033[36m\033[0m")
time.sleep(1)

os.system("service tor start")

a = input("\033[38mtime to change IP in Sec [type=60]---> \033[0m")
h = input("\033[38mhow many time do you want to change your IP [type=1000]---> \033[0m")

os.system("clear")

print('''\033[31m  _____ _____         _                                 
 |_   _|  __ \       | |                                
   | | | |__) |   ___| |__   __ _ _ __   __ _  ___ _ __ 
   | | |  ___/   / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|\033[0m''')
print("\033[37m  _| |_| |      | (__| | | | (_| | | | | (_| |  __/ |   \033[0m")
print('''\033[32m |_____|_|       \___|_| |_|\__,_|_| |_|\__, |\___|_|   
       ______                            __/ |          
      |______|                          |___/         \033[0m''')
print("\033[38m <------------------------------------------------------> \033[0m")

for i in range(h):  
      time.sleep(a)
      os.system("service tor reload")
      print("\033[31m         <----- Your (IP) has been Changed ----->\033[0m") 
