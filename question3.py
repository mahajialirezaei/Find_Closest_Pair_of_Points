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


    def closest_Pair(self:list, lst_x:list, lst_y:list):
        n= len(lst_x)
        if n==1:
            print("At least n should be 2")
        if n==2:
            return lst_x[0].dist(lst_x[1])

        if n==3:
            return self.closest_pair_classic(lst_x, lst_y)


        mid = lst_x[n//2]
        lst_x_left = lst_x[:n//2]
        lst_x_right = lst_x[n//2:]
        lst_y_left = lst_y.filter(lambda point : point.x < mid.x)
        lst_y_right = lst_y - lst_y_left

        p_left, q_left, delta_left = self.closest_Pair(lst_x_left, lst_y_left)
        p_right, q_right, delta_right = self.closest_Pair(lst_x_right, lst_y_right)
        p, q, delta = p_left, q_left, delta_left if delta_left < delta_right else delta_right

        doubted_points = [point for point in lst_y if mid.x - delta < point.x < mid.x + delta]

        for i in range(len(doubted_points)):
            for j in range(i+1,min(i+7, len(doubted_points))):
                delta_p = doubted_points[i].dist(doubted_points[j])
                if delta_p < delta:
                    p, q, delta = doubted_points[i], doubted_points[j], delta_p


        return p, q, delta








