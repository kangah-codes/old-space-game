"""
Note to self: Need to clean up A LOT of the code

"""
__author__ = "Joshua Akangah"

import math
import random
import pygame
import database
from animate import Animation

# sprite groups
bulletGroup = pygame.sprite.Group()
enemybulletGroup = pygame.sprite.Group()
meteorGroup = pygame.sprite.Group()
meteorParticleGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
enemyParticleGroup = pygame.sprite.Group()
satelliteGroup = pygame.sprite.Group()
shieldGroup = pygame.sprite.Group()
powerupGroup = pygame.sprite.Group()
smokeGroup = pygame.sprite.Group()

# temporary things
screen = pygame.display.set_mode((900, 600))
gamePlay = True
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

fps = 70

# loading game assets once
playerImages = [
    # type 1
    pygame.image.load("../assets/Player/playerShip1_blue.png"),
    pygame.image.load("../assets/Player/playerShip1_orange.png"),
    pygame.image.load("../assets/Player/playerShip1_green.png"),
    pygame.image.load("../assets/Player/playerShip1_red.png"),
    # type 2
    pygame.image.load("../assets/Player/playerShip2_blue.png"),
    pygame.image.load("../assets/Player/playerShip2_orange.png"),
    pygame.image.load("../assets/Player/playerShip2_green.png"),
    pygame.image.load("../assets/Player/playerShip2_red.png"),
    # type 3
    pygame.image.load("../assets/Player/playerShip3_blue.png"),
    pygame.image.load("../assets/Player/playerShip3_orange.png"),
    pygame.image.load("../assets/Player/playerShip3_green.png"),
    pygame.image.load("../assets/Player/playerShip3_red.png"),
    # damage images
    # player 1 damage
    pygame.image.load("../assets/Damage/playerShip1_damage1.png"),
    pygame.image.load("../assets/Damage/playerShip1_damage2.png"),
    pygame.image.load("../assets/Damage/playerShip1_damage3.png"),
    # player 2 damage
    pygame.image.load("../assets/Damage/playerShip2_damage1.png"),
    pygame.image.load("../assets/Damage/playerShip2_damage2.png"),
    pygame.image.load("../assets/Damage/playerShip2_damage3.png"),
    # player 3 damage
    pygame.image.load("../assets/Damage/playerShip3_damage1.png"),
    pygame.image.load("../assets/Damage/playerShip3_damage2.png"),
    pygame.image.load("../assets/Damage/playerShip3_damage3.png"),
    # fire image
    pygame.image.load("../assets/Effects/fire16.png"),
    # gun
    [
        pygame.image.load("../assets/Ship_Guns/gun00.png"),
        pygame.image.load("../assets/Ship_Guns/gun05.png"),
        pygame.image.load("../assets/Ship_Guns/gun08.png"),
        pygame.image.load("../assets/Ship_Guns/gun09.png"),
    ]
]

smokeImages = [
    pygame.transform.scale(pygame.image.load("../assets/Effects/spaceEffects_008.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Effects/spaceEffects_009.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Effects/spaceEffects_010.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Effects/spaceEffects_011.png"), (20, 20)),
]


meteorImages = [
    pygame.image.load("../assets/Meteors/meteorBrown_big1.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_big2.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_big3.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_big4.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_med1.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_med3.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_small1.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_small2.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_tiny1.png"),
    pygame.image.load("../assets/Meteors/meteorBrown_tiny2.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_big1.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_big2.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_big3.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_big4.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_med1.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_med2.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_small1.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_small2.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_tiny1.png"),
    pygame.image.load("../assets/Meteors/meteorGrey_tiny2.png"),
]

meteorParticles = [
    pygame.transform.smoothscale(pygame.image.load("../assets/Meteors/meteorBrown_tiny1.png"),(5, 5)),
    pygame.transform.smoothscale(pygame.image.load("../assets/Meteors/meteorGrey_tiny1.png"),(5,5))
]

enemyShipParticles = [
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip1_damage1.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip1_damage2.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip1_damage3.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip2_damage1.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip2_damage2.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip2_damage3.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip3_damage1.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip3_damage2.png"), (20, 20)),
    pygame.transform.scale(pygame.image.load("../assets/Damage/playerShip3_damage3.png"), (20, 20)),
    # rocket parts
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_030.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_031.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_029.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_027.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_028.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_021.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_008.png"), (20, 25)),
    pygame.transform.scale(pygame.image.load("../assets/Rocket_parts/spaceRocketParts_003.png"), (20, 25))# if missile.type not in (1,3):
                # if missile.type != 1 or missile.type != 3:
                #     if pygame.sprite.groupcollide(shieldGroup, bulletGroup, False, True):
                #         print(missile.type)
]

