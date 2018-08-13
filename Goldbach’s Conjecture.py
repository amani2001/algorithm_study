# coding: utf-8
# author: amani2001
# 哥德巴赫猜想
# 2000以下任意大于2的偶数都可以分解成两个素数之和
import math

# 方法2 中 定义全局数组 以增加空间来减少时间复杂度
n_list = []

def isprime(n):
    '''
    判断n是否为素数
    :param n:
    :return:
    '''
    if n <= 1:
        return 0;
    if n == 2:
        return 1;
    k = int(math.sqrt(n)) + 1
    for i in range(2, k):
        if n % i == 0:
            return 0
    return 1

def get_list(n):
    '''
    生成长度为n的列表，用0和1分别表示该下标的数据是否为素数
    :param n:
    :return:
    '''
    global n_list
    n_list = [0] * (n+1)
    n_list[2] = 1
    for i in range(3,n+1,2):
        if isprime(i) == 1:
            n_list[i] = 1
    # print(n_list)

def method_1(n):
    for i in range(4, n+1, 2):
        for j in range(2, i):
            if isprime(j) == 1:
                if isprime(i-j) == 1:
                    print("{}={}+{}".format(i, j, i-j))
                    break;
        if i==j:
            print("error")

def method_2(n):
    '''
    直接读取列表中对应的数据是否为素数
    :param n:
    :return:
    '''
    global n_list
    # 初始化列表
    get_list(n)
    for i in range(4, n+1, 2):
        for j in range(2, i):
            if n_list[j] == 1:
                if n_list[i - j] == 1:
                    print("{}={}+{}".format(i, j, i - j))
                    break;
        if i == j:
            print("error")


def method_3(n):
    # 构造n以内的所有素数列表
    prime_list = [2]
    for i in range(3,n+1,2):
        if isprime(i):
            prime_list.append(i)
    for i in range(4, n+1, 2):
        for j in range(2, i):
            if j in prime_list:
                if i - j in prime_list:
                    print("{}={}+{}".format(i, j, i - j))
                    break;
        if i == j:
            print("error")

if __name__ == '__main__':
    # method_1(2000)
    # method_2(2000)
    method_3(2000)