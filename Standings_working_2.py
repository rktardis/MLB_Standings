#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:33:22 2023

@author: richard
"""

from pybaseball import schedule_and_record as snr
import pandas as pd
from datetime import date
import seaborn as sns

AL_W=["SEA","HOU","TEX","ANA","OAK"]
NL_W=["SF","ARI","LAD","SD","COL"]
AL_E=["NYY","BOS","TB","TOR","BAL"]
NL_E=["NYM","PHI","ATL","MIA","WAS"]
AL_C=["MIN","CHW","CLE","DET","KC"]
NL_C=["STL","MIL","CHC","CIN","PIT"]
AL=AL_W+AL_C+AL_E
NL=NL_W+NL_C+NL_E
MLB=AL+NL
all_div=[AL_W,NL_W,AL_C,NL_C,AL_E,NL_E,NL,AL,MLB]
#Builds lists of teams in each division, league, and one of all baseball

#%%
def to_500 (y,t):
    res=snr(y,t)
    res=res.reset_index()
    res=res[["index","Tm","W-L"]].rename(columns={"index":"Game No.","Tm":"Team","W-L":"WL"})
    res[["W","L"]]=res.WL.str.split("-",expand=True).astype(int)
    res[t]=res["W"]-res["L"]
    res=res[["Game No.",t]]
    return res
#Defines a function that uses the baseball reference api to generate a dataframe for an input teams' number of games above or below .500 after each game in an input season year

def w_pct (y,t):
    res=snr(y,t)
    res=res.reset_index()
    res=res[["index","Tm","W-L"]].rename(columns={"index":"Game No.","Tm":"Team","W-L":"WL"})
    res[["W","L"]]=res.WL.str.split("-",expand=True).astype(int)
    res[t]=res["W"]/res["Game No."]
    res=res[["Game No.",t]]
    return res
#Defines a function that uses the baseball reference api to generate a dataframe for an input teams' winning percentage after each game in an input season year

#%%

to_500_record=pd.DataFrame({"Game No.":[]})
w_pct_record=pd.DataFrame({"Game No.":[]})
grph_record=pd.DataFrame({"Game No":[],"Team":[],"To .500":[]})
y=2001
for t in AL_W:
# =============================================================================
#     r=to_500(y,t)
# =============================================================================
    to_500_record=pd.merge(to_500_record,to_500(y,t),on="Game No.",how="outer")
    w_pct_record=pd.merge(w_pct_record,w_pct(y,t),on="Game No.",how="outer")
    grph_record=to_500_record
    grph_record["Team"]=t
    grph_record=grph_record.rename(columns={t:"To .500"})
    

to_500_record.to_csv("AL_West_Standings"+str(date.today())+".csv",index=False)
sns.lineplot(data=w_pct_record,x=w_pct_record["Game No."],y=w_pct_record[AL_W])


test=to_500(2001,"SEA")
test_2=w_pct(2001,"SEA")