enemyShips = [
    pygame.image.load("../assets/Enemies/enemyBlack1.png"),
    pygame.image.load("../assets/Enemies/enemyBlack2.png"),
    pygame.image.load("../assets/Enemies/enemyBlack3.png"),
    pygame.image.load("../assets/Enemies/enemyBlack4.png"),
    pygame.image.load("../assets/Enemies/enemyBlack5.png"),
    pygame.image.load("../assets/Enemies/enemyBlue1.png"),
    pygame.image.load("../assets/Enemies/enemyBlue2.png"),
    pygame.image.load("../assets/Enemies/enemyBlue3.png"),
    pygame.image.load("../assets/Enemies/enemyBlue4.png"),
    pygame.image.load("../assets/Enemies/enemyBlue5.png"),
    pygame.image.load("../assets/Enemies/enemyGreen1.png"),
    pygame.image.load("../assets/Enemies/enemyGreen2.png"),
    pygame.image.load("../assets/Enemies/enemyGreen3.png"),
    pygame.image.load("../assets/Enemies/enemyGreen4.png"),
    pygame.image.load("../assets/Enemies/enemyGreen5.png"),
    pygame.image.load("../assets/Enemies/enemyRed1.png"),
    pygame.image.load("../assets/Enemies/enemyRed2.png"),
    pygame.image.load("../assets/Enemies/enemyRed3.png"),
    pygame.image.load("../assets/Enemies/enemyRed4.png"),
    pygame.image.load("../assets/Enemies/enemyRed5.png"),
    pygame.image.load("../assets/Enemies/spaceShips_001.png"),
    pygame.image.load("../assets/Enemies/spaceShips_002.png"),
    pygame.image.load("../assets/Enemies/spaceShips_003.png"),
    pygame.image.load("../assets/Enemies/spaceShips_004.png"),
    pygame.image.load("../assets/Enemies/spaceShips_005.png"),
    pygame.image.load("../assets/Enemies/spaceShips_006.png"),
    pygame.image.load("../assets/Enemies/spaceShips_007.png"),
    pygame.image.load("../assets/Enemies/spaceShips_008.png"),
    pygame.image.load("../assets/Enemies/spaceShips_009.png"),
    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("../assets/Enemies/spaceRockets_001.png"), (150, 500)), False, True),
    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("../assets/Enemies/spaceRockets_002.png"), (150, 500)), False, True),
    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("../assets/Enemies/spaceRockets_003.png"), (150, 500)), False, True),
    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("../assets/Enemies/spaceRockets_004.png"), (150, 500)), False, True),
]

satelliteImages = [
    pygame.image.load("../assets/Satellites/spaceBuilding_023.png"),
    pygame.image.load("../assets/Satellites/spaceBuilding_024.png"),
    pygame.image.load("../assets/Satellites/spaceStation_018.png"),
    pygame.image.load("../assets/Satellites/spaceStation_019.png"),
    pygame.image.load("../assets/Satellites/spaceStation_017.png"),
]

powerupImages = [
    # bolt
    pygame.image.load("../assets/Power-ups/bolt_silver.png"),
    pygame.image.load("../assets/Power-ups/bolt_gold.png"),
    # pills
    pygame.image.load("../assets/Power-ups/pill_red.png"),
    pygame.image.load("../assets/Power-ups/pill_yellow.png"),
    pygame.image.load("../assets/Power-ups/pill_green.png"),
    # shield
    pygame.image.load("../assets/Power-ups/shield_gold.png"),
    # star credits
    pygame.image.load("../assets/Power-ups/star_bronze.png"),
    pygame.image.load("../assets/Power-ups/star_gold.png"),
    pygame.image.load("../assets/Power-ups/star_gold.png"),

]


class Shield(pygame.sprite.Sprite):
    def __init__(self, player): 
        pygame.sprite.Sprite.__init__(self)
        self.shieldImage3 = pygame.image.load("../assets/Effects/shield1.png")
        self.shieldImage2 = pygame.image.load("../assets/Effects/shield2.png")
        self.shieldImage1 = pygame.image.load("../assets/Effects/shield3.png")
        self.image = self.shieldImage1
        # self.x = player.pos.x+player.rect.width/2-self.shieldImage.get_rect().width/2
        # self.y = player.pos.y-self.shieldImage.get_rect().height/4
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.player = player

    def update(self):
        self.rect.x, self.rect.y = self.player.pos.x+self.player.rect.width/2-self.rect.width/2, self.player.pos.y-self.rect.height/4
        self.mask = pygame.mask.from_surface(self.image)

