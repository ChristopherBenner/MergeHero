import csv
def get_new_gem_grid():
    with open('new_gem_grid.csv','r') as gem_reader:
        reader = csv.reader(gem_reader)
        new_gem_grid = list(reader)
    return new_gem_grid

if __name__ == '__main__':
    get_new_gem_grid()