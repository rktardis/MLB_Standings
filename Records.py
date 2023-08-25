#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:22:10 2023

@author: richard
"""

import Standings_Funcs as stnd
import pandas as pd
import seaborn as sns

AL_W=["SEA","HOU","TEX","","OAK"]
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
to_500_record=pd.DataFrame({"Game No.":[]})
w_pct_record=pd.DataFrame({"Game No.":[]})
grph=pd.DataFrame({"Game No.":[],"Record":[]})
y=2023
for t in AL_W:
# =============================================================================
#     r=to_500(y,t)
# =============================================================================
    to_500_record=pd.merge(to_500_record,stnd.to_500(y,t),on="Game No.",how="outer")
    w_pct_record=pd.merge(w_pct_record,stnd.w_pct(y,t),on="Game No.",how="outer")
    grph=grph.append(stnd.to_500(y,t).rename(columns={t:"Record"}))
    
sns.lineplot(data=grph)