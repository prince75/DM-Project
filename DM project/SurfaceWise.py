#!/usr/bin/python

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting
import matplotlib
import csv
import os

#Goal - Compare player's performace Surface wise i.e. Hard surface, grass surface and clay surface
winners = np.unique(new_df.Winner)
losers = np.unique(new_df.Loser)
players = np.append(winners,losers)
players_un = np.unique(players)
record = np.zeros(len(players_un)) # General record of the player
GS_record = np.zeros(len(players_un)) # Grand Slam record
Clay_record =  np.zeros(len(players_un)) # Clay Record
Carpet_record = np.zeros(len(players_un)) # Carpet Record
Grass_record = np.zeros(len(players_un)) # Grass Record
Hard_record = np.zeros(len(players_un)) #Hard surface record
fifth_set_record = np.zeros(len(players_un)) # Fifth Set record 
the_final_record = np.zeros(len(players_un)) # Fianls Record

d = {'Player_name': players_un, 'record':record, 'GS_record': GS_record,'Clay_record': Clay_record, 'Carpet_record': Carpet_record,'Grass_record':Grass_record,'Hard_record':Hard_record,'fifth_set_recrod':fifth_set_record,'the_final_record':the_final_record }
players_df = pd.DataFrame(data=d)

# Fill in features values for each feature
for i,row in enumerate(players_df.iterrows()):
    w = len(new_df[new_df.Winner == row[1].Player_name])
    l = len(new_df[new_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_Games'] = w + l
    players_df.loc[i,'record'] = np.true_divide(w,(w+l))

    
    temp_df = new_df[new_df.Series == 'Grand Slam']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_GS_Games'] = w + l
    players_df.loc[i,'GS_record'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df.Surface == 'Clay']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_Clay_Games'] = w + l
    players_df.loc[i,'Clay_record'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df.Surface == 'Carpet']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_Carpet_Games'] = w + l
    players_df.loc[i,'Carpet_record'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df.Surface == 'Grass']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_Grass_Games'] = w + l
    players_df.loc[i,'Grass_record'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df.Surface == 'Hard']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_Hard_Games'] = w + l
    players_df.loc[i,'Hard_record'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df['Total Sets'] == 5]
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_fifth_set_recrod_Games'] = w + l
    players_df.loc[i,'fifth_set_recrod'] = np.true_divide(w,(w+l))
    
    temp_df = new_df[new_df['Round'] == 'The Final']
    w = len(temp_df[temp_df.Winner == row[1].Player_name])
    l = len(temp_df[temp_df.Loser == row[1].Player_name])
    players_df.loc[i,'Total_final_Games'] = w + l
    players_df.loc[i,'the_final_recrod'] = np.true_divide(w,(w+l))

print(players_df.Carpet_record)
#GS Factor represents how well a play performs in Grand Slams compared to regular tournaments
players_df['GS_Factor'] = (players_df.GS_record - players_df.record)/(players_df.GS_record + players_df.record)
# Final factor represents how well a play performs in finals compared to regular matches
players_df['Final_Factor'] = (players_df.the_final_recrod - players_df.record)/(players_df.the_final_recrod + players_df.record)

players_df.record = players_df.record.fillna(0)
players_df.GS_record = players_df.GS_record.fillna(0)
players_df.Clay_record = players_df.Clay_record.fillna(0)
players_df.Carpet_record = players_df.Carpet_record.fillna(0)
players_df.Grass_record = players_df.Grass_record.fillna(0)
players_df.Hard_record = players_df.Hard_record.fillna(0)
players_df.fifth_set_recrod = players_df.fifth_set_recrod.fillna(0)
players_df.the_final_record = players_df.the_final_record.fillna(0)
players_df.GS_Factor = players_df.GS_Factor.fillna(0)
players_df.Final_Factor = players_df.Final_Factor.fillna(0)

players_df.to_csv('players_info.csv')
selected_players = players_df[players_df.Total_Games>850]
selected_players.to_csv('moregameplay.csv')
federer = np.zeros(3)
federer[0] = selected_players.Clay_record[selected_players.Player_name == 'Federer R.']
federer[1] = selected_players.Grass_record[selected_players.Player_name == 'Federer R.']
federer[2] = selected_players.Hard_record[selected_players.Player_name == 'Federer R.']

nadal = np.zeros(3)
nadal[0] = selected_players.Clay_record[selected_players.Player_name == 'Nadal R.']
nadal[1] = selected_players.Grass_record[selected_players.Player_name == 'Nadal R.']
nadal[2] = selected_players.Hard_record[selected_players.Player_name == 'Nadal R.']

djokovich = np.zeros(3)
djokovich[0] = selected_players.Clay_record[selected_players.Player_name == 'Djokovic N.']
djokovich[1] = selected_players.Grass_record[selected_players.Player_name == 'Djokovic N.']
djokovich[2] = selected_players.Hard_record[selected_players.Player_name == 'Djokovic N.']

ferrer = np.zeros(3)
ferrer[0] = selected_players.Clay_record[selected_players.Player_name == 'Ferrer D.']
ferrer[1] = selected_players.Grass_record[selected_players.Player_name == 'Ferrer D.']
ferrer[2] = selected_players.Hard_record[selected_players.Player_name == 'Ferrer D.']

plt.figure(figsize = (10,10))
plt.hold(True)
plt.bar([0,2.5,5],federer, color = 'green' , width = 0.5)
plt.bar([0.5,3,5.5],nadal, color = 'red', width = 0.5)
plt.bar([1,3.5,6],djokovich, color = 'blue', width = 0.5)
plt.bar([1.5,4,6.5],ferrer, color = 'cyan', width = 0.5)
plt.xlim(0,7.5)
plt.xticks([1,3,5], ['Clay','Grass','Hard'], fontsize = 25)
plt.legend(['Federer','Nadal','Djokovic','Ferrer'], fontsize = 15)
plt.ylabel('Winning Probability')
plt.show()

