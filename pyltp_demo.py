# from pyltp import SentenceSplitter
# # 分句
# doc = """据韩联社12月28日反映，美国防部发言人杰夫·莫莱尔27日表示，美国防部长盖茨将于2011年1月14日访问韩国。盖茨原计划从明年1月9日至14日陆续访问中国和日本，目前，他决定在行程中增加对韩国的访问。莫莱尔表示，盖茨在访韩期间将会晤韩国国防部长官金宽镇，就朝鲜近日的行动交换意见，同时商讨加强韩美两军同盟关系等问题，拟定共同应对朝鲜挑衅和核计划的方案。"""
# sents = SentenceSplitter.split(doc)  # 分句
# for sent in sents:
#     print(sent)


# # -*- coding: utf-8 -*-
# import os
# from pyltp import Segmentor
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# cws_model_path = root + 'cws.model'  # 分词模型路径，模型名称为`cws.model`
# lexicon_path = root + 'lexicon.txt'  # 参数lexicon是自定义词典的文件路径
# segmentor = Segmentor(cws_model_path, lexicon_path)
# sent = '据韩联社12月28日反映，美国防部发言人杰夫·莫莱尔27日表示，美国防部长盖茨将于2011年1月14日访问韩国。'
# words = segmentor.segment(sent)  # 分词
# print('/'.join(words))
# segmentor.release()





# '''词性标注结果说明
# https://ltp.readthedocs.io/zh_CN/latest/appendix.html#id3 '''
# from pyltp import Segmentor, Postagger
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# cws_model_path = root + 'cws.model'  # 分词模型路径，模型名称为`cws.model`
# lexicon_path = root + 'lexicon.txt'  # 参数lexicon是自定义词典的文件路径
# segmentor = Segmentor(cws_model_path, lexicon_path)
# sent = '据韩联社12月28日反映，美国防部发言人杰夫·莫莱尔27日表示，美国防部长盖茨将于2011年1月14日访问韩国。'
# words = segmentor.segment(sent)  # 分词
# # 词性标注
# pos_model_path = root + 'pos.model'  # 词性标注模型路径，模型名称为`pos.model`
# postagger = Postagger(pos_model_path)  # 初始化实例
# postags = postagger.postag(words)  # 词性标注
# for word, postag in zip(words, postags):
#     print(word, postag)
# # 释放模型
# segmentor.release()
# postagger.release()
#


# from pyltp import Segmentor, Postagger
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# pos_model_path = root + 'pos.model'  # 词性标注模型路径，模型名称为`pos.model`
# postagger = Postagger(pos_model_path)  # 初始化实例
# # 分词结果
# words = ['你', '会', '机器', '学习', '中', '的', '随机', '森林', '吗']
# words_1 = ['你', '会', '机器学习', '中', '的', '随机森林', '吗']
# postags = postagger.postag(words)
# postags_1 = postagger.postag(words_1)  # 词性标注
# print([(word,tag) for tag, word in zip(postags, words)])
# print([(word,tag) for tag, word in zip(postags_1, words_1)])
# postagger.release()  # 释放模型






# from pyltp import NamedEntityRecognizer
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# ner_model_path = root + 'ner.model'   # 命名实体识别模型路径，模型名称为`pos.model`
# recognizer = NamedEntityRecognizer(ner_model_path) # 命名实体识别
# words_4 = ['奥巴马','住','在','纽约']
# postags_4 = ['nh','v','r','ns']
# netags = recognizer.recognize(words_4, postags_4)
# print( '\t'.join(netags))
# recognizer.release()



# # -*- coding: utf-8 -*-
# # https://ltp.readthedocs.io/zh_CN/latest/appendix.html
# from pyltp import Segmentor, Postagger
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# cws_model_path = root + 'cws.model'  # 分词模型路径，模型名称为`cws.model`
# lexicon_path = root + 'lexicon.txt'  # 参数lexicon是自定义词典的文件路径
# segmentor = Segmentor(cws_model_path, lexicon_path)
# sent = '据韩联社12月28日反映，美国防部发言人杰夫·莫莱尔27日表示，美国防部长盖茨将于2011年1月14日访问韩国。'
# words = segmentor.segment(sent)  # 分词
# pos_model_path = root + 'pos.model'  # 词性标注模型路径，模型名称为`pos.model`
# postagger = Postagger(pos_model_path)  # 初始化实例
# postags = postagger.postag(words)  # 词性标注
# ner_model_path = root + 'ner.model'   # 命名实体识别模型路径，模型名称为`pos.model`
# from pyltp import NamedEntityRecognizer
# recognizer = NamedEntityRecognizer(ner_model_path) # 初始化实例
# netags = list(recognizer.recognize(words, postags))  # 命名实体识别
# print([(word,tag) for tag, word in zip(netags, words)])
#
# persons, places, orgs = set(), set(), set()
# i = 0
# for tag, word in zip(netags, words):
#     j = i
#     # 人名
#     if 'Nh' in tag:
#         if str(tag).startswith('S'):
#             persons.add(word)
#         elif str(tag).startswith('B'):
#             union_person = word
#             while netags[j] != 'E-Nh':
#                 j += 1
#                 if j < len(words):
#                     union_person += words[j]
#             persons.add(union_person)
#     # 地名
#     if 'Ns' in tag:
#         if str(tag).startswith('S'):
#             places.add(word)
#         elif str(tag).startswith('B'):
#             union_place = word
#             while netags[j] != 'E-Ns':
#                 j += 1
#                 if j < len(words):
#                     union_place += words[j]
#             places.add(union_place)
#     # 机构名
#     if 'Ni' in tag:
#         if str(tag).startswith('S'):
#             orgs.add(word)
#         elif str(tag).startswith('B'):
#             union_org = word
#             while netags[j] != 'E-Ni':
#                 j += 1
#                 if j < len(words):
#                     union_org += words[j]
#             orgs.add(union_org)
#     i += 1
#
# print('人名：', '，'.join(persons))
# print('地名：', '，'.join(places))
# print('组织机构：', '，'.join(orgs))
# # 释放模型
# segmentor.release()
# postagger.release()
# recognizer.release()
#








