#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:10:19 2022

@author: karlsteen
"""

#skatt 
kskatt = 0.2136 #21.36% Komunnalskatt
lskatt = 0.1148 #11.45% landstingsskatt
sskatt = 0.20 #20% Statligskatt
värnskatt = 0.05 #5% värnskatt

# bruttolön
lön1 = int(input("Vad är din bruttolön?: "))
# lön2 = 
# lön3 = 
if lön1 < 19247:
    kskatt_avdrag = 0
    lskatt_avdrag = 0
    kvarlön = lön1
    print("Månadslön: {}".format(round(lön1)))
    print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
    print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
    print("Lön efter skatt: {}".format(round(kvarlön)))
else:
    #kskatt avdrag
    kskatt_avdrag = lön1*kskatt
    
    #lskatt avdrag
    lskatt_avdrag = lön1*lskatt
    
    #kvarståendelön
    kvarlön = lön1 - lskatt_avdrag - kskatt_avdragsa
    if lön1 > 468700:
        statlig = lön1*sskatt
        slön = kvarlön
        
        print("Månadslön: {}".format(round(lön1)))
        print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
        print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
        print("Statligskatt: {}".format(round(sskatt)))
        print("Lön efter skatt: {}".format(round(slön)))
    else:
        print("Månadslön: {}".format(round(lön1)))
        print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
        print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
        print("Lön efter skatt: {}".format(round(slön)))
        if lön1 > 675700:
            print("Månadslön: {}".format(round(lön1)))
            print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
            print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
            print("Statligskatt: {}".format(round(sskatt)))
            print("Lön efter skatt: {}".format(round(slön)))
        else:
            print("Månadslön: {}".format(round(lön1)))
            print("Kommunalskatt: {}".format(round(kskatt_avdrag)))
            print("lanstingsskatt: {}".format(round(lskatt_avdrag)))
            print("Lön efter skatt: {}".format(round(slön)))
            
