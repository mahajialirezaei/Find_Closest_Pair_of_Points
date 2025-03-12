import math


class Node:

    def __init__(self, x:int,y:int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def dist(self, q):
        return math.sqrt((self.x - q.x) **2 + (self.y - q.y) **2)

    @staticmethod
    def closest_pair_classic(lst_x: list):
        dist = math.inf
        p, q = None, None
        n = len(lst_x)
        for i in range(n):
            for j in range(i + 1, n):
                new_dist = lst_x[i].dist(lst_x[j])
                if new_dist < dist:
                    p = lst_x[i]
                    q = lst_x[j]
                    dist = new_dist
        return p, q, dist

    @staticmethod
    def closest_pair(lst_x: list, lst_y: list):
        n = len(lst_x)
        if n < 2:
            print("At least n should be 2")
            return None, None, math.inf

        if n == 2:
            return lst_x[0], lst_x[1], lst_x[0].dist(lst_x[1])

        if n == 3:
            return Node.closest_pair_classic(lst_x)

        mid = lst_x[n // 2]
        lst_x_left = lst_x[:n // 2]
        lst_x_right = lst_x[n // 2:]
        lst_y_left = [point for point in lst_y if point.x <= mid.x]
        lst_y_right = [point for point in lst_y if point.x > mid.x]

        p_left, q_left, delta_left = Node.closest_pair(lst_x_left, lst_y_left)
        p_right, q_right, delta_right = Node.closest_pair(lst_x_right, lst_y_right)

        if delta_left < delta_right:
            p, q, delta = p_left, q_left, delta_left
        else:
            p, q, delta = p_right, q_right, delta_right

        doubted_points = [point for point in lst_y if mid.x - delta < point.x < mid.x + delta]

        for i in range(len(doubted_points)):
            for j in range(i + 1, min(i + 7, len(doubted_points))):
                delta_p = doubted_points[i].dist(doubted_points[j])
                if delta_p < delta:
                    p, q, delta = doubted_points[i], doubted_points[j], delta_p

        return p, q, delta



n = int(input())
lst = []
for i in range(n):
    x, y = map(int ,input().split(' '))
    lst.append(Node(x,y))

lst_x = sorted(lst, key = lambda p : p.x)
lst_y = sorted(lst, key = lambda p : p.y)

p, q, distance = Node.closest_pair(lst_x, lst_y)

print(p, q, distance)





