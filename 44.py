import time as t

# class MyTimer:
#     def __init__(self):
#         self.unit = ['年','月','日','小时','分钟','秒']
#         self.borrow = [0, 12, 31, 24, 60, 60]
#         self.prompt = '未开始计时'
#         self.lasted = []
#         self.begin = 0
#         self.end = 0    
    
#     def __str__(self):
#         return self.prompt
    
#     __repr__ = __str__

#     def __add__(self,other):
#         prompt = "总共运行了"
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 prompt += (str(result[index]) + self.unit[index])
#         return prompt

#     def start(self):
#         self.begin =  t.localtime()
#         self.prompt = "提示:请先调用stop()停止计时"
#         print("计时开始。。。")
    
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用start()进行计时！")
#         else:
#             self.end = t.localtime()
#             self._calc()
#             print("计时结束！")
    
#     def _calc(self):
#         self.lasted = []
#         self.prompt = "总共运行了"
#         for index in range(6):
#             temp = self.end[index] - self.begin[index]
#             if temp < 0:
#                 i = 1
#                 while self.lasted[index - i] < 1:
#                     self.lasted[index-i] += self.borrow[index - i]  - 1
#                     self.lasted[index- i - 1] -= 1
#                     i += 1
#                 self.lasted.append(self.borrow[index] + temp)
#                 self.lasted[index - 1] -= 1
#             else:
#                 self.lasted.append(temp)
#         for index in range(6):
#             if self.lasted[index]:
#                 self.prompt += str(self.lasted[index]) + self.unit[index]

#         self.begin = 0
#         self.end = 0






# class MyTimer:
#     def __init__(self):
#         self.prompt = '未开始计时'
#         self.lasted = 0.0
#         self.begin = 0
#         self.end = 0    
#         self.default_timer = t.perf_counter
    
#     def __str__(self):
#         return self.prompt
    
#     __repr__ = __str__

#     def __add__(self,other):
#         result = self.lasted + other.lasted
#         prompt = "总共运行了 %0.2f 秒" % result
#         return prompt

#     def set_timer(self,timer):
#         if timer == 'process_time':
#             self.default_timer = t.process_time
#         elif timer == 'perf_counter':
#             self.default_timer = t.perf_counter
#         else:
#             print("输入无效，请输入 perf_counter 或 process_time")

#     def start(self):
#         self.begin =  self.default_timer()
#         self.prompt = "提示:请先调用stop()停止计时"
#         print("计时开始。。。")
    
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用start()进行计时！")
#         else:
#             self.end = self.default_timer()
#             self._calc()
#             print("计时结束！")
    
#     def _calc(self):
#         self.lasted = self.end - self.begin
#         self.prompt = "总共运行了 %0.2f 秒" % self.lasted

#         self.begin = 0
#         self.end = 0

#     def set_timer(self,timer):
#         if timer == "process_time":
#             self.default_timer = t.process_time
#         elif timer == "perf_counter":
#             self.default_timer = t.perf_counter
#         else:
#             print("输入无效，请输入 perf_counter 或 proce_time")



class MyTimer:
    def __init__(self,func,number = 1000000):
        self.prompt = '未开始计时'
        self.lasted = 0.0
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number
            
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__

    def __add__(self,other):
        result = self.lasted + other.lasted
        prompt = "总共运行了 %0.2f 秒" % result
        return prompt
    
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
            self.end = self.default_timer()
            self.lasted = self.end = self.begin
            self.prompt = "总共运行了 %0.2f 秒" %self.lasted

    
    def set_timer(self,timer):
        if timer == "process_time":
            self.default_timer = t.process_time
        elif timer == "perf_counter":
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 proce_time")



    