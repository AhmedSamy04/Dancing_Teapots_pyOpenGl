import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

##############################################
######### Constants ##########################
##############################################

rangle = 0
rotate_self = 0
zloc = 0
INTERVAL = 1


####################################################################################

def init():
    glClearColor(0.0, 0.0, 0.0, 0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#####################################################################################

def teapots_cylinders(x = 0, y = 0, i = 0):
    global rangle
    global rotate_self
    global zloc
    global z

    z = 2 * sin(i + zloc) + 9
    glPushMatrix()
    glColor(1, 0, 1)
    glRotate(rangle, 0, 0, 1)
    glTranslate(x, y, z)
    glRotate(rotate_self, 0, 0, 1)
    glRotate(90, 1, 0, 0)
    glutWireTeapot(2)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(0.2, z, 10, 10)
    glPopMatrix()


def Display():
    global rangle
    global rotate_self
    global zloc
    global z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(20, 20, 20,
              0, 0, 0,
              0, 0, 1)

    glColor(1, 1, 1)
    glPushMatrix()
    glRotate(rangle, 0 ,0, 1)
    glutSolidCylinder(17, 5, 70, 70)
    glPopMatrix()

    #draw teapot and cylinders
    for i in np.arange(0, 360, 72):
        x = 12 * cos(i * pi / 180)
        y = 12 * sin(i * pi / 180)
        teapots_cylinders(x, y, i / 72)


    rangle += 0.15
    rotate_self += 0.25
    zloc += 0.01
    glutSwapBuffers()


def timer(v):
    Display()
    glutPostRedisplay()
    glutTimerFunc(INTERVAL, timer, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Dancing Teapot")
    glutDisplayFunc(Display)
    glutTimerFunc(INTERVAL, timer, 1)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
