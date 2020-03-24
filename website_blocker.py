import time
from datetime import datetime as dt


hosts_temp = 'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list=['www.facebook.com','facebook.com','google.com','www.google.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('Horas laborales')
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website  in content:
                    pass
                else:
                    file.write(redirect+' '+ website+'\n')    
    else:
         with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            #file.write('Final')        
            file.truncate()      
            print('horas libres')  
    time.sleep(5) 