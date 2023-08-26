#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:21:15 2023

@author: richard
"""

from pybaseball import schedule_and_record as snr

def to_500 (y,t):
    res=snr(y,t)
    res=res.reset_index()
    res=res[["index","Tm","W-L"]].rename(columns={"index":"Game No.","Tm":"Team","W-L":"WL"})
    res=res.dropna(0,"any")
    res[["W","L"]]=res.WL.str.split("-",expand=True).astype(int)
    res[t]=res["W"]-res["L"]
    res=res[["Game No.",t]]
    return res
#Defines a function that uses the baseball reference api to generate a dataframe for an input teams' number of games above or below .500 after each game in an input season year

def w_pct (y,t):
    res=snr(y,t)
    res=res.reset_index()
    res=res[["index","Tm","W-L"]].rename(columns={"index":"Game No.","Tm":"Team","W-L":"WL"})
    res=res.dropna(0,"any")
    res[["W","L"]]=res.WL.str.split("-",expand=True).astype(int)
    res[t]=res["W"]/res["Game No."]
    res=res[["Game No.",t]]
    return res
#Defines a function that uses the baseball reference api to generate a dataframe for an input teams' winning percentage after each game in an input season year

def grph (y,t):
    res=snr(y,t)
    res=res.reset_index()
    res=res[["index","Tm","W-L"]].rename(columns={"index":"Game No.","Tm":"Team","W-L":"WL"})
    res=res.dropna(0,"any")
    res[["W","L"]]=res.WL.str.split("-",expand=True).astype(int)
    res["Record"]=res["W"]-res["L"]
    res=res[["Game No.","Record","Team"]]
    return res
