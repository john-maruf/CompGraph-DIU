from OpenGL.GL import *
from OpenGL.GLUT import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_horizontal_line(y):
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(50, y)
    glVertex2f(450, y)
    glEnd()

# Letter Functions
def draw_J(x, y, size=40):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # vertical stem
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    # bottom curve
    glVertex2f(x + w, y)
    glVertex2f(x, y)
    glVertex2f(x, y)
    glVertex2f(x, y + 0.25*h)
    glEnd()

def draw_O(x, y, size=40):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # rectangle approximation of O
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glVertex2f(x, y + h)
    glVertex2f(x, y)
    glEnd()

def draw_N(x, y, size=40):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y + h)
    glVertex2f(x, y + h)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glEnd()

# Digit Functions
def draw_1(x, y, size=40):
    glBegin(GL_LINES)
    glVertex2f(x + size//4, y)
    glVertex2f(x + size//4, y + size)
    glEnd()

def draw_6(x, y, size=40):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # left vertical
    glVertex2f(x, y)
    glVertex2f(x, y + h)
    # top horizontal
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h)
    # middle horizontal
    glVertex2f(x, y + h//2)
    glVertex2f(x + w, y + h//2)
    # bottom horizontal
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    # right vertical (bottom half)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h//2)
    glEnd()

def draw_5(x, y, size=40):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # top horizontal
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h)
    # middle horizontal
    glVertex2f(x, y + h//2)
    glVertex2f(x + w, y + h//2)
    # bottom horizontal
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    # vertical lines
    glVertex2f(x, y + h//2)
    glVertex2f(x, y + h)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h//2)
    glEnd()

# Main Display Function
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(0.0, 0.0, 1.0)  # blue

    # Draw horizontal line
    draw_horizontal_line(250)

    # Draw Name "JON" above line
    draw_J(100, 280)
    draw_O(180, 280)
    draw_N(260, 280)

    # Draw ID "1165" below line
    draw_1(120, 210)
    draw_1(160, 210)
    draw_6(200, 210)
    draw_5(260, 210)

    glutSwapBuffers()

# GLUT Setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow(b"Name and ID JON 1165")
glutDisplayFunc(showScreen)
glutMainLoop()