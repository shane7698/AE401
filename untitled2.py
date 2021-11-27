# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:14:50 2021

@author: Administrator
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create("anorfire.club")
uuid=mc.getPlayerEntityId("shane7698")
x,y,z=mc.entity.getTilePos(uuid)

while 1:
    x,y,z=mc.entity.getTilePos(uuid)
    block=mc.getBlock(x,y-1,z+3)
    if block==9 or block==8 or block==0:
        mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,79)