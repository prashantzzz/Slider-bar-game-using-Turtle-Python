import turtle,time,winsound

win=turtle.Screen()
win.setup(810,509)
win.getcanvas()._root().overrideredirect(True)
win.bgpic('circuit-off.gif')
win.register_shape('gradient2.gif'); win.register_shape('grove.gif')
win.register_shape('green-on.gif'); win.register_shape('green-off.gif')

#setting sliders:
sld1=turtle.Turtle(); sld2=turtle.Turtle()
sld3=turtle.Turtle(); sld4=turtle.Turtle()

grn=turtle.Turtle()
grn.penup(),grn.goto(-250,0),grn.shape('green-off.gif')

grv1=turtle.Turtle(); grv2=turtle.Turtle()
grv3=turtle.Turtle(); grv4=turtle.Turtle()
grove_list=[grv1,grv2,grv3,grv4]
slider_list=[sld1,sld2,sld3,sld4]
a=1; x=0; stop=False

for grv in grove_list:
    if grv==grove_list[0]:sldx, sldy=-200, -540
    if grv==grove_list[1]:sldx, sldy=-68,-640
    if grv==grove_list[2]:sldx, sldy=68,-740
    if grv==grove_list[3]:sldx, sldy=200,-840
    grv.speed(0),grv.penup(),grv.goto(sldx,-560),grv.shape('grove.gif')
while True:
    for grv in grove_list:
        grv.speed('normal')
        grv.goto(grv.xcor(),0)
    if grv==grove_list[3]:break
 
for slide in slider_list:
    if slide==slider_list[0]:sldx=-200
    if slide==slider_list[1]:sldx=-68
    if slide==slider_list[2]:sldx=68
    if slide==slider_list[3]:sldx=200
    slide.penup(),slide.speed(0)
    slide.right(90),slide.speed('normal'),slide.goto(sldx,-165),slide.speed('normal'),slide.shape('gradient2.gif')

turtle.listen()
def bnd():
    global stop,slider,a,x,y
    stop=True
    try:
        if slider!=3 and -50<slider_list[slider].ycor()<50:
            winsound.PlaySound('Speech Disambiguation.wav', winsound.SND_ASYNC)
            grn.shape('green-on.gif')
            win.update(),time.sleep(0.5)
            slider+=1;stop=False
            main()
    
        elif slider==3 and -50<slider_list[slider].ycor()<50:
            winsound.PlaySound('Speech Disambiguation.wav', winsound.SND_ASYNC)
            grn.shape('green-on.gif')
            win.bgpic('circuit-on.gif')
            for slider in slider_list:
                slider.clear(),win.update()
            for grv in grove_list:
                grv.clear(),win.update()
            win.update(),time.sleep(3),win.bye()
    except:pass
    
    else: stop=False
        
slider=0
def main():
    global x,a,y,slider,stop,sldx
    try:
        while True:
            grn.shape('green-off.gif')
            for i in range(34):
                if not stop:
                    y=round((x**2)*0.1,2)
                    if y==28.9:
                        a*=-1
                    x+=(1*a)
                    win.onkey(bnd,'p')
                    slider_list[slider].sety(slider_list[slider].ycor()+y)    
            a*=-1;x=0        
            for i in range(34):
                if not stop:
                    y=-round((x**2)*0.1,2)
                    if y==-28.9:
                        a*=-1
                    x+=(1*a)
                    win.onkey(bnd,'p')
                    slider_list[slider].sety(slider_list[slider].ycor()+y)  
            a*=-1; x=0
    except:pass

main()

