#******************************************************************#
#Name: SnakeGame                                                   #
#Author: Pascal Tietjen                                            #
#Class: C21 Erasmus Student                                        #
#Date: March 2017                                                  #
#Description: A Snake Game                                         #
#******************************************************************#
# Map erstellt und 2 verschiedene durchgaenge (test und normal) bereitgestellt.#
# Food bereitgestellt per random
#Schlange Beteit nur noch anwenden
#Naechster Schritt Schlange erstellen#

#imports
import pygame as sg
import random as ran

#Settings
#Screen
Width = 25 #width screen
Height = 25 #height screen
Speed = 8 #beginning speed
Speedt = 2 #speed time
Speed_Rise = 5 #rise of speed
Short = 12
Long = 1

#Colours
Yellow        = (255,0,255)
Yellow_Dark   = (150,0,150)
Green      = (0,255,0)
Green_Dark = (0,150,0)
Blue       = (0,0,255)
Blue_Dark  = (0,0,150)
White      = (255,255,255)
Black      = (0,0,0)

#Sizes
Block_Size = 25 #inner Blocksize
Block_Size_Out = 30 #Blocksize out

#End of Settings

#define Map
#Define the Wallblocks around the game
Wallstone = sg.Surface((Block_Size_Out,Block_Size_Out)) 
Wallstone.set_alpha(255)
Wallstone.fill(Yellow)
Wallstone_Dark = sg.Surface((Block_Size,Block_Size))
Wallstone_Dark.set_alpha(255)
Wallstone_Dark.fill(Yellow_Dark)

#draw map where the around wall should be
def drawmap(surface):
        #sides
        for y in range(Height+1):
                surface.blit(Wallstone,(0,y*Block_Size_Out))
                surface.blit(Wallstone_Dark,(2,y*Block_Size_Out+2))               
                surface.blit(Wallstone,((Width+1)*Block_Size_Out,y*Block_Size_Out))
                surface.blit(Wallstone_Dark,((Width+1)*Block_Size_Out+2,y*Block_Size_Out+2))

        #bottom and top
        for x in range(Width+2):
                surface.blit(Wallstone,(x*Block_Size_Out,0))
                surface.blit(Wallstone_Dark,(x*Block_Size_Out+2,2))               
                surface.blit(Wallstone,((x*Block_Size_Out,(Height+1)*Block_Size_Out)))
                surface.blit(Wallstone_Dark,(x*Block_Size_Out+2,(Height+1)*Block_Size_Out+2))

#Make Food
class food:
        def __init__(self,surface,minx,maxx,miny,maxy):
                self.surface = surface
                self.posx = ran.randint(minx,maxx)
                self.posy = ran.randint(miny,maxy)

                #Look to Draw
                self.Foodstone = sg.Surface((Block_Size_Out,Block_Size_Out))
                self.Foodstone.set_alpha(255)
                self.Foodstone.fill(Green)
                self.Foodstone_Dark = sg.Surface((Block_Size,Block_Size))
                self.Foodstone_Dark.set_alpha(255)
                self.Foodstone_Dark.fill(Green_Dark)

        #Get the Position
        def Position(self):
                return(self.posx,self.posy)

        #Draw it
        def draw(self):
                fs = self.Foodstone
                fsd = self.Foodstone_Dark
                fss = self.surface

                fp = self.Position()
                fss.blit(fs,(fp[1]*Block_Size_Out,fp[0]*Block_Size_Out))
                fss.blit(fsd,(fp[1]*Block_Size_Out+2,fp[0]*Block_Size_Out+2))