class Player(pygame.sprite.Sprite):
    def __init__(self, typeOf, variation):
        """
        param type: The type of ship going to be used by player
        param variation: The color of the ship. Each type has 4 color variations
        variation should be from 1-3
        """
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        self.variation = variation
        if self.type == 1:
            self.damageImage1 = playerImages[12]
            self.damageImage2 = playerImages[13]
            self.damageImage3 = playerImages[14]
            self.life = 5
            self.bullets = 10
            if self.variation == 1:
                self.image = playerImages[0]
            elif self.variation == 2:
                self.image = playerImages[1]
            elif self.variation == 3:
                self.image = playerImages[2]
            else:
                self.image = playerImages[3]
        elif self.type == 2:
            self.damageImage1 = playerImages[15]
            self.damageImage2 = playerImages[16]
            self.damageImage3 = playerImages[17]
            self.life = 8
            self.bullets = 15
            if self.variation == 1:
                self.image = playerImages[4]
            elif self.variation == 2:
                self.image = playerImages[5]
            elif self.variation == 3:
                self.image = playerImages[6]
            else:
                self.image = playerImages[7]
        else:
            self.damageImage1 = playerImages[18]
            self.damageImage2 = playerImages[19]
            self.damageImage3 = playerImages[20]
            self.life = 10
            self.bullets = 25
            if self.variation == 1:
                self.image = playerImages[8]
            elif self.variation == 2:
                self.image = playerImages[9]
            elif self.variation == 3:
                self.image = playerImages[10]
            else:
                self.image = playerImages[11]
        # shield
        self.shieldTimer = 0
        self.shield = False
        self.shields = 1
        self.pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.damageLevel = 0
        self.fire = playerImages[21]
        self.fire_rect = self.fire.get_rect()
        self.delay = 0
        self.missiles = 0
        self.score = 0
        self.tempShield = Shield(self)
        shieldGroup.add(self.tempShield)

    def move(self):
        keyPress = pygame.key.get_pressed()
        mousePress = pygame.mouse.get_pressed()

        if keyPress[pygame.K_a]:
            self.pos.x -= self.speed

        if keyPress[pygame.K_d]:
            self.pos.x += self.speed

        if mousePress[0]:
            self.delay += 1
            if self.delay >= 5:
                if self.type == 1:
                    bulletGroup.add(Bullet(1, self.pos.x+self.rect.width/2 - 4.5, self.pos.y))
                elif self.type == 2:
                    bulletGroup.add(Bullet(1, self.pos.x+18, self.pos.y-10))
                    bulletGroup.add(Bullet(1, self.pos.x+self.rect.width-27, self.pos.y-10))
                elif self.type == 3:
                    bulletGroup.add(Bullet(1, self.pos.x+21, self.pos.y))
                    bulletGroup.add(Bullet(1, self.pos.x+self.rect.width/2 - 4.5, self.pos.y-27))
                    bulletGroup.add(Bullet(1, self.pos.x+self.rect.width-30, self.pos.y))
                self.delay = 0

    def update(self):
        self.pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        """ bug """
        #self.rect.midbottom = self.pos
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        shieldGroup.update()

        for powerup in powerupGroup:
            if pygame.sprite.collide_mask(self, powerup):
                if powerup.type == "bolt":
                    self.missiles += powerup.effect
                elif powerup.type == "pill":
                    self.life += powerup.effect
                elif powerup.type == "shield":
                    self.shields += 1
                else:
                    self.score += powerup.effect
                powerup.kill()

        for missile in enemybulletGroup:
            if not self.shield:
                if missile.type not in (1, 3):
                    if pygame.sprite.collide_mask(self, missile):
                        if missile.type == 4:
                            self.life -= missile.damage
                            smokeGroup.add(smokeAnimation(missile.pos.x, missile.pos.y))
                            missile.kill()
                        else:
                            self.life -= 1
                            smokeGroup.add(smokeAnimation(missile.pos.x, missile.pos.y))
                            missile.kill()
            else:
                pygame.sprite.groupcollide(shieldGroup, enemybulletGroup, False, True)

    def draw(self, display):
        if self.type == 1:
            display.blit(pygame.transform.flip(playerImages[22][0], False, True), ((self.pos.x+self.rect.width/2)-(playerImages[22][0].get_rect().width/2), self.pos.y - playerImages[22][0].get_rect().height/2))
            display.blit(self.fire, ((self.pos.x+self.rect.width/2) - self.fire_rect.width/2, self.pos.y + self.rect.height))

        elif self.type == 2:
            display.blit(pygame.transform.flip(playerImages[22][1], False, True), (self.pos.x+self.rect.width/6, self.pos.y+5))
            display.blit(pygame.transform.flip(playerImages[22][1], True, True), (self.pos.x+self.rect.width/1.5, self.pos.y+5))
            display.blit(self.fire, ((self.pos.x+self.rect.width/4) - self.fire_rect.width/2, self.pos.y + self.rect.height - 5))
            display.blit(self.fire, ((self.pos.x+self.rect.width) - self.fire_rect.width*2.6, self.pos.y + self.rect.height - 5))

        else:
            display.blit(pygame.transform.flip(playerImages[22][3], False, True), (self.pos.x+self.rect.width/8, self.pos.y+5))
            display.blit(pygame.transform.flip(playerImages[22][2], False, True), ((self.pos.x+self.rect.width/2)-(playerImages[22][2].get_rect().width/2), self.pos.y - playerImages[22][2].get_rect().height/2))
            display.blit(pygame.transform.flip(playerImages[22][3], True, True), (self.pos.x+self.rect.width/1.5, self.pos.y+5))
            display.blit(self.fire, ((self.pos.x+self.rect.width/5) - self.fire_rect.width/2, self.pos.y + self.rect.height - 10))
            display.blit(self.fire, ((self.pos.x+self.rect.width) - self.fire_rect.width*1.8, self.pos.y + self.rect.height - 10))

        # draw the player before damage images
        display.blit(self.image, self.pos)

        if self.damageLevel == 1:
            display.blit(self.damageImage1, self.pos)
        elif self.damageLevel == 2:
            display.blit(self.damageImage2, self.pos)
        elif self.damageLevel == 3:
            display.blit(self.damageImage3, self.pos)

        if self.shield:

            self.shieldTimer += 1

            if self.shieldTimer >= 0 and self.shieldTimer < 360:
                self.tempShield.shieldImage = self.tempShield.shieldImage1
            elif self.shieldTimer >= 360 and self.shieldTimer < 720:
                self.tempShield.shieldImage = self.tempShield.shieldImage2
            elif self.shieldTimer >= 720:
                self.tempShield.shieldImage = self.tempShield.shieldImage3

            #display.blit(self.tempShield.image, (self.pos.x+self.rect.width/2-self.tempShield.rect.width/2, self.pos.y-self.tempShield.rect.height/4))
            shieldGroup.draw(display)
            if self.shieldTimer >= 360*3:
                self.shieldTimer = 0
                self.shield = False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, typeOf, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("../assets/Lasers/laserBlue01.png"),
            pygame.transform.flip(pygame.image.load("../assets/Lasers/laserRed01.png"), False, True),
            pygame.transform.scale(pygame.image.load("../assets/Lasers/laserBlue10.png"), (15, 15)),
            pygame.transform.scale(pygame.image.load("../assets/Lasers/laserRed10.png"), (15,15))
        ]
        self.type = typeOf
        if self.type == 1:
            self.image = self.images[0]
        else:
            self.image = self.images[1]
        self.speed = 15
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.bType = "Bullet"
        self.delayTime = 0

    def update(self, display, player=None):
        # self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

        if self.images.index(self.image) in (2, 3):
            self.delayTime += 1
            if self.delayTime >= 10:
                self.kill()

        else:
            if self.type == 1:
                self.pos.y -= self.speed
                if self.pos.y + self.rect.height < 0:
                    self.kill()
            else:
                self.pos.y += self.speed
                if self.pos.y > 600:
                    self.kill()+self.rect.height

