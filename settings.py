import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
SAND = (212, 171, 83)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Apocalipse"
BGCOLOR = SAND

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'wall.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                        'bullet_lifetime': 1000,
                        'rate': 250,
                        'kickback': 200,
                        'spread': 5,
                        'damage': 15,
                        'bullet_size': 'lg',
                        'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                         'bullet_lifetime': 500,
                         'rate': 900,
                         'kickback': 300,
                         'spread': 25,
                         'damage': 5,
                         'bullet_size': 'sm',
                         'bullet_count': 12}


# mob settings
MOB_HEALTH = 100
MOB_DMG = 10
MOB_KNOCKBACK = 20
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 175, 75, 100, 125, 150, 100]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
SPLAT = 'splat red.png'
FLASH_DURATION = 40
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_med.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 25
BOB_RANGE = 15
BOB_SPEED = 0.4
