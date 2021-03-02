import os
import subprocess
from tqdm import tqdm
import mmap
from multiprocessing import Pool

root_path="/home/samsepi0l/fdroid_apks"
op_path="/home/samsepi0l/fdroid_java"

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines




def move_to(categ):
    from_dir=os.path.join(root_path,categ)
    to_dir=os.path.join(op_path,categ)
    os.chdir(from_dir)

    subprocess.run("find . -type f -name '*.java' > list.txt",shell=True)
    with open('list.txt','r') as f:
        for line in tqdm(f,total=get_num_lines('list.txt')):
            line=line.strip()
            #print(line)
            line_lis=line.split("/")
            #print(line_lis)
            to_path=os.path.join(to_dir,line_lis[1])
            if os.path.isdir(to_path):
                subprocess.run("mv "+line+" "+to_path,shell=True)
            else:
                os.mkdir(to_path)
                subprocess.run("mv "+line+" "+to_path,shell=True)



def init_op(op_path,root_path):
    dirs=sorted(os.listdir(root_path))
    for dir in dirs:
        dir_path=os.path.join(op_path,dir)
        if os.path.isdir(dir_path):
            continue
        else:
            os.mkdir(dir_path)

if __name__=='__main__':

    init_op(op_path,root_path)
    categories=list(sorted(os.listdir(root_path)))
    pool=Pool(processes=6)
    pool.map(move_to,categories)
