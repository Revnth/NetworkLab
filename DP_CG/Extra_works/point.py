from OpenGL.GL import *
from OpenGL.GLU import *     
from OpenGL.GLUT import *  
  
import sys
import math

print("Packages imported successfully")
def clearscreen(): #clears the windows
    glClearColor(1.0, 1.0, 1.0, 0.0) 
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.5,-0.5)
    glEnd()
    glFlush()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("point")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(plot_points)
    clearscreen()
    glutMainLoop()
    
main()

