import turtle 
import time
wn = turtle.Screen()
wn.title("Animation Practice")


Player = turtle.Turtle()
Player.shape('square')
Player.color('green')

while True: 
    wn.bgcolor('black')
    time.sleep(0.5)
    Player.shape('square')
    time.sleep(0.5)
    wn.bgcolor('orange')
    Player.shape('circle')
    time.sleep(0.5)
    wn.bgcolor('purple')
    time.sleep(0.5)