class Missile(pygame.sprite.Sprite):
    def __init__(self, typeOf, spawnX, spawnY, player):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        if self.type == 1:
            self.image = pygame.image.load("../assets/Missiles/spaceMissiles_006.png")
        elif self.type == 2:
            self.image = pygame.transform.flip(pygame.image.load("../assets/Missiles/spaceMissiles_006.png"), False, True)
        elif self.type == 3:
            self.image = pygame.image.load("../assets/Missiles/spaceMissiles_012.png")
        else:
            self.image = pygame.transform.flip(pygame.image.load("../assets/Missiles/spaceMissiles_012.png"), False, True)
        self.smoke_image = random.choice(smokeImages)
        if self.type in (1, 2):
            self.damage = 5
        else:
            self.damage = 10
        self.damage = 5
        self.speed = 10
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.fire = pygame.image.load("../assets/Effects/spaceEffects_003.png")
        self.delay = 0
        self.bType = "Missile"
        self.player = player
        self.player_pos = self.player.pos
        self.explosion_timer = 0
        self.timer = 0
        # to check if there is an enemy in the enemy sprites group to follow
        # if there is none, continue
        try:
            
            self.enemy = enemyGroup.sprites()[0]
            if self.enemy.type >= 10:
                self.speed = 15
            self.missile_pos = math.atan2(self.enemy.rect.center[0]-self.player.rect.center[0], -(self.enemy.rect.center[1]-self.player.rect.center[1]))
            if self.type != 1:
                if self.type not in (1,2): # if rot is false and is not a player missile
                    self.image = pygame.transform.rotate(self.image, 360-(self.missile_pos*57.29))
        except:
            pass
            

    def update(self, display, player):
        if self.image in smokeImages:
            self.delay += 1
            if self.delay >= 10:
                self.kill()
        else:
            self.rect.x, self.rect.y = self.pos.x, self.pos.y
            if self.type == 1:
                self.pos.y -= self.speed
                if self.pos.y + self.rect.height < 0:
                    self.kill()
                display.blit(self.fire, (self.pos.x+self.rect.width/2-self.fire.get_rect().width/2, self.pos.y+self.rect.height))
            elif self.type == 3:
                # this is to only chase enemies who are existing
                # if there is no enemy, the bullet will be destroyed
                if len(enemyGroup) != 0:
                    self.missile_pos = math.atan2(self.enemy.rect.center[0]-self.player.rect.center[0], -(self.enemy.rect.center[1]-self.player.rect.center[1]))
                    enemy = enemyGroup.sprites()[0]
                    distance = math.sqrt((math.pow((self.rect.center[0] - self.enemy.pos.x), 2) + math.pow((self.rect.center[1] - self.enemy.pos.y), 2)))
                    if distance != 0:
                        dx = (self.pos.x-self.enemy.rect.center[0])/distance
                        dy = (self.pos.y-self.enemy.rect.center[1])/distance
                    self.pos.x -= dx*(self.speed*2)
                    self.pos.y -= dy*(self.speed*2)
                    
                    
                else:
                    self.kill()
            else:
                if self.type == 4:
                    #print(f"Self.pos: {self.pos}, Player.pos: {self.player.pos}")
                    self.explosion_timer += 1
                    if self.explosion_timer >= 60:
                        self.smoke_timer = 0
                        self.image = random.choice(smokeImages)
                        self.smoke_timer += 1
                        if self.smoke_timer >= 20:
                            self.kill()
                    try:
                        self.missile_pos = math.atan2(self.player.rect.center[0]-self.enemy.rect.center[0], -(self.player.rect.center[1]-self.enemy.rect.center[1]))
                    except:
                        self.kill()
                    distance = math.sqrt((math.pow((self.rect.center[0] - self.player.rect.center[0]), 2) + math.pow((self.rect.center[1] - self.player.rect.center[1]), 2)))
                    #print(distance)
                    dx = (self.pos.x-(self.player.pos.x+(self.player.rect.width/2)))/distance
                    dy = (self.pos.y-(self.player.pos.y+(self.player.rect.height/2)))/distance
                    if distance != 0:
                        self.timer += dx
                        if self.timer >= 70:
                            self.timer = 0
                            self.image = pygame.transform.rotate(self.image, 360-(self.missile_pos*57.29))
                        dx = (self.pos.x-(self.player.pos.x+(self.player.rect.width/2)))/distance
                        dy = (self.pos.y-(self.player.pos.y+(self.player.rect.height/2)))/distance
                        """ bug """
                        # dx = (self.pos.x - self.player.rect.center[0])/distance
                        # dy = (self.pos.y - self.player.rect.center[1])/distance
                        #print(f"{dx, dy}")
                    #print(f"dx{dx}\dy{dy}\distance{distance}\player_pos{self.player.pos}\enemy_pos{self.enemy.pos}")
                        
                    self.pos.x -= dx*self.speed
                    self.pos.y -= dy*self.speed
                    # left = False
                    # top = False
                    # if self.player.pos.x > self.pos.x:
                    #     left = True
                    # if self.player.pos.y > self.pos.y:
                    #     top = True
                    # angle = math.tanh((self.player.pos.y-self.pos.y)/(self.player.pos.x-self.pos.x))
                    # print(self.pos.x)
                    # if top and left:
                    #     pygame.transform.rotate(self.image, 360 - angle)
                    # elif top and not left:
                    #     pygame.transform.rotate(self.image, 180 + angle)
                    # elif left and not top:
                    #     pygame.transform.rotate(self.image, angle)
                    # else:
                    #     pygame.transform.rotate(self.image, 180 - angle)
                elif self.type == 2:
                    self.pos.y += self.speed
                    if self.pos.y+self.rect.height > 600:
                        self.kill()

                elif self.type == 3:
                    self.pos.y += 0.5

        # for missile in bulletGroup:
        #     if pygame.sprite.collide_mask(self, missile) and self.type in (2, 4) and missile.type in (1, 3):
        #         self.image = self.smoke_image
        #         missile.kill()
        pygame.sprite.groupcollide(bulletGroup, enemybulletGroup, True, True)


