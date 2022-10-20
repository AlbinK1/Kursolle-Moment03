#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:10:19 2022

@author: karlsteen
"""

#skatt 
kskatt = 0.2136 #21.36% Komunnalskatt
lskatt = 0.1148 #11.45% landstingsskatt

# bruttolön
lön1 = int(input("Vad är din bruttolön?: "))
# lön2 = 
# lön3 = 
if lön1 < 19247:
    print("dibshit")
    kskatt_avdrag = 0
    lskatt_avdrag = 0
    kvarlön = lön1
else:
    #kskatt avdrag
    kskatt_avdrag = lön1*kskatt
    
    #lskatt avdrag
    lskatt_avdrag = lön1*lskatt
    
    #kvarståendelön
    kvarlön = lön1 - lskatt_avdrag - kskatt_avdrag


print("Månadslön: {}".format(round(lön1)))
print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
print("Lön efter skatt: {}".format(round(kvarlön)))