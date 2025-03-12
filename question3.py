import math


class node:

    def __init__(self, x:int,y:int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def dist(self, q):
        return math.sqrt((self.x - q.x) **2 + (self.y - q.y) **2)

    def closest_pair_classic(self:list,lst_x:list, lst_y:list):
        dist = math.inf
        n = len(lst_x)
        p, q = 0, 1
        for i in range(n):
            for j in range(i+1,n):
                new_dist = self[i].dist(self[j])
                if new_dist < dist:
                    p = self[i]
                    q = self[j]
                    dist = new_dist
        return p, q, dist