class EnemyShipParticle(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY, typeOf):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        if self.type == 1:
            self.image = enemyShipParticles[random.randint(0, 8)]
        else:
            self.image = enemyShipParticles[random.randint(9, 16)]
        self.speed = 3
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.rect = self.image.get_rect()
        self.choices = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # using a list instead of randint to prevent a 0 occuring
        self.move_y = random.choice(self.choices)
        self.move_x = random.choice(self.choices)
        self.delay = 0

    def update(self):
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.pos.x += self.move_x
        self.pos.y += self.move_y
        self.delay += 1
        if self.delay >= 60:
            self.kill()

class MeteorParticle(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY, typeOf):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        if self.type == 1:
            self.image = meteorParticles[0]
        else:
            self.image = meteorParticles[1]
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.speed = 3
        self.rect = self.image.get_rect()
        self.choices = [-3, -2, -1, 1, 2, 3] # using a list instead of randint to prevent a 0 occuring
        self.move_y = random.choice(self.choices)
        self.move_x = random.choice(self.choices)
        self.delay = 0

    def update(self):
        #self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.pos.x += self.move_x
        self.pos.y += self.move_y
        self.delay += 1
        if self.delay >= 60:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteorImages)
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.choices = [-2, -1, 1] # using a list instead of randint to prevent a 0 occuring
        self.y_move = random.choice(self.choices)
        self.x_move = random.choice(self.choices)
        self.die_delay = 0

    def update(self, playerObject):
        #self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.pos.y += self.y_move
        self.pos.x += self.x_move

        if self.pos.y > 600 or self.pos.x + self.rect.width < 0 or self.pos.x > 900:
            self.kill()

        for bullet in bulletGroup:
            if pygame.sprite.collide_mask(self, bullet):
                for i in range(random.randint(20, 30)): # add a random number of particles
                    if meteorImages.index(self.image) < 10: # brown meteor
                        meteorParticleGroup.add(MeteorParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 1))
                    else:
                        meteorParticleGroup.add(MeteorParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 2))
                self.kill()

        if pygame.sprite.collide_mask(self, playerObject):
            for i in range(random.randint(0, 10), random.randint(10, 15)): # add a random number of particles
                if meteorImages.index(self.image) < 10: # brown meteor
                    meteorParticleGroup.add(MeteorParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 1))
                else:
                    meteorParticleGroup.add(MeteorParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 2))

            self.kill()
            playerObject.life -= 2

