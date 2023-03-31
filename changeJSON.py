import json
import os
import datetime
import pytz
import shutil

timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
timeformat = f"{timeformat.strftime('%Y-%m-%d')}"
#IMG Archiving
try:
    path_dir = "./archive/"
    file_list = os.listdir(path_dir)
    print(file_list)
    if timeformat in file_list:
        arc = path_dir+ timeformat  #아카이브되는 디렉토리 주소
        cnt = len(os.listdir(arc))
        if  cnt == 0:
            shutil.copy2("./build/images/1.png", arc + "/1.png")
        else:
            shutil.copy2("./build/images/1.png", arc + "/"+ str(cnt+1) +".png")
    else:
        os.mkdir(path_dir + timeformat)
        shutil.copy2("./build/images/1.png", path_dir + timeformat + "/1.png")    
except:
    print("Failed")
#METADATA Archiving
with open("./build/json/1.json", "r") as json_file:
    json_data = json.load(json_file)
    json_data.pop('edition')
    json_data.pop('compiler')
with open("./build/json/1.json", 'w') as outfile:
    json.dump(json_data, outfile, indent=4)
try:
    path_dir = "./metadata/"
    file_list = os.listdir(path_dir)
    print(file_list)
    if timeformat in file_list:
        arc = path_dir+ timeformat  #아카이브되는 디렉토리 주소
        cnt = len(os.listdir(arc))
        if  cnt == 0:
            shutil.copy2("./build/json/1.json", arc + "/1.json")
        else:
            shutil.copy2("./build/json/1.json", arc + "/"+ str(cnt+1) +".json")
    else:
        os.mkdir(path_dir + timeformat)
        shutil.copy2("./build/json/1.json", path_dir + timeformat + "/1.json")    
except:
    print("Failed")
    
#reference
#https://abluesnake.tistory.com/107
