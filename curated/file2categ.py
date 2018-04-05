'''
Akond Rahman
April 05, 2018
Thursday
This script maps each file to catgeory
'''
import pandas as pd
import csv
import numpy as np

def getAPDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             apID = row[0]
             name = row[1]
             if apID not in dict_:
                 dict_[apID] = name
    return dict_

def getProDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             studentID = row[0]
             sweExp = row[1]
             iacExp = row[2]
             time   = row[3]
             if studentID not in dict_:
                 dict_[studentID] = ( sweExp, iacExp, time)
    return dict_

def getSubmDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             scriptID = row[0]
             apID = row[1]
             if scriptID not in dict_:
                 dict_[scriptID] = [apID]
             else:
                 dict_[scriptID] = [apID] + dict_[scriptID]
    return dict_

def getScriptPath(id_param, df_param):
    path2ret = ''
    path2ret = df_param[df_param['scriptID']==id_param]['path'].tolist()[0]
    return path2ret

def getLabel(dic, inp):
    lab = ''
    if inp in dic:
        lab = dic[inp]
    return lab

def getAgreement(dict_pa, scr_df, dict_ap):
    agrCnt, disAgrCnt  = 0, 0
    lis2ret = []
    for k_, v_ in dict_pa.iteritems():
        scr_pat = getScriptPath(k_, scr_df)
        if (len(v_)==1):
            agrCnt += 1
            scr_lab = getLabel(dict_ap, v_)
            lis2ret.append((scr_pat, scr_lab))
        elif (len(np.unique(v_))==1):
            agrCnt += 1
            scr_lab = getLabel(dict_ap, np.unique(v_)[0])
            lis2ret.append((scr_pat, scr_lab))
        else:
            scr_lab = getLabel(dict_ap , str(np.bincount(v_).argmax()))
            scr_lab_occ = scr_lab.count(scr_lab)
            tot_len = len(v_)
            freq_perc  = float(scr_lab_occ)/float(tot_len)
            # if the most frequent is 75% of the list , then agreement
            if freq_perc >= 0.75:
                agrCnt += 1
                lis2ret.append((scr_pat, scr_lab))
            else:
                disAgrCnt += 1


if __name__=='__main__':
   apa_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/antipattern_table.csv'
   pro_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/profile_table.csv'
   scr_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/script_table.csv'
   sub_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/submission_table.csv'

   '''
   get anti patterns
   '''
   ap_di = getAPDict(apa_tbl)
   # print ap_di
   '''
   get profile
   '''
   pr_di = getProDict(pro_tbl)
   # print pr_di
   '''
   get script table
   '''
   sc_df = pd.read_csv(scr_tbl)
   # print sc_df.head()
   '''
   get submissions
   '''
   sb_di = getSubmDict(sub_tbl)
   # print sb_di
   getAgreement(sb_di, sc_df, ap_di)
