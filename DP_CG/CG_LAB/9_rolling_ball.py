
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math


WINDOW_SIZE = 1000
GLOBAL_X_POSTION = -500
GLOBAL_Y_POSTION = 0
TARGET_FPS=60
STATE= 1
SPEED=4
ANGLE=0
THETA=0
choice=0
X1_GROUND=-1000
Y1_GROUND=0
X2_GROUND=1000
Y2_GROUND=0



BALL_RADIUS =  float(input("Ball Radius: "))

TOP_X=GLOBAL_X_POSTION
TOP_Y=GLOBAL_Y_POSTION + BALL_RADIUS
BOTTOM_X=GLOBAL_X_POSTION
BOTTOM_Y=GLOBAL_Y_POSTION - BALL_RADIUS

def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE) 

def update(value):
    global GLOBAL_X_POSTION 
    global GLOBAL_Y_POSTION 
    global STATE
    global WINDOW_SIZE
    global SPEED
    global ANGLE
    global THETA
    global TOP_X
    global TOP_Y
    global BOTTOM_X
    global BOTTOM_Y
    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,int(0))

    if choice == 1:
        if(STATE == 1):
            if(GLOBAL_X_POSTION<WINDOW_SIZE):
                GLOBAL_X_POSTION=SPEED+GLOBAL_X_POSTION
              
                TOP_X=GLOBAL_X_POSTION
                TOP_Y=GLOBAL_Y_POSTION + BALL_RADIUS
                BOTTOM_X=GLOBAL_X_POSTION
                BOTTOM_Y=GLOBAL_Y_POSTION - BALL_RADIUS
                THETA=THETA-1
                TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y=rotation(TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y,THETA,GLOBAL_X_POSTION,GLOBAL_Y_POSTION)
            else:
                STATE=-1
        elif(STATE == -1):
            if(GLOBAL_X_POSTION>-WINDOW_SIZE):
                GLOBAL_X_POSTION=-SPEED+GLOBAL_X_POSTION
                TOP_X=GLOBAL_X_POSTION
                TOP_Y=GLOBAL_Y_POSTION + BALL_RADIUS
                BOTTOM_X=GLOBAL_X_POSTION
                BOTTOM_Y=GLOBAL_Y_POSTION - BALL_RADIUS
                THETA=THETA+1
                TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y=rotation(TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y,THETA,GLOBAL_X_POSTION,GLOBAL_Y_POSTION)
            else:
                STATE=1
    if choice == 2:
        if(GLOBAL_X_POSTION<WINDOW_SIZE):
            GLOBAL_X_POSTION=SPEED+GLOBAL_X_POSTION
            GLOBAL_Y_POSTION= GLOBAL_Y_POSTION-(SPEED*math.tan(ANGLE))
            TOP_X=GLOBAL_X_POSTION
            TOP_Y=GLOBAL_Y_POSTION + BALL_RADIUS
            BOTTOM_X=GLOBAL_X_POSTION
            BOTTOM_Y=GLOBAL_Y_POSTION - BALL_RADIUS
            THETA=THETA-1
            TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y=rotation(TOP_X,TOP_Y,BOTTOM_X,BOTTOM_Y,THETA,GLOBAL_X_POSTION,GLOBAL_Y_POSTION)




    
# Here is my keyboard input code
def buttons(key,x,y):
    global SPEED
    if key == b'f':
        SPEED=SPEED+1
        print(SPEED)
    if key == b's':
        SPEED=SPEED-1
        print(SPEED)
    glutPostRedisplay()

def rotation(x1,y1,x2,y2,angle,xr,yr):
    cosT=  math.cos(angle)
    sinT=  math.sin(angle)
    X1 = (x1-xr)*cosT + (y1-yr)*sinT + xr
    Y1 = -(x1-xr)*sinT + (y1-yr)*cosT + yr
    X2 = (x2-xr)*cosT + (y2-yr)*sinT + xr
    Y2 = -(x2-xr)*sinT + (y2-yr)*cosT + yr
    rgb =(0,1,0)
    return(X1,Y1,X2,Y2)


def drawCircle(x,y):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)    
    glVertex2f(x, y);

    while(i<=360):

        glVertex2f(BALL_RADIUS*math.sin(math.pi * i / 180.0) + GLOBAL_X_POSTION,
                   BALL_RADIUS*math.cos(math.pi * i / 180.0) + GLOBAL_Y_POSTION)
        i=i+1.0

    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(TOP_X,TOP_Y)
    glVertex2f(BOTTOM_X,BOTTOM_Y)
    glEnd()





def drawBall():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,1.0,0.0)
    drawCircle(GLOBAL_X_POSTION,GLOBAL_Y_POSTION)
    draw_ground()
    glutSwapBuffers()

def draw_ground():
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_LINES)
    if choice == 1:       
        glVertex2f(WINDOW_SIZE,-BALL_RADIUS)
        glVertex2f(-WINDOW_SIZE,-BALL_RADIUS)
    if choice == 2:
        glVertex2f(X1_GROUND,Y1_GROUND)
        glVertex2f(X2_GROUND,Y2_GROUND)
    glEnd()
    glFlush()



def main():
    global choice
    global ANGLE
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global X1_GROUND,Y1_GROUND,X2_GROUND,Y2_GROUND

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB  | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    while(choice!=2):
        choice=int(input("Enter\n1.Rolling Ball about Flat surface \n2.Rolling Ball about Inclined Plane\n"))


        if choice ==1:
            glutCreateWindow("Rolling Ball About flat surface")
            glutDisplayFunc(drawBall)
            glutTimerFunc(0,update,0)
            glutIdleFunc(drawBall)
            glutKeyboardFunc(buttons)

        elif choice ==2:
    
            glutCreateWindow("Rolling Ball About Inclined Plane")
            ANGLE=int(input('angle='))
            ANGLE= (ANGLE*(22/7))/180
            X1_GROUND,Y1_GROUND,X2_GROUND,Y2_GROUND=rotation(-2828.5,0,2828.5,0,ANGLE,0,0)
            GLOBAL_Y_POSTION=Y1_GROUND+(BALL_RADIUS/math.cos(ANGLE))
            GLOBAL_X_POSTION=X1_GROUND

            glutDisplayFunc(drawBall)
            glutTimerFunc(0,update,0)
            glutIdleFunc(drawBall)
            glutKeyboardFunc(buttons)
            

        else:
            print("Invalid Choice") 

        init()
        glutMainLoop()

main()