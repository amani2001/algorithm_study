# coding: utf-8
# author: amani2001
# 背包问题初步入门，最优装载问题
import random


class Knapsack:
    def __init__(self):
        self.weight = input("请输入背包最大的装载量:")

    def get_best_loads(self, goods_list):
        goods_list.sort()
        accumulate = 0
        count = 0
        print(goods_list)
        for goods in goods_list:
            accumulate += goods
            if accumulate <= int(self.weight):
                count += 1
            else:
                accumulate -= goods
                break
        return accumulate, count

if __name__ == '__main__':
    knapsack = Knapsack()

    number = input("输入货物的数量: ")
    # 随机生成每件商品重量，每件商品的重量介于1-20之间
    goods_list = [random.randint(1,20) for i in range(0, int(number))]
    print("物品重量列表：{}".format(goods_list))
    accumulate, count = knapsack.get_best_loads(goods_list)
    print("装了{}件物品，共重{}".format(count, accumulate))

