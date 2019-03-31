
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:26:14 2018
main.py
@author: Max McDevitt
"""
# Released under the GNU General Public License

from woods import woods
from town import town
from cave import runcave
from castle import castle
import gameset as gs
#from unknown import unknown

def navigate(cname, level, reputation, age, cl):
    locs = {'town':town, 'woods':woods
            ,'cave':runcave ,'castle':castle}
#       'camelot':camelot, 'Unknown':unknown}
    p = input("\nDo you want to travel? ")
    if p == 'yes' or p == 'y':
        print("Where do you want to travel to?")
        for k in locs.keys():
            print(k.title())
        dest = input('\n: ')
        if dest in locs.keys():
            return locs[dest](cname, level, reputation, age)
            gs.save(level, age, cname, reputation, cl)
        else:
            raise SystemExit