# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def output2Dhielo(mc,mList,x,y,z,color1,color2);
     for k in range (0,10):
        for l  in range (0,10):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,35,theBlock)
    #print()

def matrixZ(mc,x,y,z):
    I = [[,5,1,1,1,1,1,1,4,4],
        [5,5,7,7,7,7,7,7,4,4],
        [1,1,7,7,7,7,7,7,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,7,7,7,7,5,5,1,1],
        [1,1,7,7,7,7,5,5,1,1],
        [1,1,1,1,1,1,1,1,1,1]]
    print(m)
    for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
    print()

def matrixY(mc,x,y,z):
    m = [[1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,0,1,1,1,0,1,1],
     [1,1,1,0,1,1,1,0,0,1],
     [1,1,1,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,1,1,1,1,1,0,1],
     [1,1,1,1,1,1,1,1,1,1]]
    print(m)
    for h in range (0,10):
        for l  in range (0,10):
            print(m[h][l],end="")
            mc.setBlocks(x+h,y-5, z+l, x+h,y+20,z+l,m[h][l])

    print()
    mc.setBlocks(x-1,y-5, z-1, x+11,y-5,z+11,89)
    mc.setBlocks(x-1,y+10, z-1, x+11,y+10,z+11,89)
    mc.setBlocks(x-1,y+20, z-1, x+11,y+20,z+11,89)


def main():
    mc = init()
    x,y,z = mc.player.getPos()
    CLR = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
           
    I =   [[0,0,0,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,0,1,1,0,0,0,0],
           [0,0,0,1,1,1,1,0,0,0],
           [0,0,0,1,1,1,1,0,0,0]]
    
    D =   [[0,1,1,1,1,1,1,0,0,0],
           [0,1,1,1,1,1,1,0,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,0,0,0,1,1,0,0],
           [0,1,1,1,1,1,1,0,0,0],
           [0,1,1,1,1,1,1,0,0,0]]
           
    O = [[0001111000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000],
         [0000000000]]
         
    matrixZ(mc,x,y,z)
    mc.player.setPos(x,y,z-2)
    x = x -20
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()

'''
AIR                   0
ICE                  79
WOOL                35
"""
