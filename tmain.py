from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Scale variables
scaleX, scaleY = 1.0, 1.0
Sx, Sy = 0.5, 1.6  

# Translation variables
posX, posY = 0.0, 0.0
move_step = 20.0


def draw_triangle():
    glColor3f(1.0, 0.6, 0.2)  # Orange
    
    glBegin(GL_TRIANGLES)
    glVertex2f(250, 250)  # Top
    glVertex2f(100, 100)  # Bottom Left
    glVertex2f(400, 100)  # Bottom Right
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Apply translation first
    glTranslatef(posX, posY, 0.0)

    # Apply scaling
    glScalef(scaleX, scaleY, 1.0)

    draw_triangle()

    glutSwapBuffers()


def keyboard(key, x, y):
    global scaleX, scaleY, posX, posY

    # Scaling
    if key == b'+':
        scaleX += Sx
        scaleY += Sy

    if key == b'-':
        scaleX -= Sx
        scaleY -= Sy

    # Movement
    if key == b'w':  # Up
        posY += move_step

    if key == b's':  # Down
        posY -= move_step

    if key == b'a':  # Left
        posX -= move_step

    if key == b'd':  # Right
        posX += move_step

    glutPostRedisplay()


def initiate():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Example 2 - Scale & Move 2D Triangle")

initiate()

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

print("Press + to scale up")
print("Press - to scale down")
print("Use W A S D to move the triangle")

glutMainLoop()
