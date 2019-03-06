from queue import PriorityQueue
from implementation import *

start, goal = (5, 6), (7, 8)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
print()


# g = SquareGrid(30, 15)
# g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
# draw_grid(g)