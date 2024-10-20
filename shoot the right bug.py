import pgzrun
import random

HEIGHT = 800
WIDTH = 1000

#lists
gunfires = []
score = 0
bugs = []
level = 1

TITLE = "Shoot the bug"
# ship actor
ship = Actor("ship",(500,700))
#bug actor
x = random.randint(50,950)
bug = Actor("bug",(x,50))
bugs.append(bug)

def draw():
    screen.fill("blue")
    ship.draw()
    for bug in bugs:
        bug.draw()
    screen.draw.text("Score : " + str(score),(50,50))
    screen.draw.text("level : " + str(level),(50,70))
    for gunfire in gunfires:
        gunfire.draw()


def bugmaker():
    global bugs
    for i in range(len(bugs)):
        x = random.randint(50,950)
        bug = Actor("bug",(x,50))
        bugs.append(bug)



def update():
    global score,level
# bug move part
    for bug in bugs:
        bug.y = bug.y + 3
        if bug.y == 800:
            bug.y = 50
            bug.x = random.randint(50,950)
# ship moving part
    if keyboard.left:
        ship.x -= 4

    if keyboard.right:
        ship.x += 4 
#bug collide part
    for gunfire in gunfires:
        gunfire.y -= 7
        if gunfire.colliderect(bug):
            for bug in bugs:
                bug.x = random.randint(50,950)
                bug.y = 50
            gunfires.remove(gunfire)
            score += 100
        if gunfire.y < 0:
            gunfires.remove(gunfire) 
    
    if keyboard.space and len(gunfires) == 0:
        gunfire = Actor("bg",(ship.x,ship.y))
        gunfires.append(gunfire)
    #level 2

    if score %1000 == 0 and score != 0:
        level += 1

        bugmaker()
        






pgzrun.go()