# from pyltp import Parser
# words_4 = ['奥巴马','住','在','纽约']
# postags_4 = ['nh','v','r','ns']
# # 依存句法分析
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# par_model_path = root + 'parser.model'  # 模型路径，模型名称为`parser.model`
# parser = Parser(par_model_path) # 初始化实例
# # 句法分析
# arcs = parser.parse(words_4, postags_4)
# print(arcs)
# """
# head 表示依存弧的父节点词的索引。ROOT节点的索引是0，第一个词开始的索引依次为1、2、3…。
# relation 表示依存弧的关系。
# 那么，2：SBV就表示当前词“奥巴马”和第二个词也就是“住”是主谓关系。
# """
# print("\t".join("%d:%s" % (head, relation) for head, relation in arcs))
# parser.release()


# import os
# from pyltp import Segmentor, Postagger, Parser
# # 分词
# root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
# cws_model_path = root + 'cws.model'  # 分词模型路径，模型名称为`cws.model`
# lexicon_path = root + 'lexicon.txt'  # 参数lexicon是自定义词典的文件路径
# segmentor = Segmentor(cws_model_path, lexicon_path)
# sent = '据韩联社12月28日反映，美国防部发言人杰夫·莫莱尔27日表示，美国防部长盖茨将于2011年1月14日访问韩国。'
# words = segmentor.segment(sent)  # 分词
#
# # 词性标注
# pos_model_path = root + 'pos.model'  # 词性标注模型路径，模型名称为`pos.model`
# postagger = Postagger(pos_model_path)  # 初始化实例
# postags = postagger.postag(words)  # 词性标注
#
# # 依存句法分析
# par_model_path = root + 'parser.model'  # 模型路径，模型名称为`parser.model`
# parser = Parser(par_model_path) # 初始化实例
# arcs = parser.parse(words, postags)  # 句法分析
# print(arcs)
# rely_id = [arc.head for arc in arcs]  # 提取依存父节点id
# relation = [arc.relation for arc in arcs]  # 提取依存关系
# heads = ['Root' if id == 0 else words[id-1] for id in rely_id]  # 匹配依存父节点词语
#
# for i in range(len(words)):
#     print(relation[i] + '(' + words[i] + ', ' + heads[i] + ')')
#
# # 释放模型
# segmentor.release()
# postagger.release()
# parser.release()






import os
from pyltp import SementicRoleLabeller,Parser
root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
words_4 = ['奥巴马','住','在','纽约']
postags_4 = ['nh','v','r','ns']
# 依存句法分析
root = "J:/XMIND_FILE/NLP/models/ltp-models/3.4.0/ltp_data_v3.4.0/"
par_model_path = os.path.join(root, 'parser.model')  # 模型路径，模型名称为`parser.model`
parser = Parser(par_model_path)
arcs = parser.parse(words_4, postags_4)
# 注意：对windows系统此处模型加载必须为pisrl_win.model，；下载地址。http://ltp.ai/download.html
# pisrl.model 如在windows系统下不可用，可以到 此链接 下载支持windows的语义角色标注模型。
srl_model_path = os.path.join(root, 'pisrl_win.model')
labeller = SementicRoleLabeller(srl_model_path)
roles = labeller.label(words_4, postags_4, arcs)  # 语义角色标注
print(roles)
"""
第一个词开始的索引依次为0、1、2…; 返回结果 roles 是关于多个谓词的语义角色分析的结果。由于一句话中可能不含有语义角色，所以结果可能为空。
[(index,[(name,(start,end))])]
index 代表谓词的索引;name 表示语义角色类型。
start 表示该语义角色起始词位置的索引。end 表示该语义角色结束词位置的索引。
"""
for index,role in roles:
    print(index, "".join(["%s:(%d~%d) \t" % (name, position[0], position[1]) for name,position in role]))
labeller.release()  # 释放模型



