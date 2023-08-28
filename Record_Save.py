#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:48:33 2023

@author: rktardis
"""

from pybaseball import schedule_and_record as snr
from datetime import date

AL_W=["SEA","HOU","TEX","LAA","OAK"]
NL_W=["SF","ARI","LAD","SD","COL"]
AL_E=["NYY","BOS","TB","TOR","BAL"]
NL_E=["NYM","PHI","ATL","MIA","WSN"]
AL_C=["MIN","CHW","CLE","DET","KC"]
NL_C=["STL","MIL","CHC","CIN","PIT"]
AL=AL_W+AL_C+AL_E
NL=NL_W+NL_C+NL_E
MLB=AL+NL

for t in MLB:
    res=snr(2023,t)
    filename=f"{t}"+"_"+str(date.today())+".csv"
    res.to_csv(filename)