class smokeAnimation(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x_pos, y_pos
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.animation = Animation(
            ["../assets/Effects/spaceEffects_008.png","../assets/Effects/spaceEffects_009.png","../assets/Effects/spaceEffects_010.png","../assets/Effects/spaceEffects_011.png"],
            random.choice([0.5, 0.6, 0.7, 0.8, 0.9, 1.0]), 
            0.5
        )
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

    def update(self, dt):
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.image = self.animation.get_current_image()
        self.animation.animate(dt)

        if self.animation.is_last_image():
            self.kill()

class Satellite(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, typeOf):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        if self.type == 1:
            self.image = satelliteImages[0]
            self.life = 10
            self.speed = 0.5
        elif self.type == 2:
            self.image = satelliteImages[1]
            self.life = 10
            self.speed = .5
        elif self.type == 3:
            self.image = satelliteImages[2]
            self.life = 5
            self.speed = .8
        elif self.type == 4:
            self.image = satelliteImages[2]
            self.life = 5
            self.speed = .8
        else:
            self.image = satelliteImages[4]
            self.life = 10
            self.speed = .8
        if random.randint(0, 5) == 3:
            self.image = pygame.transform.rotate(self.image, random.randrange(0, 350))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(x_pos, y_pos)

    def update(self, display):
        self.pos.y += self.speed
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

        pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*3)/2, self.pos.y-10, self.life*3, 5), 0)

        if self.pos.y > 600:
            self.kill()

        if self.life <= 0:
            # randomly choosing a powerup to spawn when a satellite is destroyed 
            powerupChoices = ["bolt", "pill", "shield", "star"]
            powerupSubTypes = ["bronze", "silver", "gold", "red", "yellow", "green"]

            powerType = random.choice(powerupChoices)
            if powerType == "bolt":
                powerSubType = powerupSubTypes[random.randint(0, 1)]
            elif powerType == "pill":
                powerSubType = powerupSubTypes[random.randint(3, 5)]
            elif powerType == "shield":
                powerSubType = None
            else:
                powerSubType = powerupSubTypes[random.randint(0, 2)]

            for i in range(random.randrange(10, 20)):
                enemyParticleGroup.add(EnemyShipParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 1))

            powerupGroup.add(Powerup(powerType, powerSubType, self.pos.x, self.pos.y, True))

            self.kill()

        for bullet in bulletGroup:
            try:
                if pygame.sprite.collide_mask(self, bullet) and bullet.images.index(bullet.image) != 2:
                    if bullet.bType == "Bullet":
                        self.life -= 1
                        bullet.image = bullet.images[2]
            except:
                # bullet is a missile
                # bug here
                if bullet.image not in smokeImages and bullet.type not in (2, 4):
                    self.life -= bullet.damage
                    smokeGroup.add(smokeAnimation(bullet.pos.x, bullet.pos.y))
                    bullet.kill()

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY, typeOf, variation):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        self.variation = variation
        if self.type == 1:
            self.speed = random.randrange(1,3)
            self.life = 1
            self.shootDelay = 60
            if self.variation == 1:
                self.image = enemyShips[0]
            elif self.variation == 2:
                self.image = enemyShips[5]
            elif self.variation == 3:
                self.image = enemyShips[10]
            elif self.variation == 4:
                self.image = enemyShips[15]
        elif self.type == 2:
            self.speed = random.randrange(1,3)
            self.life = 3
            self.shootDelay = 60
            if self.variation == 1:
                self.image = enemyShips[1]
            elif self.variation == 2:
                self.image = enemyShips[6]
            elif self.variation == 3:
                self.image = enemyShips[11]
            elif self.variation == 4:
                self.image = enemyShips[16]
        elif self.type == 3:
            self.speed = random.randrange(1,3)
            self.life = 10
            self.shootDelay = 60
            if self.variation == 1:
                self.image = enemyShips[2]
            elif self.variation == 2:
                self.image = enemyShips[7]
            elif self.variation == 3:
                self.image = enemyShips[12]
            elif self.variation == 4:
                self.image = enemyShips[17]
        elif self.type == 4:
            self.speed = random.randrange(3,5)
            self.life = 15
            self.shootDelay = 60
            if self.variation == 1:
                self.image = enemyShips[3]
            elif self.variation == 2:
                self.image = enemyShips[8]
            elif self.variation == 3:
                self.image = enemyShips[13]
            elif self.variation == 4:
                self.image = enemyShips[18]
        elif self.type == 5:
            self.speed = random.randrange(3,5)
            self.life = 20
            self.shootDelay = 60
            if self.variation == 1:
                self.image = enemyShips[4]
            elif self.variation == 2:
                self.image = enemyShips[9]
            elif self.variation == 3:
                self.image = enemyShips[14]
            elif self.variation == 4:
                self.image = enemyShips[19]
        elif self.type == 6:
            self.speed = random.randrange(3,5)
            self.life = 50
            self.shootDelay = 60
            self.image = enemyShips[20]
        elif self.type == 7:
            self.speed = random.randrange(3,5)
            self.life = 100
            self.shootDelay = 60
            self.image = enemyShips[21]
        elif self.type == 8:
            self.speed = random.randrange(5,8)
            self.life = 100
            self.shootDelay = 60
            self.image = enemyShips[22]
        elif self.type == 9:
            self.speed = random.randrange(5,8)
            self.life = 100
            self.shootDelay = 60
            self.image = enemyShips[23]
        elif self.type == 10:
            self.speed = random.randrange(5,8)
            self.life = 100
            self.shootDelay = 60
            self.image = enemyShips[24]
        elif self.type == 11:
            self.speed = random.randrange(5,8)
            self.life = 150
            self.shootDelay = 60
            self.image = enemyShips[25]
        elif self.type == 12:
            self.speed = 7
            self.life = 150
            self.shootDelay = 60
            self.image = enemyShips[26]
        elif self.type == 13:
            self.speed = 7
            self.life = 150
            self.shootDelay = 60
            self.image = enemyShips[27]
        elif self.type == 14:
            self.speed = 7
            self.life = 150
            self.shootDelay = 60
            self.image = enemyShips[28]
        elif self.type == 15:
            self.speed = 3
            self.life = 300
            self.shootDelay = 60
            self.image = enemyShips[29]
        elif self.type == 16:
            self.speed = 3
            self.life = 300
            self.shootDelay = 60
            self.image = enemyShips[30]
        elif self.type == 17:
            self.speed = 3
            self.life = 300
            self.shootDelay = 60
            self.image = enemyShips[31]
        elif self.type == 18:
            self.speed = 3
            self.life = 300
            self.shootDelay = 60
            self.image = enemyShips[32]
        self.pos = pygame.math.Vector2(spawnX, spawnY)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.orangefire = pygame.image.load("../assets/Effects/fire07.png")
        self.bluefire = pygame.image.load("../assets/Effects/fire05.png")
        self.whiteFire = pygame.transform.flip(pygame.image.load("../assets/Effects/spaceEffects_006.png"), False, True)
        self.bluefireRect = self.bluefire.get_rect()
        self.fastRect = self.whiteFire.get_rect()
        self.switchDirection = None
        self.y_mov = random.randint(0, 2)
        self.blueFire = pygame.transform.smoothscale(self.bluefire, (40, 90))
        self.blueFireRect = self.blueFire.get_rect()
        self.WhiteFire = pygame.transform.smoothscale(self.whiteFire, (18, 90))
        self.timer = 0
        self.moveDirection = random.choice(["left", "right"])

        # adding enemies for wave 1
        # for i in range(self.wave+1, self.waveIncrement+1):
        #     enemyGroup.add(EnemyShip(random.randint(0, 800), random.randint(-200, 0), random.randint(1, 19), random.randint(1, 4)))

    def update(self, display, player_object):
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.pos.y += 0.5

        if self.pos.y > 600:
            self.kill()

        pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*0.5)/2, self.pos.y-10, self.life*0.5, 5), 0)

        if self.type in (1, 2, 3, 4, 5):
            display.blit(self.orangefire, (self.pos.x+self.rect.width/2-7, self.pos.y-20))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*50)/2, self.pos.y-10, self.life*50, 5), 0)


        elif self.type in (6, 7):
            display.blit(self.bluefire, (self.pos.x+self.rect.width/3.5, self.pos.y - 30))
            display.blit(self.bluefire, (self.pos.x+self.rect.width/2 + 7, self.pos.y - 30))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*25)/2, self.pos.y-10, self.life*50, 5), 0)

        elif self.type == 8:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width/2-self.bluefire.get_rect().width/2, self.pos.y-self.bluefire.get_rect().height-5))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*50)/2, self.pos.y-10, self.life*50, 5), 0)

        elif self.type == 9:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+(31*1.2)/2, self.pos.y - 31*1.2))
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width-31*1.1, self.pos.y - 31*1.2))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*50)/2, self.pos.y-10, self.life*50, 5), 0)
        
        elif self.type == 10:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+(31*1.15), self.pos.y - 31*1.2))
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width-31*1.65, self.pos.y - 31*1.2))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*50)/2, self.pos.y-10, self.life*50, 5), 0)
        
        elif self.type == 11:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.5), int(31*1.5))), (self.pos.x+self.rect.width/2-(14*1.5)/2, self.pos.y-40))
            pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*50)/2, self.pos.y-10, self.life*50, 5), 0)
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*35)/2, self.pos.y-10, self.life*35, 5), 0)

        elif self.type == 12:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+(31*1.15), self.pos.y - 21))
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width-31*1.65, self.pos.y - 21))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*35)/2, self.pos.y-10, self.life*35, 5), 0)

        elif self.type == 13:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+28, self.pos.y - 31*1.2))
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width-28*1.55, self.pos.y - 31*1.2))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*35)/2, self.pos.y-10, self.life*35, 5), 0)

        elif self.type == 14:
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+(31), self.pos.y - 31*1.2))
            display.blit(pygame.transform.smoothscale(self.bluefire, (int(14*1.2), int(31*1.2))), (self.pos.x+self.rect.width-31*1.5, self.pos.y - 31*1.2))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*35)/2, self.pos.y-10, self.life*35, 5), 0)

        elif self.type == 15:
            # blueFire = pygame.transform.smoothscale(self.bluefire, (40, 90))
            # fast = pygame.transform.smoothscale(self.whiteFire, (18, 90))
            display.blit(self.blueFire, (self.pos.x+self.rect.width/2-self.blueFireRect.width/2, self.pos.y-self.blueFireRect.height))
            display.blit(self.whiteFire, (self.pos.x+self.fastRect.width/2+5, self.pos.y-self.fastRect.height+5))
            display.blit(self.whiteFire, (self.pos.x+self.rect.width/2-self.fastRect.width/2, self.pos.y-self.fastRect.height+32))
            display.blit(self.whiteFire, (self.pos.x+self.rect.width-self.fastRect.width-9, self.pos.y-self.fastRect.height+5))
            #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*0.5)/2, self.pos.y-10, self.life*0.5, 5), 0)

        else:
            #self.fastRect = fast.get_rect()
            if self.type != 17:    
                display.blit(self.blueFire, (self.pos.x+self.rect.width/2-self.blueFireRect.width/2, self.pos.y-self.blueFireRect.height))
                #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*.5)/2, self.pos.y-10, self.life*.5, 5), 0)
            else:
                display.blit(self.blueFire, (self.pos.x+self.rect.width/2-self.blueFireRect.width/2, self.pos.y-self.blueFireRect.height/1.5))
                display.blit(self.WhiteFire, (self.pos.x+self.rect.width/4-self.blueFireRect.width/1.5, self.pos.y-self.blueFireRect.height/25+5))
                display.blit(self.WhiteFire, (self.pos.x+self.rect.width-self.blueFireRect.width/1.5, self.pos.y-self.blueFireRect.height/25+5))
                #pygame.draw.rect(display, (0, 255, 0), (self.pos.x+self.rect.width/2-(self.life*.5)/2, self.pos.y-10, self.life*.5, 5), 0)

        for bullet in bulletGroup:
            try:
                if pygame.sprite.collide_mask(self, bullet) and bullet.images.index(bullet.image) != 2:
                    if bullet.bType == "Bullet":
                        self.life -= 1
                        bullet.image = bullet.images[2]
            except:
                # bullet is a missile
                # bug here
                if bullet.image not in smokeImages and bullet.type not in (2, 4):
                    self.life -= bullet.damage
                    smokeGroup.add(smokeAnimation(bullet.pos.x, bullet.pos.y))
                    bullet.kill()

        if self.life <= 0: 
            if self.type not in (15, 16, 17, 18):
                for i in range(random.randint(0, 25), random.randint(25, 50)): # add a random number of particles
                    enemyParticleGroup.add(EnemyShipParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 1))
                self.kill()
            else:
                for i in range(random.randint(0, 50), random.randint(50, 100)): # add a random number of particles
                    enemyParticleGroup.add(EnemyShipParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 2))
                    enemyParticleGroup.add(EnemyShipParticle(self.pos.x+(self.rect.width/2), self.pos.y+(self.rect.height/2), 1))
                self.kill()
        if self.type < 15:
            if self.pos.x + self.rect.width < 900 and self.switchDirection == None: # first case
                if self.moveDirection == "left":
                    self.switchDirection = False
                else:
                    self.switchDirection = True
            if self.pos.x + self.rect.width >= 900 and self.switchDirection == True: # only if switch was true and is crossing boundaries
                self.switchDirection = False
            elif self.pos.x <= 0: # only if switch was false and is crossing boundaries
                self.switchDirection = True

            if self.switchDirection:
                self.pos.x += self.speed
            else:
                self.pos.x -= self.speed            

            self.rect.x, self.rect.y = self.pos.x, self.pos.y

        self.timer += 1

        if self.timer >= 60:
            self.timer = 0
            enemybulletGroup.add(Missile(4, self.pos.x+self.rect.width/2 - 19/2, self.pos.y, player))

        if self.pos.x + self.rect.width < 0 or self.pos.x > 900:
            self.kill()

