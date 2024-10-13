import pgzrun
import random

HEIGHT = 800
WIDTH = 1000

#lists
gunfires = []

TITLE = "Shoot the bug"
# ship actor
ship = Actor("ship",(500,700))
#bug actor
x = random.randint(50,950)
bug = Actor("bug",(x,50))

def draw():
    screen.fill("blue")
    ship.draw()
    bug.draw()
    for gunfire in gunfires:
        gunfire.draw()


def update():
# bug move part
    bug.y = bug.y + 3
    if bug.y == 800:
        bug.y = 50
        bug.x = random.randint(50,950)
# ship moving part
    if keyboard.left:
        ship.x -= 4

    if keyboard.right:
        ship.x += 4 

    for gunfire in gunfires:
        gunfire.y -= 5

    if keyboard.space:
        gunfire = Actor("bg",(ship.x,ship.y))
        gunfires.append(gunfire)





pgzrun.go()