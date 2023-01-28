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



gem_grid = [['r','g'],['r','g'],['g','r']]
level2 = Level(2,gem_grid,1,2,3)

gem_grid = [['r','g'],['g','g'],['r','r']]
level3 = Level(3, gem_grid, 2,4,6)

gem_grid = [['r','b','r'],['b','g','b'],['g','r','g']]
level4 = Level(4,gem_grid, 2,3,4)

gem_grid = [['r','b','g'],['b','g','r'],['r','b','g']]
level5 = Level(5,gem_grid,2,3,4)

gem_grid = [[0,'k',0],['r','g','r'],['g','g','r']]
level6 = Level(6, gem_grid,2,3,4)

gem_grid = [['r','g','b'],['r','g','b'],['b','r','g']]
level7 = Level(7, gem_grid,2,4,6)

gem_grid = [['r','g','b','g'],['r','g','b','g'],['b','r','g','b'],[0,'g','b','b']]
level8 = Level(8, gem_grid,4,6,8)

gem_grid = [['r','g','b','g'],['r','g','b','g'],['b','r','g','b'],['k','g','b','b']]
level9 = Level(9, gem_grid,3,5,7)

gem_grid = [[0,'b',0],['r','g','r'],['b','r','b'],['g','k','g']]
level10 = Level(10,gem_grid, 7,8,9)

gem_grid = [[0,'b',0,0],['r','g','r','b'],['b','r','b','g'],['g','k','b','b']]
level11 = Level(11,gem_grid, 8,10,12)

gem_grid = [['r','g','b','r','g'],['g','b','r','g','r'],['r','g','b','r','g']]
level12 = Level(12, gem_grid, 3,5,7)

gem_grid = [[0,'b',0],['r','g','r'],['b','r','b'],['g','k','g'],['k','b','k'],['r','g','r'],['b','r','b'],['g','k','g']]
level13 = Level(13, gem_grid, 14,16,18)

gem_grid = [[0,'b',0,0,0],['r','g','r','b','r'],['b','r','b','g','r'],['g','k','b','r','b']]
level14 = Level(14, gem_grid, 8,10,12)

gem_grid = [['r','g','b','r','g','b'],['g','b','r','g','b','r'],['b','r','g','b','r','g'],['r','g','b','r','g','b'],['g','b','r','g','b','r'],['b','r','g','b','r','g']]
level15 = Level(15, gem_grid, 12,14,16)

levels = [level1, level2, level3, level4,level5, level6, level7, level8, level9, level10, level11, level12, level13, level14, level15]

