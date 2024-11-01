from time import sleep
from draw import *

''' PARAMETERS '''

# TODO 1: représenter le problème principal : nombre de disques à déplacer, source et destination (utiliser un nombre ou des lettres A, B ou C).
NB_DISKS = 5
SOURCE = 'A'
DESTINATION ='C' 

''' CLASSES '''

class Node:
    def __init__(self, text):
        # Attributs du noeud

        self.text = text
        self.parent = None
        self.childs = []

        # - juste pour l'affichage
        self.x = 0
        self.y = 0

    def add_child(self, node):
        # Ajouter un fils au noeud
        self.childs.append(node)
        node.parent = self

''' INIT '''

# TODO 2: initialiser la séquence d'actions, déclarer actions comme étant une liste vide.
actions = []

''' FUNCTIONS '''

# Trouver une place auxiliaire

def find_aux(source, destination):
    for towers in ['A', 'B', 'C']:
        if towers != source and towers != destination:
            return towers

      



    return 

# Fonction récursive pour générer l'arbre AND des sous-problèmes
def move(disques, source, destination, parent=None):
    # Tree:
    node = Node(f"{disques}{source}{destination}")
    if parent:
        parent.add_child(node)

    # Find an auxiliary place different from source and destination
    auxiliaire = find_aux(source, destination)

    # If the number of disks to move is equal to 1
    if disques == 1:
        # Terminal node, add the action to the sequence
        actions.append([source, destination])
    else:
        # Apply this function on 3 subproblems (with node as the parent)
        
        # Move (disques - 1) from source to auxiliary
        move(disques - 1, source, auxiliaire, node)

        # Move 1 disk from source to destination
        move(1, source, destination, node)

        # Move (disques - 1) from auxiliary to destination
        move(disques - 1, auxiliaire, destination, node)

    return node


''' MAIN '''

# TODO 9: jouez!
"""
# init
from_place = ""
# run
while True:
    screen.fill((255, 255, 255))
    place = detect_keyboard()

    # Draw disks
    draw_hanoi(NB_DISKS, from_place)

    # Do action
    if place:
        if from_place:
            move_list(from_place, place)
            from_place = ""
        else:
            from_place = place

    # Update window
    pygame.display.update()
"""

# TODO 8: appeler la fonction move sur le problème principal (prendre 3 arguments: disques & source & destination), et mettre son résultat dans la variable node.
node = move(NB_DISKS, SOURCE, DESTINATION)


''' DRAW '''

# Show tree & actions (animation)
for i, action in enumerate(actions):
    if detect_exit():
        break

    screen.fill((255, 255, 255))

    # Draw the tree
    draw_tree(node, i-1)
    # Draw the disks
    draw_hanoi(NB_DISKS)

    # Update window
    pygame.display.update()

    # Edit the list of disks
    move_list(action[0], action[1])
    sleep(1)

# Show tree & actions
while True:
    if detect_exit():
        break

    screen.fill((255, 255, 255))

    # Draw the tree
    draw_tree(node, len(actions)-1)
    # Draw the disks
    draw_hanoi(NB_DISKS)

    # Update window
    pygame.display.update()
