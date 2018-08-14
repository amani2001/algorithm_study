# coding: utf-8
# author: amani2001

# 钟点秘书
import random


# 定义秘书类
class Secretary:
    def __init__(self,name):
        '''
        初始化秘书
        :param name:
        '''
        self.__name = name
        self.meeting_list = []

    def init_meetings(self, meeting_count, day_start_time, day_end_time):
        '''
        初始化承接会议信息
        :param meeting_count: 需安排的会议数量
        :param day_start_time: 会议最早开始时间
        :param day_end_time: 会议最晚结束时间
        :return:
        '''
        for i in range(1, meeting_count + 1):
            # 随机生成某个会议的开始和结束时间
            start_time = random.randint(day_start_time, day_end_time - 1)
            end_time = random.randint(start_time + 1, day_end_time)
            # 创建一个会议对象
            meeting = Meeting(i, start_time, end_time)
            self.meeting_list.append(meeting)
        # 输出待安排的会议信息
        for m in self.meeting_list:
            print(m)

    def arrange_meeting(self):
        # print(self.meeting_list)
        # 对待安排的会议按结束时间升序排序
        temp_meeting_list = sorted(self.meeting_list,key=lambda x:x.end_time)
        # 至少安排一场会议
        count = 1
        # 将第一场会议的结束时间，设为标志量
        last = temp_meeting_list[0].end_time
        # 创建最终会议列表
        arr_meeting_list=[]
        arr_meeting_list.append(temp_meeting_list[0])
        # 根据贪心算法将当前会议开始时间大于上一次会议结束时间的添加到最终会议列表
        for m in temp_meeting_list:
            if m.start_time >= last:
                last = m.end_time
                arr_meeting_list.append(m)
        return arr_meeting_list, len(arr_meeting_list)

    def get_name(self):
        '''
        获取秘书的姓名
        :return:
        '''
        return self.__name


class Meeting:
    def __init__(self,number,start_time,end_time):
        '''
        构建一次会议
        :param number:
        :param start_time:
        :param end_time:
        '''
        self.__number = number
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        '''
        重写对象的print方法
        :return:
        '''
        return "会议编号:{},会议开始时间:{},会议结束时间:{}".format(self.__number,self.start_time,self.end_time)


if __name__ == '__main__':
    secretary = Secretary('lina')
    meeting_count= input("请输入待安排的会议场次:")
    day_start_time = input("请输入会议最早开始时间:")
    day_end_time = input("请输入会议最迟结束时间:")

    # 秘书初始化会议
    secretary.init_meetings(int(meeting_count),int(day_start_time),int(day_end_time))
    # secretary.init_meetings(5,8,20)

    # 秘书安排会议
    arrange_meeting_list, count = secretary.arrange_meeting()
    # 输出安排好的会议信息
    print("钟点秘书{}，共安排的会议场次数为：{},具体信息如下".format(secretary.get_name(), count))
    print("-"*20)
    for m in arrange_meeting_list:
        print(m)