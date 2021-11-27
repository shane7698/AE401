from mcpi.minecraft import Minecraft
mc=Minecraft.create("anorfire.club",4711)
mc.setBlocks(24,50,302,30,46,310,1)#蓋實心
mc.setBlocks(25,49,303,29,47,309,0)#掏空
mc.setBlock(24,47,306,0)#門