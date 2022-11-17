#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:44:40 2022

@author: cindyzhang
"""
from psychopy import core, visual, event
#core=time(core.wait, core.clock)
#visual=drawing stimuli(visual.window, visual.rect, visual.imagestim)
#event=mouse clicks and key presses

import random 

def runExperiment():
    
    win = visual.Window(size=(800, 800), pos=(400, -300), color=([0, 0, 0]))       
    
    nTrial = 3
    
    for trial in range(nTrial):
        
        print("-"*10)
        
        colors = shuffleColors()
        
        targetLocation, targetColor = chooseTarget(colors)
        
        print(targetLocation)
        print(targetColor)
    
        displaySquares(win, colors)
        
        core.wait(1)
        
        clearScreen(win)
        
        core.wait(1)
        
        displayTarget(win, targetColor)
        
        core.wait(1)
        
        clearScreen(win)
        
        core.wait(1)
        
        shapes = drawNineBlankSquares(win)
               
        core.wait(1)

    #    clickedSquare = waitResponse(shapes)
        
       # if clickedSqaure == targetLocation:
    #        print("correct")
     #   else:
      #      print("incorrect")
        
        core.wait(1)
        
    win.close()    

#def waitResponse(shapes):
    #timer = core.CountdownTimer(10)
   # mouse = event.Mouse(visible=True, newPos=None,win=win)
  #  while timer.getTime() > 0:
  #      for i, shape in enumerate(invisibleRects):
   #         if mouse.isPressedin(shape):
    #            print("clicked")
     #           return i
   # return None
    

def drawNineBlankSquares(win):
    shapes = []
    for y in [.6,0,-.6]:
        for x in [-.6,0,.6]:
            square = visual.Rect(win, width=0.4, height=0.4, fillColor="black", pos=(x,y))    
            square.draw()
            shapes.append(square)
            
    win.flip()   
    print("Choices!")    
    return shapes 
    
def chooseTarget(colors):
    randLocation = random.randint(1, 9)
    return (randLocation, colors[randLocation-1])
    
def shuffleColors():
    
    colors=["red","purple","lightBlue","black","blue","green","yellow","brown","white"]

    random.shuffle(colors)
    
    return colors
    
def displaySquares(win, colors):
    
    colorsIterator = 1
    
    for y in [.6,0,-.6]:
        for x in [-.6,0,.6]:
            square = visual.Rect(win, width=0.4, height=0.4, fillColor=colors[colorsIterator-1], pos=(x,y))    
            square.draw()
            
            colorsIterator+=1
            
    win.flip()
    print("Squares!")
    
    
def clearScreen(win):
    
    win.flip()
    win.flip()
    
    print("Gone!")
    
def displayTarget(win, color):
    
    square = visual.Rect(win, width=0.4, height=0.4, fillColor=color, pos=(0,0))    
    square.draw()  
    win.flip()

    
    print("Target!")
    
def waitResponse():
    print("Pls Click!")
    core.wait(0.5)
    

    
runExperiment()