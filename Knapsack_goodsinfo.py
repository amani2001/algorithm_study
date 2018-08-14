# coding: utf-8
# author: amani2001
# 背包问题初步入门，最优装载问题，显示被装的物品信息
import random


class Knapsack:
    def __init__(self):
        self.weight = input("请输入背包最大的装载量:")

    def get_best_loads(self, goods_list):
        accumulate = 0
        count = 0
        # 对列表中字典按weigth列进行升序排列
        goods_number_list.sort(key=lambda x: x.get('weight'), reverse=False)
        # 用于保存装载了的物品对象
        loads_goods =[]
        for goods in goods_list:
            accumulate += goods['weight']
            if accumulate <= int(self.weight):
                count += 1
                loads_goods.append(goods)
            else:
                accumulate -= goods["weight"]
                break
        return loads_goods, accumulate, count


if __name__ == '__main__':
    knapsack = Knapsack()

    number = input("输入货物的数量: ")
    # 随机生成每件商品重量，每件商品的重量介于1-20之间
    goods_list = [random.randint(1,20) for i in range(0, int(number))]
    goods_number_list = []
    number = 1001
    for g in goods_list:
        item = {
            "num": str(number),
            "weight":g}
        goods_number_list.append(item)
        number += 1

    print("物品重量列表：{}".format(goods_number_list))
    load_goods, accumulate, count = knapsack.get_best_loads(goods_number_list)
    print("装了{}件物品，共重{}".format(count, accumulate))
    print("装入的商品列表为：{}".format(load_goods))

