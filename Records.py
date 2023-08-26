#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:22:10 2023

@author: richard
"""

import Standings_Funcs as stnd
import pandas as pd
import seaborn as sns
from datetime import date

AL_W=["TEX","HOU","OAK","LAA","SEA"]
NL_W=["SF","ARI","LAD","SD","COL"]
AL_E=["NYY","BAL","TB","BOS","TOR"]
NL_E=["NYM","PHI","ATL","MIA","WN"]
AL_C=["MIN","CHW","CLE","DET","KC"]
NL_C=["STL","MIL","CHC","CIN","PIT"]
AL=[AL_W,AL_C,AL_E]
NL=[NL_W,NL_C,NL_E]
MLB=AL+NL

all_div=[AL_W,NL_W,AL_C,NL_C,AL_E,NL_E,NL,AL,MLB]
#Builds lists of teams in each division, league, and one of all baseball

#%%
to_500_record=pd.DataFrame({"Game No.":[]})
w_pct_record=pd.DataFrame({"Game No.":[]})
graph=pd.DataFrame({"Game No.":[],"Record":[]})
y=2023
# =============================================================================
# for t in MLB:
# # =============================================================================
# #     r=to_500(y,t)
# # =============================================================================
#     to_500_record=pd.merge(to_500_record,stnd.to_500(y,t),on="Game No.",how="outer")
#     w_pct_record=pd.merge(w_pct_record,stnd.w_pct(y,t),on="Game No.",how="outer")
#     graph=graph.append(stnd.grph(y,t))
# =============================================================================

# =============================================================================
# for d in AL:
#     for t in ["HOU","TEX","TB","TOR","BAL","BOS","SEA"]:
#         graph=graph.append(stnd.grph(y,t))
#         
#     graph=graph.reset_index().drop(columns="index")    
#     sns.set_theme(rc={'figure.dpi': 600}) 
#     sns.lineplot(data=graph,x="Game No.",y="Record",hue="Team").set(title="MLB Records")
#     graph=pd.DataFrame({"Game No.":[],"Record":[]})
# =============================================================================

    
# =============================================================================
# sns.lineplot(data=graph,x="Game No.",y="Record")
# =============================================================================
#%%

def div_graph(y,d):
    graph=pd.DataFrame({"Game No.":[],"Record":[]})
    for t in d:
        graph=graph.append(stnd.grph(y,t))
        
    graph=graph.reset_index().drop(columns="index")    
    sns.set_theme(rc={'figure.dpi': 600}) 
    ttl="MLB Records ("+str(y)+")"
    fig=sns.lineplot(data=graph,x="Game No.",y="Record",hue="Team").set(title=ttl)
    nme=d+"_graph_"+str(date.today())
    fig.saveplot(nme)
    graph=pd.DataFrame({"Game No.":[],"Record":[]})
    
div_graph(y,AL_W)
