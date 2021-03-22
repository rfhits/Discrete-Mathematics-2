# _*_coding:utf-8_*_

import graph.graph as gt
import sys

# 动态添加test_package文件夹的路径，为了能让此文件夹下的
# 自定义包成功的导入
# 要根据你自己的实际包的模块来决定路径。
sys.path.append('/graph')


V = {'a', 'c', 'b', 'd', 'e'}
E = {('b', 'c'), ('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e'), ('b', 'e'),
     ('d', 'e')}
Vs = {'a', 'c', 'b', 'd', 'e'}
Es = {('b', 'c'), ('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e'), ('b', 'e'),
      ('d', 'e')}
tv = gt.is_subgraph(V, E, Vs, Es)
print(tv)
