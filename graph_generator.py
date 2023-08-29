#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:03:29 2023

@author: rktardis
"""
#%% Imports & Lists
import Standings_Funcs as sf
import pandas as pd
AL_W=["TEX","HOU","OAK","LAA","SEA"]
NL_W=["SF","ARI","LAD","SD","COL"]
AL_E=["NYY","BAL","TB","BOS","TOR"]
NL_E=["NYM","PHI","ATL","MIA","WN"]
AL_C=["MIN","CHW","CLE","DET","KC"]
NL_C=["STL","MIL","CHC","CIN","PIT"]
AL=[AL_W,AL_C,AL_E]
NL=[NL_W,NL_C,NL_E]
MLB=AL+NL
#Builds lists of teams in each division, league, and one of all baseball
#%% Inputs
Division=AL_W
Year=2023
#%% Output
graph=pd.DataFrame({"Game No.":[],"Record":[]})
fig=sf.div_graph(Year,Division)