#Make Snake
class snake:

        def __init__(self,surface,headx=(Width/2),heady=(Height/2)):
                     self.surface = surface
                     self.length = 10
                     self.posline = [(headx,y) for y in reversed(range(heady-self.legth+1,heady+1))]
                     self.md = Right
                     self.crashed = False

                     #Draw the Snake
                     self.Snakestone = sg.Surface((Block_Size_Out,Block_Size_Out))
                     self.Snakestone.set_alpha(255)
                     self.Snakestone.fill(Green)
                     self.Snakestone_Dark = sg.Surface((Block_Size,Block_Size))
                     self.Snakestone_Dark.set_alpha(255)
                     self.Snakestone_Dark.fill(Green_Dark)

                     #Delete Snakesstone
                     self.Blackstone = sg.Surface((Block_Size_Out,Block_Size_Out))
                     self.Blackstone.set_alpha(255)
                     self.Blockstone.fill(Black)

                     
        #Where is the Head
        def Get_Pos(self):
                     return(self.posline[0])


        #Where is the whole Snake
        def Get_Pos_W(self):
                     return self.posline

        #Where to go
        def Get_Md(self):
                     return self.md

        #Modify the Direction
        def Set_Md(self,direction):
                     self.md = direction

        #A Bigger Snake
        def Inc_L(self):
                     self.length += 1

        #Lets Move and Check
        def move(self):
                     motion = self.Get_Md
                     head = self.Get_Pos

                     #Where to Go
                     if motion == Up:
                             posline = [head[0]-1,head[1]]
                     elif motion == Down:
                             posline = [head[0]+1,head[1]]
                     elif motion == Right:
                             posline = [head[0],head[1]+1]
                     elif motion == Left:
                             posline = [head[0],head[1]-1]

                     posline.extend(self.Posline[:-1])
                     self.Posline = posline

                     #Check
                     if self.Get_Pos() in self.Get_Pos_W()[1:]:
                             self.crashed = True

        #Is the snake dead?
        def Check(self):
                     return self.crashed

        #Now grow
        def grow(self):
                     last = self.Get_Pos_W()[-1]
                     self.length += 1
                     self.posline.append((last[0]-1,last[1]))


        #Lets see the Snake
        def Draw_S(self):
                     sk = self.Snakestone
                     skd = self.Snakestone_Dark
                     sf = self.surface

                     for blockpos in self.Get_Pos_W():
                             sf.blit(sk,(blockpos[1]*Block_Size_Out,blockpos[0]*Block_Size_Out))
                             sf.blit(skd,(blockpos[1]*Block_Size_Out+2,blockpos[0]*Block_Size_Out+2))


        #Remove
        def remove(self):
                     bs = self.Blackstone
                     sf = self.surface

                     for blockpos in self.Get_Pos_W():
                             sf.blit(bs,(blockpos[1]*Block_Size_Out,blockpos[0]*Block_Size_Out))



                     
#initialize
sg.init() #initialize pygame
layout = sg.font.SysFont(sg.font.get_default_font(),40) #Layout from the Font
starttext = layout.render("Welcome, Press Any Key to Start!",1,White) #Text Before the Game on the screen
screen = sg.display.set_mode(((Width+2)*Block_Size_Out,(Height+2)*Block_Size_Out)) #Size of the screen

food1 = food(screen,1,Height,1,Width)
food1.__init__(screen,1,Height,1,Width)
drawmap(screen) #Draw the Map
screen.blit(starttext,((Width-10)*Block_Size_Out/2,Height*Block_Size_Out/2)) #Show Beginning Text

testtext = layout.render("Test",1,White) #Text Before the Game on the screen
weitertext = layout.render("Weiter",1,White) #Text Before the Game on the screen

start = True
while start:
        drawmap(screen)
        sg.display.flip()
        key = sg.event.wait()
        if key.type == sg.KEYDOWN:
                start = False

if key.key == 116:
        screen.fill(Black)
        drawmap(screen)
        screen.blit(testtext,((Width-10)*Block_Size_Out/2,Height*Block_Size_Out/2)) #Show Beginning Text
        sg.display.flip()

else:
        screen.fill(Black)
        food1.draw()
        drawmap(screen)
      #  screen.blit(weitertext,((Width-10)*Block_Size_Out/2,Height*Block_Size_Out/2)) #Show Beginning Text
        sg.display.flip()

#loop
gaming = True
while gaming:
       # drawmap(screen)
       # sg.display.flip()
        gaming = True
