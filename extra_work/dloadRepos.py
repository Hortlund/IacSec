'''
Akond Rahman 
June 27, 2018 
Download repos from Github 
'''
from itertools import izip_longest
import os 
import csv 
import subprocess
import numpy as np

def getRepos(file_name):
    list_ = []
    with open(file_name, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
          the_repo_name = row_[0]
          repo_dload_url = 'https://github.com/' + the_repo_name + '.git'
          list_.append(repo_dload_url)
          #https://github.com/akondrahman/SolidityExploration.git    
    return list_



def makeChunks(the_list, size_):
    for i in range(0, len(the_list), size_):
        yield the_list[i:i+size_]

def cloneRepo(repo_name):
    cmd_ = "git clone " + repo_name
    subprocess.check_output(['bash','-c', cmd_])    

def cloneRepos(repo_list):
    for repo_batch in repo_list:
        str_ = ''
        for repo_ in repo_batch:
            print 'Cloning ', repo_
            cloneRepo(repo_)
            dirName = repo_.split('/')[-1].split('.')[0]
            print dirName

if __name__=='__main__':
   srcFile1='/Users/akond.rahman/Documents/Personal/misc/icse19-work/gh-repo-list-batch1.csv'
   srcFile2='/Users/akond.rahman/Documents/Personal/misc/icse19-work/gh-repo-list-batch2.csv'
   list1=getRepos(srcFile1)    
   list2=getRepos(srcFile2)      
   list_ = list1 + list2 
   list_ = np.unique(list_)
   print 'Repos to download:', len(list_)
   ## need to create chunks as too many repos 
   chunked_list = list(makeChunks(list_, 1000))  ### list of lists, at each batch download 1000 repos 
   #print chunked_list
   cloneRepos(chunked_list)
