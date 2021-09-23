"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Tor Erik Brown

********* HEY, READ THIS FIRST **********

This code generates a tree during fall. Every time the code is run it will generate a unique tree with a different set of branches and leaves.

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#below is the code for the turnk and branches of this tree. 
turtle.pensize(15)
turtle.up()
turtle.goto(0,50)
turtle.down()
turtle.right(90)
turtle.forward(325)

turtle.speed(400)

#Randomly generated branches

trunk = turtle.Turtle()

for i in range(15):#15 different unique branches
    randang = random.randrange(1,360)
    randang2 = random.randrange(-60,60)
    randbranch = random.randrange(50,150)
    randbranch2 = random.randrange(50,75)
    branchsize = random.randrange(5,10)
    branch2 = random.randrange(5,8)
    trunk.goto(0,50)
    trunk.pensize(branchsize)
    trunk.down()
    trunk.right(randang)
    trunk.forward(randbranch)
    trunk.right(randang2)
    trunk.pensize(branch2)
    trunk.forward(randbranch2)
    trunk.up()
    
#now the spirograph leaf pattern in fall colors

colorlist = [(242,230,65),(242,183,5),(217,103,4)]

leaf = turtle.Turtle()
leaf.pensize(8)

ic = 10
num = int(360/ic)
innercirc = 1
leaf.up()
leaf.goto(0,50)
leaf.down()

for i in range(num):
    randradius = random.randrange(40,125)
    color = random.choice (colorlist)
    leaf.color(color)
    leaf.circle(randradius)
    leaf.forward(innercirc)
    leaf.right(ic)
    
turtle.done()
    
# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
