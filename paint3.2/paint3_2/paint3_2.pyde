dg = 0
r = 0
l = 0
t = 0
g = 0
h = 0
j = 0
bg = 125
def setup():
    size(1000,700)
    background(bg)
def draw():
    global dg,r,l,t,g
    t = random(1,255)
    #background(bg)
    fill(146,5,76)
    strokeWeight(0)
    rect(300,0,100,50)
    rect(140,0,100,50)
    rect(50,0,50,50)
    rect(470,0,100,50)
    rect(770,0,100,50)
    rect(640,0,100,50)
    rect(574,0,60,50)
    fill(154,148,148)
    rect(900,0,200,1000)
    fill(255)
    rect(900,20,50,50)
    fill(0,0,255)
    rect(900,80,50,50)
    fill(255)
    fill(255,0,0)
    rect(900,142,50,50)
    fill(255,204,153)
    rect(900,202,50,50)
    fill(255,255,0)
    rect(900,262,50,50)
    fill(0,255,51)
    rect(900,322,50,50)
    fill(255,0,127)
    rect(900,382,50,50)
    fill(153,0,76)
    rect(900,442,50,50)
    fill(0,0,0)
    rect(900,502,50,50)
    fill(0,0,52)
    rect(900,562,50,50)
    fill(102,51,0)
    rect(900,622,50,50)
    textSize(30)
    textAlign(CENTER,CENTER)
    text(u"цвет",350,5)
    text("+",190,5)
    text("-",75,5)
    text(u"точки",520,5)
    text(u"savee",813,5)
    text(u"ластик",690,5)
    text(u"ф0н",603,5)
    if mousePressed:
        if r < 0: 
            r = 1
        strokeWeight(r)
        line(mouseX,mouseY, pmouseX, pmouseY)
        
def mouseClicked():
    global dg, r,l, bg
    if mouseX>300 and mouseX<400 and mouseY > 0 and mouseY<100:
        stroke(random(255),random(255),random(255))
    if mouseX>140 and mouseX<240 and mouseY > 0 and mouseY<100:
        r += 10
    if mouseX>50 and mouseX<100 and mouseY > 0 and mouseY<100:
        r -= 10
    if mouseX>470 and mouseX<570 and mouseY > 0 and mouseY<100:   
        for g in range (1,101,1):
             ellipse(random(600),random(600),20,20) 
    if mouseX>770 and mouseX<870 and mouseY > 0 and mouseY<100:  
        saveFrame('frame.png')
    if mouseX>640 and mouseX<740 and mouseY > 0 and mouseY<100:
        stroke(bg)
    if mouseX>574 and mouseX<634 and mouseY > 0 and mouseY<100:
        bg = random(255)
        background(bg)
    if mouseX>900 and mouseX<1000 and mouseY > 20 and mouseY<100:
        stroke(255)
    if mouseX>900 and mouseX<1000 and mouseY > 80 and mouseY<100:
        stroke(0,0,255)
    if mouseX>900 and mouseX<1000 and mouseY > 142 and mouseY<200:    
        stroke(255,0,0)
    if mouseX>900 and mouseX<1000 and mouseY > 202 and mouseY<300:
        stroke(255,204,153)
    if mouseX>900 and mouseX<1000 and mouseY > 262 and mouseY<300:
        stroke(255,255,0)
    if mouseX>900 and mouseX<1000 and mouseY > 322 and mouseY<400:
        stroke(0,255,51)      
    if mouseX>900 and mouseX<1000 and mouseY > 382 and mouseY<500:
        stroke(255,0,127)
    if mouseX>900 and mouseX<1000 and mouseY > 442 and mouseY<500:
        stroke(153,0,76)    
    if mouseX>900 and mouseX<1000 and mouseY > 502 and mouseY<600:
        stroke(0,0,0)        
    if mouseX>900 and mouseX<1000 and mouseY > 562 and mouseY<600:
        stroke(0,0,51)    
    if mouseX>900 and mouseX<1000 and mouseY > 622 and mouseY<700:
        stroke(102,51,0)    