waveCounter = database.EnemyWaveDatabase()

class Powerup(pygame.sprite.Sprite):
    def __init__(self, typeOf, subtype, spawnX, spawnY, fromWreck=False):
        pygame.sprite.Sprite.__init__(self)
        self.type = typeOf
        self.subtype = subtype
        self.effect = None
        if self.type == "bolt":
            if self.subtype == "silver":
                self.image = powerupImages[0]
                self.effect = 3
            else:
                self.image = powerupImages[1]
                self.effect = 5
        elif self.type == "pill":
            if self.subtype == "red":
                self.image = powerupImages[2]
                self.effect = 2
            elif self.subtype == "yellow":
                self.image = powerupImages[3]
                self.effect = 5
            else:
                self.image = powerupImages[4]
                self.effect = 10
        elif self.type == "shield":
            self.image = powerupImages[5]
            self.effect = True
        else:
            if self.subtype == "bronze":
                self.image = powerupImages[6]
                self.effect = 2
            elif self.subtype == "silver":
                self.image = powerupImages[7]
                self.effect = 5
            else:
                self.image = powerupImages[8]
                self.effect = 10
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = spawnX, spawnY
        self.speeds = [-3, -2, -1, 1, 2, 3]
        self.speed = random.choice(self.speeds)
        self.fromWreck = fromWreck

    def update(self):
        if self.fromWreck:
            self.rect.x += self.speed
            self.rect.y += self.speed
        
        else:
            if self.speed > 0:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

        if self.rect.x + self.rect.width < 0 or self.rect.x > 900 or self.rect.y > 600 or self.rect.y + self.rect.height < 0:
            self.kill()


