# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 06:28:48 2021

@author: Administrator
"""
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create("anorfire.club")
uuid=mc.getPlayerEntityId("shane7698")
x,y,z=mc.entity.getTilePos(uuid)

while 1:
    x,y,z=mc.entity.getTilePos(uuid)
    blockid=random.choice([37,38])
    if blockid==38:
        blocktype=random.randint(0, 9)
        mc.setBlocks(x+5,y,z+5,x-5,y,z-5,blockid,blocktype)
    else:
        mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,blockid)