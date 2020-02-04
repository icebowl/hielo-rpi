# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import math

def clearAir(mc,x,y,z):
    mc.setBlocks(-100,-63,-100,100,63,100,0)

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def plotShpere(mc,x,y,z,scale):
    l = 0
    clearAir(mc,x,y,z)
    for theta in range (0,360,1):
        h = math.cos((3.141592 / 180) * theta ) * scale
        k = math.sin((3.141592 / 180) * theta ) * scale
        print(x+h,y+k,z+l)
        mc.setBlock(x+h,y+k,z+l,79)
    #print()

def main():
    mc = init()
    x,y,z = mc.player.getPos()
    plotShpere(mc,x,y,z,30)
    #mc.player.setPos(x+10,y,z-10)
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()

'''
AIR                   0
ICE                  79
WOOL                35
'''
