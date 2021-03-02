import os
import subprocess
from tqdm import tqdm
from multiprocessing import Pool

root_path="/home/samsepi0l/fdroid_apks"


def starting_fn():

    
    categories=list(sorted(os.listdir(root_path)))
    pool=Pool(processes=6)
    pool.map(process_apks,categories)


def process_apks(categ):

    print("Starting the {} category\n".format(categ))
    folder_path=os.path.join(root_path,categ)
    os.chdir(folder_path)
    apks=sorted(os.listdir(folder_path))
    for apk in tqdm(apks,total=len(apks)):
        subprocess.run("apkx "+apk,shell=True)
        
    print("Category {} completed".format(categ))

if __name__=='__main__':
    os.chdir(root_path)
    starting_fn()