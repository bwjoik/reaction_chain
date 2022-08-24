import os
import sys
import jieba
import codecs
import math
import jieba.posseg as pseg
jieba.enable_paddle()

dict_path = "D:/OneDrive - 東吳大學/python/practice/sigodo/dict.txt"
fact_path = "D:/OneDrive - 東吳大學/python/practice/sigodo/fact.txt"
node_path = "D:/OneDrive - 東吳大學/python/practice/sigodo/node.txt"
edge_path = "D:/OneDrive - 東吳大學/python/practice/sigodo/edge.txt"
names = {}
relationships = {}
lineNames = []

jieba.load_userdict(dict_path)

with open(fact_path, "r", encoding='utf-8-sig') as f:
    for line in f.readlines():
        poss = pseg.lcut(line, use_paddle=True)
        lineNames.append([])
        for w in poss:
            if w.flag == "nr" or w.flag == "PER":
                lineNames[-1].append(w.word)
                if names.get(w.word) is None:
                    names[w.word] = 0
                    relationships[w.word] = {}
                names[w.word] += 1


# for line in lineNames:
#     for name1 in line:
#         for name2 in line:
#             if name1 == name2:
#                 continue
#             if relationships[name1].get(name2) is None:
#                 relationships[name1][name2] = 1
#             else:
#                 relationships[name1][name2] = relationships[name1][name2] + 1

# with open(node_path, "w", encoding="utf-8-sig") as f:
#     f.write("Id Label Weight\r\n")
#     for name, times in names.items():
#         f.write(name + " " + name + " " + str(times) + "\r\n")
# with open(edge_path, "w", encoding="utf-8-sig") as f:
#     f.write("Source Target Weight\r\n")
#     for name, edges in relationships.items():
#         for v, w in edges.items():
#             if w > 3:
#                 f.write(name + " " + v + " " + str(w) + "\r\n")
