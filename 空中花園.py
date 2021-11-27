# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:28:37 2021

@author: Administrator
"""
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create("anorfire.club")
uuid=mc.getPlayerEntityId("shane7698")
x,y,z=mc.entity.getTilePos(uuid)

for i in range(10):
    mc.setBlock(x,y+i,z+i,1)
    mc.entity.setTilePos(uuid,x,y+1+i,z+i)
mc.setBlocks(x-3,y+10,z+10,x+3,y+10,z+13,2)

blockid=random.choice([37,38])
if blockid==38:
        blocktype=random.randint(0, 9)
        mc.setBlocks(x-3,y+11,z+10,x+3,y+11,z+13,blockid,blocktype)
else:
    mc.setBlocks(x-3,y+11,z+10,x+3,y+11,z+13,blockid)