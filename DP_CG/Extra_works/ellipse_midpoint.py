from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

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


def ellipse_Midpoint(a,b,xc,yc):
    x,y=0,b
    

    p1=((b*b)-(a*a*b)+(0.25*a*a))
    
    u=2*b*b*x   
    v=2*a*a*y

    while u<v:
    
        if p1<0 :
            x+=1
            u=u+(2*b*b)
            p1=p1+u+(b*b)

        else:
            x+=1
            y-=1
            u=u+(2*b*b)
            v=v-(2*a*a)
            p1=p1+u-v+(b*b)

        setpixel(x+xc,y+yc)
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc)

     
    p2=((b*b)*((x+0.5)*(x+0.5))) + ((a*a)*((y-1)*(y-1)))-(a*a*b*b)
   
    while y>0:
      



        if p2>0:
            y-=1
            v=v-(2*a*a)
            p2=p2-v+(a*a)

        else:
            x+=1
            y-=1

            u=u+(2*b*b)
            v=v-(2*a*a)
            p2=p2+u-v+(a*a)


        setpixel(x+xc,y+yc)
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc)    



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
    glutCreateWindow("Ellipse using Midpoint Algorithm")
    glutDisplayFunc(lambda: ellipse_Midpoint(a, b, xc, yc))
    glutIdleFunc(lambda: ellipse_Midpoint(a, b, xc, yc))
    clearscreen()
    glutMainLoop()

main()    

   


















