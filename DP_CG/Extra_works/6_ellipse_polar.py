from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)

def setpixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def ellipse_polar(rx, ry, xc, yc):
    x, y = 0, ry
    angle = 0
    end_angle = (22/7)/2

    while angle<=end_angle:
        angle=angle+0.001

        x=math.cos(angle)*rx
        y=math.sin(angle)*ry

        
        setpixel(x+xc,y+yc)
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc)    

def ellipse_nonPolar():
    














def main():
    a=int(input('rx='))
    b=int(input('ry='))
    xc=int(input('xc='))
    yc=int(input('yc='))
    print("starting window....")
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(200,200)
    glutCreateWindow("Ellipse")
    glutDisplayFunc(lambda: ellipse_polar(a, b, xc, yc))
    glutIdleFunc(lambda: ellipse_polar(a, b, xc, yc))
    clearscreen()
    glutMainLoop()

main()    

   


















