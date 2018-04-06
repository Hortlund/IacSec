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
             apID = int(row[1])
             name = row[0]
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
    id_param = int(id_param)
    path2ret = df_param[df_param['scriptID']==id_param]['path'].tolist()[0]
    return path2ret

def getScriptContent(id_param, df_param):
    id_param = int(id_param)
    content = df_param[df_param['scriptID']==id_param]['content'].tolist()[0]
    return content

def getLabel(dic, inp):
    lab = ''
    inp = int(inp)
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
            scr_lab = getLabel(dict_ap, v_[0])
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
            # if the most frequent is 50% of the list , then agreement
            if freq_perc >= 0.50:
                agrCnt += 1
                lis2ret.append((scr_pat, scr_lab))
            else:
                disAgrCnt += 1
                scr_con = getScriptContent(k_, scr_df)
                lis2ret.append((scr_pat, 'DISAGREED'))

    return lis2ret, agrCnt, disAgrCnt

if __name__=='__main__':
   apa_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/antipattern_table.csv'
   pro_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/profile_table.csv'
   scr_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/script_table.csv'
   sub_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/submission_table.csv'

   curated_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED.csv'

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
   full_list, agrCnt, disAgrCnt = getAgreement(sb_di, sc_df, ap_di)
   print full_list
   print agrCnt
   print disAgrCnt
   curated_df = pd.DataFrame.from_records(full_list, columns=['PATH', 'CATEG'])
   curated_df.to_csv(curated_ds)
