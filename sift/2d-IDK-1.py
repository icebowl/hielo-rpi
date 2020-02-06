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
    
def output2d(mc,mList,x,y,z):
     for k in range (0,10):
        for l  in range (0,10):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == "1"):
                theBlock = 79
            if (theBlock == "0"):
                theBlock = 0
            mc.setBlock(x,9+y-k,z+l,theBlock)
    #print()

def main():
    mc = init()
    x,y,z = mc.player.getPos()
    CLR = ["0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000"]
           
    D = ["0111111000",
         "0111111100",
         "0110001100",
         "0110001100",
         "0110001100",
         "0110001100",
         "0110001100",
         "0110001100",
         "0111111100",
         "0111111000"]
           
    output2d(mc,D,x,y,z)
    mc.player.setPos(x,y,z-2)
    x = x -20
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()

'''
AIR                   0
ICE                  79
WOOL                35
'''
