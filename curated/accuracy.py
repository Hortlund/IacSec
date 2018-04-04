'''
April 03, 2018
Tuesday
Akond Rahman
Script to detect accuracy of SLIC
'''

from sklearn.metrics import precision_score, recall_score
import numpy as np, pandas as pd
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def printAccu(file_name):
  df2read = pd.read_csv(file_name)
  actualLabels = df2read['ACTUAL'].tolist()
  predictedLabels = df2read['TOOL'].tolist()
  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
                                             next index after first  -> next lower index -> 1 -> 'high'
  '''
  target_labels =  ['N', 'Y']
  '''
  getting the confusion matrix
  '''
  print "Confusion matrix start"
  #print conf_matr_output
  conf_matr_output = pd.crosstab(actualLabels, predictedLabels, rownames=['True'], colnames=['Predicted'], margins=True)
  print conf_matr_output
  print "Confusion matrix end"
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
  the precision score is computed as follows:
  '''
  prec_ = precision_score(actualLabels, predictedLabels, average='binary')
  #print "The precision score is:", prec_
  #print">"*25
  '''
  the recall score is computed as follows:
  '''
  recall_ = recall_score(actualLabels, predictedLabels, average='binary')
  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions
  ideally 1.0, higher the better
  '''
  #accuracy_score_output = accuracy_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  print "Accuracy output  is ", accuracy_score_output
  print">"*10


if __name__=='__main__':
   curated_ds = 'cd /Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/Test.csv'
   printAccu(curated_ds)
