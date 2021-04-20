# 数据集来自kaggle公开数据集
#0+ ！/usr/bin/python3
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
# us_file_path = "D:\qq文件\377577275\FileRecv\day56 (1)\youtube_video_data/US_video_data_numbers.csv  "

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
# 这里就是 unpack是否为 true
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")
# 读入和转置读入对比
print(t1)
print("*"*100)
print(t2)
print("*"*100)
# 切片读入
b = t2[2:5,1:4]
print(b)

t_us=t2
# 取评论的数据
# -1是最后一行 也即是评论
t_us_comments = t_us[:,-1]
print(t_us.shape)
# 怎么知道分多少，打印最大和最小值
# 之后会发现数据大于5000的极其少 所以数据绝大部分集中在5000一下，所以过滤
t_us_comments = t_us_comments[t_us_comments<=5000]

print(t_us_comments.max(),t_us_comments.min())
# 50是试验后得出 初始可随机一个数
d=50
# 条形图组距
bin_nums = (t_us_comments.max()-t_us_comments.min())//d

# 绘图 设置画布
plt.figure(figsize=(20,8),dpi=80)
# hist是条形图函数
plt.hist(t_us_comments,bin_nums)

# just show
plt.show()