"""
wave adding logic

- get current wave
- every 5 waves add half the total number of the wave a new type of enemy 

for example if in wave 5 there are 3 type 1s and 3 type 2s
remove all the type 1s and add 4 type 3s and 1 type 2
to make it 4 type 2s and 4 type 3s

"""


def addEnemyWave():
    currentWave = waveCounter.retrieveWave()[0]
    currentType = waveCounter.retrieveWave()[1]

    print(f"Current wave is {currentWave}")
    print(f"Current type is {currentType}")

    if currentType != 18:
        if currentWave % 5 == 0:
            print(f"Changing type from {currentType} to {currentType+1}")
            for i in range(2):
                enemyGroup.add(EnemyShip(random.randint(0, 900), random.randint(-500, 0), currentType, random.randint(1,4)))
            for i in range(2):
                enemyGroup.add(EnemyShip(random.randint(0, 900), random.randint(-500, 0), currentType+1, random.randint(1,4)))
            waveCounter.updateWave(True)
        else:
            for i in range(4):
                enemyGroup.add(EnemyShip(random.randint(0, 900), 0, currentType, random.randint(1,4)))
            waveCounter.updateWave()

    print(f"Number of enemies {len(enemyGroup)}")
        


# creating player
#  instance
player = Player(3, 3)

#enemyGroup.add(EnemyShip(100, -100, 17, 4))
#for i in range(random.randint(0, 10)):
# enemyGroup.add(EnemyShip(300, 0, 15, 4))

# enemyGroup.add(EnemyShip(random.randint(0, 700), -50, 14, 4))
# enemyGroup.add(EnemyShip(random.randint(0, 700), -50, 14, 4))

# for i in range(10):
#     meteorGroup.add(Meteor(random.randint(0, 900), random.randint(-100, 0)))

for i in range(10):
    satelliteGroup.add(Satellite(random.randint(0, 800), random.randint(0, 800), random.randrange(1, 4)))
powerupGroup.add(Powerup("star", "gold", 100, 100))

bg = pygame.image.load("../assets/Backgrounds/darkPurple.png")

while gamePlay:
    for event in pygame.event.get():
        # test for quittting
        if event.type == pygame.QUIT:
            waveCounter.clearDatabase()
            gamePlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemyGroup.add(EnemyShip(300, 0, random.randint(1, 18), 2))
            if event.key == pygame.K_g:
                for i in enemyGroup:
                    i.kill()
            if event.key == pygame.K_a and player.shields > 0:
                player.shield = True
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                bulletGroup.add(Missile(1, player.pos.x+player.rect.width/2 - 19/2, player.pos.y, player))
            if event.button == 2:
                bulletGroup.add(Missile(3, player.pos.x+player.rect.width/2 - 19/2, player.pos.y, player))

    # for missile in bulletGroup:
    #     if missile.bType == "Missile" and missile.type == 4:
    #         if pygame.sprite.collide_mask(player, missile):
    #             print(f"{i}")
    #             i+= 1
                #missile.image = missile.smoke_image

    # fill screen with black
    # screen.fill((0, 0, 0))

    

    screen.blit(pygame.transform.smoothscale(bg, (900, 600)), (0, 0))

    meteorGroup.update(player)
    meteorGroup.draw(screen)

    meteorParticleGroup.update()
    meteorParticleGroup.draw(screen)

    enemyGroup.draw(screen)
    enemyGroup.update(screen, player)

    enemyParticleGroup.update()
    enemyParticleGroup.draw(screen)

    satelliteGroup.update(screen)
    satelliteGroup.draw(screen)

    bulletGroup.update(screen, player)
    bulletGroup.draw(screen)

    enemybulletGroup.update(screen, player)
    enemybulletGroup.draw(screen)

    powerupGroup.update()
    powerupGroup.draw(screen)

    smokeGroup.update(fps/300.0)
    smokeGroup.draw(screen)

    # if len(enemyGroup) == 0:
    #     enemyGroup.add(EnemyShip(100, -100, 17, 4))

    player.draw(screen)
    player.update()
    player.move()

    # update screen 
    pygame.display.update()
    clock.tick(70)
