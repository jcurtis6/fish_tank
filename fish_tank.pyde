from random import randint

def setup():
    size (600, 600)
    #ocean
    r = random (0, 255)
    g = random (0, 255)
    b = random (0, 255)
    background(92, 182, 255)
    fish_color = color(255, 149, 92)
    i = 1
    
    while i < randint(10, 20):
        fishX = randint(100, 400)
        fishY = randint(100, 400)
        print(fish(fishX, fishY, r, g, b))
        
        i = i + 1
        
        
def fish(x, y, r, g, b):
    fill(r, g, b) #fish body
    ellipse(x - 30, y , 60, 30)
    triangle(x, y, x + 20, y - 20, x + 20, y + 20)
    
        
    
    
    
    
    
    
    
