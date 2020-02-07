
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import math

def clearAir(mc):
    mc.setBlocks(-127,-63,-127,128,64,128,0)
    for k in range (-64,0):
        m = 2
        if k < -20:
            m = 7
        if k > -3 and k < -1 :
            m = 3
        mc.setBlocks(-127,-63,-127,127,-62,127,m)
    
    
    mc.postToChat("World Cleared!!!!")
    

def init():
    ip = "192.168.7.226"
    mc = Minecraft.create(ip, 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def plotTube(mc,x,y,z,scale,length):
    ladj =  int(scale / 2)
    for l in range (-length, length):
        for theta in range (0,360,1):
            h = math.cos((3.141592 / 180) * theta ) * scale
            k = math.sin((3.141592 / 180) * theta ) * scale
            print(x+h,y+k,z+l)
            mc.setBlock(x+h,y+k,z+l,20)
            mc.postToChat(length)
        #print()

def plotSphere(mc,x,y,z,radius,m):
	mc.postToChat("Hallo, here's your sphere")
	m = 20 # glass
	for h in range(radius*-1,radius):
		for k in range(radius*-1, radius):
			for l in range(radius*-1,radius):
				if h**2 + k**2 + l**2 < radius**2:
					mc.setBlock(x + h,y + k,z +l,m)


def main():
	mc = init()
	x,y,z = mc.player.getPos()
	clearAir(mc)
	mc.player.setPos(0,0,0)
	plotTube(mc,x,y,z,7,32)
	m = 20
	plotSphere(mc,x,y,z,7,m)
	m = 0
	plotSphere(mc,x,y,z,7,m)
	mc.player.setPos(0,0,0)
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
	main()


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


