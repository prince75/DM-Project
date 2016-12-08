#!/usr/bin/python

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting
import matplotlib
import csv
import os


			#GOal 1 - see the winning probability based on rank difference b/w players of both Grand-slum and Regular tournments
tennis_df = pd.read_csv('Data.csv', encoding = 'latin1') 	    # Reading Data from data.csv to tennis_df DataFrame
tennis_df.WRank = pd.to_numeric(tennis_df.WRank, errors = 'coerce') # WRank - Winner Rank  
tennis_df.LRank = pd.to_numeric(tennis_df.LRank, errors = 'coerce') # LRank - Loser Rank  
tennis_df['Diff'] =  tennis_df.LRank - tennis_df.WRank              # A different column having rank differnce b/w Winner and Loser
# New Feature: Round the rank difference to 10's and 20's
tennis_df['Round_10'] = 10*np.round(np.true_divide(tennis_df.Diff,10))  # round of the ranks and make them multiple of 10
# New Feature: Total number of sets in the match
tennis_df['Total Sets'] = tennis_df.Wsets + tennis_df.Lsets

#preprocessing:  NA values to 0
tennis_df.W3 = tennis_df.W3.fillna(0)
tennis_df.W4 = tennis_df.W4.fillna(0)
tennis_df.W5 = tennis_df.W5.fillna(0)
tennis_df.L3 = tennis_df.L3.fillna(0)
tennis_df.L4 = tennis_df.L4.fillna(0)
tennis_df.L5 = tennis_df.L5.fillna(0)

tennis_df['Sets Diff'] = tennis_df.W1+tennis_df.W2+tennis_df.W3+tennis_df.W4+tennis_df.W5 - (tennis_df.L1+tennis_df.L2+tennis_df.L3+tennis_df.L4+tennis_df.L5)
new_df = tennis_df
df_non_GS = new_df[~(new_df.Series == 'Grand Slam')]
df_GS = new_df[new_df.Series == 'Grand Slam']

plt.figure(figsize = (10,10))
bins = np.arange(10,200,10)
Gs_prob = []
non_Gs_prob = []

for value in bins:
    pos = value
    neg = -value
    
    pos_wins = len(df_GS[df_GS.Round_10 == pos])
    neg_wins = len(df_GS[df_GS.Round_10 == neg])
    Gs_prob.append(np.true_divide(pos_wins,pos_wins + neg_wins))
    
    pos_wins = len(df_non_GS[df_non_GS.Round_10 == pos])
    neg_wins = len(df_non_GS[df_non_GS.Round_10 == neg])
    non_Gs_prob.append(np.true_divide(pos_wins,pos_wins + neg_wins))
    
    
plt.bar(bins,Gs_prob,width = 9, color = 'green') 
plt.bar(bins,non_Gs_prob,width = 8, color = 'blue')
plt.title('Winning probability vs Rank difference', fontsize = 30)
plt.xlabel('Rank Difference',fontsize = 15)
plt.ylabel('Winning Probability',fontsize = 15)
plt.xlim([10,200])
plt.ylim([0.5,0.9])
plt.legend(['Grand Slams', 'Non Grand Slams'], loc = 1, fontsize = 15)
plt.show()

