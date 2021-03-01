import os
import subprocess
from tqdm import tqdm
import mmap

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines//2



op_dir="/home/samsepi0l/fdroid_apks/"
apk_list="/home/samsepi0l/fdroid_apks/apk_list_condensed.txt"

file=open(apk_list,'r')
count=0
tot=0
line_num=1
with open(apk_list) as f:
    for line in tqdm(f,total=get_num_lines(apk_list)):
        line=line.strip()
        print("APK:",line,"Line number:",line_num)
        nextline = next(f)
        nextline=nextline.strip()
        
        lis=nextline.split(',')
        if(len(lis)>1):
            tot+=1
            line_num+=2
            continue

        else:
            nextline=nextline.replace(" ","_")
            nextline=nextline.replace("&","and")
            new_dir=os.path.join(op_dir,nextline)
            if os.path.isdir(new_dir):
                
                x=subprocess.check_output("fdroidcl download "+line,shell=True)
                x=x.decode("utf-8")
                l1=x.split("\n")
                subprocess.run("mv "+l1[1][17:]+" "+new_dir,shell=True)
                print("{} APKs downloaded".format(tot))
                

                
            else:
                os.mkdir(new_dir)
                x=subprocess.check_output("fdroidcl download "+line,shell=True)
                x=x.decode("utf-8")
                l1=x.split("\n")
                subprocess.run("mv "+l1[1][17:]+" "+new_dir,shell=True)
                print("{} APKs downloaded".format(tot))
                
            
            tot+=1
        line_num+=2



print("Total number of apks: {}".format(tot))

#subprocess.run("")
