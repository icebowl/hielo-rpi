# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import math
pi = math.pi
sin = math.sin
cos = math.cos

def init():
    #ip = "192.168.7.84"
    ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def truckAir(mc,x,y,z):
    mc.setBlocks(x-10,y,z+1,x+10,y+20,z+30,0)

def clearAir(mc,x,y,z):
    mc.setBlocks(x-10,y-5,z-20,x+10,y+20,z+20,0)
    mc.setBlocks(-128,-3,-128,128,64,128,0)
    for k in range (-10,0,1):
        m = 2
        if k < -5:
            m = 7
        if k > -3 and k < -1 :
            m = 3
        mc.setBlocks(-128,k,-128,127,k,127,m)
    mc.postToChat("World Cleared!!!!")

def tunnels(mc):
  #  x to -x
  h = 128; k = 0; l = 0
  ha = 7; ka = 7; za = 7
  mc.setBlocks(h+ha,k+ka ,l+za,-1*h-ha,k-ka,l-za,42)
  # clear air
  h = 128; k = 0; l = 0
  ha = 7; ka = 7; za = 7
  mc.setBlocks(h+ha,k+ka-1 ,l+za-1,-1*h-ha,k-ka+1,l-za+1,0)
  #  z to -z
  h = 0; k = 0; l = 128
  ha = 7; ka = 7; za = 7
  mc.setBlocks(h+ha,k+ka,l+za,h-ha,k-ka,-1 * l-za,42)
  # clear air
  mc.setBlocks(h+ha-1,k+ka-1,l+za,h-ha+1,k-ka+1,-1 *l-za,0)
  mc.setBlocks(5,5,10,-5,-5,-10,0)
  mc.setBlocks(10,5,5,-10,-5,-5,0)
  mc.setBlocks(3,10,3,-3,-5,-3,0)
  
  
def output2dspace(mc,mList,x,y,z):
     for k in range (0,10):
        for l  in range (0,10):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == " "):
                theBlock = 7
            if (theBlock == "1"):
                theBlock = 3
            mc.setBlock(x,9+y-k,z+l,35,theBlock)


def tire(mc,x,y,z):
  X = [" 1 ",
       "121",
       " 1 "]
      #"0123"
  for k in range (0,3):
    for l  in range (0,3):
      #print(X[k][l],end="")
      theBlock = X[k][l]
      if (theBlock == " "):
        m = -1
      if (theBlock == "1"):
        m = 0
      if (theBlock == "2"):
        m = 1
      if m == -1:
        mc.setBlocks(x-1,y+k,z+l,x,y+k,z+l,0)
      else:
        mc.setBlocks(x-1,y+k,z+l,x,y+k,z+l,35,m)
    #print()
    
    
def truck(mc,x,y,z):
  
  X = ["       11111111    ",
       "       11     1    ",
       "       11     111  ",
       "1111111111111111112",
       "1111111111111111112",
       "1   111   1111   12"]
      #"0123456789ABCDEF012"
 

  for k in range (0,6):
    for l  in range (0,19):
      print(X[k][l],end="")
      theBlock = X[k][l]
      m = 0
      if (theBlock == "1"):
        m = 13
      if (theBlock == "2"):
        m = 5
      if m == 0:
        mc.setBlocks(x-3,y-k,z+l,x+3,y-k,z+l,0)
      else:
        mc.setBlocks(x-3,y-k,z+l,x+3,y-k,z+l,35,m)
    print()
    
def colors(mc,x,y,z):
  done = 0
  while(done < 32):
    mc.setBlock(x,y+10,z+done,35,done)
    done = done + 1
    
def axels(mc,x,y,z):
  mc.setBlocks(x-5,y+1,z+8,x+4,y+1,z+8,57)
  mc.setBlocks(x-5,y+1,z+8+5,x+4,y+1,z+8+5,57)
  mc.setBlocks(x-5,y+1,z+8+5+7,x+4,y+1,z+8+5+7,57)
def main():
  mc = init()
  x,y,z = mc.player.getPos()
  clearAir(mc,x,y,z)
  tunnels(mc)
  truckAir(mc,x,y,z)
  colors(mc,x,y,z)
  truck(mc,x,y+7,z+5)
  tire(mc,x+-3,y,z+7)
  tire(mc,x-3,y,z+12)
  tire(mc,x-3,y,z+19)
  tire(mc,x+3,y,z+7)
  tire(mc,x+3,y,z+12)
  tire(mc,x+3,y,z+19)
  axels(mc,x,y,z)
  mc.player.setPos(x-9,y,z+10)

if __name__ == "__main__":
    main()

'''
WOOL
0 = white
1 = orange
2 = magenta 
3 = sky blue
4 = yellow
5 = green
6 = pink
7 =  grey
8 = light grey
9 = cyan
10 = pruple
11 = darker blue
12 = brown
13 = green
14 = red
15 = black
#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
'''



