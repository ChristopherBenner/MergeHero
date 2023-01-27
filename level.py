import pygame
class Level():
    def __init__(self, level, gem_grid, three_star, two_star, one_star):
        self.gem_grid = gem_grid
        self.level = level
        self.three_star = three_star
        self.two_star = two_star
        self.one_star = one_star
        self.stars_earned = 0

    def get_star_moves(self):
        return [self.three_star, self.two_star, self.one_star]
        
def get_gem_grid(current_level):
    return levels[current_level - 1].gem_grid

def get_max_level():
    return len(levels)


levels = []
gem_grid = [[0,0,0],['r','r','g'],['g','g','r']]
level1 = Level(1,gem_grid, 1,2,3)
#levels.append[level1]

gem_grid = [['r','g'],['r','g'],['g','r']]
level2 = Level(2,gem_grid,1,2,3)
#levels.append[level2]

gem_grid = [['r','b','r'],['b','g','b'],['g','r','g']]
level3 = Level(3,gem_grid, 2,3,4)
#levels.append[level3]

levels = [level1, level2, level3] * 5

