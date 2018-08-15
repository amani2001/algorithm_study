# coding: utf-8
# author: amani2001

# 最短路径算法，Dijkstra算法, 也是典型的贪心算法
import numpy as np
from queue import LifoQueue  # 导入栈，后进先出队列

INF = int(np.e**20)


class Dijkstra:
    def __init__(self,n):
        # 初始化全为无穷大的邻接矩阵
        self.matrix = np.array([[INF]*n for i in range(n)],"\n")
        self.__dist = []    # 到各节点的距离数组
        self.__pre_node = [-1] * n   # 初始化前驱节点数组
        self.__flag =[False] * n  # 设置初始标志数组，用于判断该顶点是否加入到集合中，false表示未加入
        self.n = n

    def generate_matrix(self, edge):
        # 随机生成路线和权值
        for i in range(edge+1):
            u = np.random.randint(0, self.n)
            v = np.random.randint(0, self.n)
            w = np.random.randint(1, 30)
            if u != v:
                self.matrix[u,v] = w

    def generate_source_dist(self,p):
        # 根据邻接矩阵，生成当前节点到各节点的距离，其前驱节点
        self.__dist = self.matrix[p - 1].copy()  # python中列表直接赋值使用是引用方式，共享空间，要想复制副本，则使用copy方法
        for i in range(self.n):
            if self.__dist[i] != INF:
                self.__pre_node[i] = p
        self.__dist[p - 1] = 0
        self.__flag[p - 1] = True
        # print(self.__dist)
        # print(self.__pre_node)

    def get_shortest_dist(self, p):
        # 生成顶点p到各顶点的最短路径及最小距离值
        for i in range(self.n):
            temp = INF
            t = p - 1
            for j in range(self.n):
                if self.__flag[j] == False and self.__dist[j] < temp:
                    t = j
                    temp = self.__dist[j]
            if t == p:
                return
            self.__flag[t] = True
            for j in range(self.n):
                if self.__flag[j] == False and self.matrix[t,j] < INF:
                    if self.__dist[j] > self.__dist[t] + self.matrix[t, j]:
                        self.__dist[j] = self.__dist[t] + self.matrix[t, j]
                        self.__pre_node[j] = t + 1

    def get_path(self, p):
        # 使用堆栈 实现路径输出
        stack = LifoQueue()
        print("源点为：{}".format(p))
        for i in range(self.n):
            temp = self.__pre_node[i]
            s = ''
            while temp != -1:
                stack.put(temp)
                temp = self.__pre_node[temp - 1]
            while not stack.empty():
                s += "{}--".format(stack.get())
            if self.__dist[i] != INF:
                print("源点{}到结点{}的路径为：{}，距离为：{}".format(p,str(i+1),(s + str(i+1)),self.__dist[i]))
            else:
                print("源点{}到结点{}的无路可行".format(p,str(i+1)))

    def run(self, edge, p):
        self.generate_matrix(edge)
        self.generate_source_dist(p)
        print(self.matrix)
        print("-"*self.n*10)
        self.get_shortest_dist(p)
        self.get_path(p)


if __name__ == '__main__':

    n = input("输入图中顶点个数:")
    dijkstra = Dijkstra(int(n))
    e = input("输入图中的路线数：")   # 取值不大于 n*(n-1)
    p = input("输入你所在的顶点位置：")  # 取值不大于 (n-1)
    dijkstra.run(int(e), int(p))

