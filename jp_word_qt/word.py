import re
import os
# 提问单词的yaml文件模板
yaml_str = '''
  {count}:
    假名: {kana}
    日本字: {japan}
    汉译: {china}
'''


# 匹配单词类型
type_pattern = re.compile(r'(［.*］)')


# 作成单词列表
def make_word_list(fileline, word_dict, word_type):
    '''
        作成单词列表
        params
          fileline: 单词源文件中的每一行单词
          word_dict: 要写入的对应字典
          word_type: 单词类型
        return
          first_list: 单词源文件中的每一行单词以空格分割后的列表
          second_list: 假名和日本字列表
          japan: 日本字
    '''
    # 在当前字典中追加单词类型，只需追加一次
    if 'type' not in word_dict:
        word_dict['type'] = word_type
    # 第一次按照空格分隔源文件中的单词
    first_list = fileline.split(' ')
    # 第二次拆分假名和日本字
    second_list = first_list[0].split('（')
    # 长度等于2表示当前单词有日本字
    if len(second_list) == 2:
        japan = second_list[1][:-1]
    else:
        japan = ''
    return first_list, second_list, japan


# 设定单词
def set_word(count, word_list1, word_list2, japan, word_dict):
    word_dict[count] = {'假名': word_list2[0], '日本字': japan if japan else word_list2[0], '汉译': word_list1[-1][:-1]}


# 作成单词字典
def make_word_dict(file_path):
    # 初始化单词下标
    count = 0
    # 读取对应源文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            # 跳过空行
            if i == '\n':
                continue
            word_list1 = []
            word_list2 = []
            japan = ''
            # 正则匹配单词类型
            if re.search(type_pattern, i):
                # 取得单词类型
                word_type = re.search(type_pattern, i).group(1)[1:-1]
                # 判断当前单词类型是否时副词
                if word_type == '副':
                    word_list1, word_list2, japan = make_word_list(i, adverb_dict, '副词')
                    set_word(count, word_list1, word_list2, japan, adverb_dict)
                # 判断当前单词类型是否是动词
                elif word_type.startswith('动'):
                    word_list1, word_list2, japan = make_word_list(i, verbs_dict, '动词')
                    set_word(count, word_list1, word_list2, japan, verbs_dict)
                # 判断当前单词类型是否是形容词
                elif word_type.startswith('形'):
                    word_list1, word_list2, japan = make_word_list(i, adjective_dict, '形容词')
                    set_word(count, word_list1, word_list2, japan, adjective_dict)
                # 上述以外单词都记为名词
                else:
                    word_list1, word_list2, japan = make_word_list(i, noun_dict, '名词')
                    set_word(count, word_list1, word_list2, japan, noun_dict)
            # 没有类型的单词为短语
            else:
                word_list1, word_list2, japan = make_word_list(i, phrase_dict, '短语')
                set_word(count, word_list1, word_list2, japan, phrase_dict)
            count += 1


def make_yaml(word_dict, file_name):
    '''
        作成yaml文件
        params
          word_dict: 对应单词字典
          file_name: 文件名
        注意：做成单词需要更改对应的书册目录. 例：初上
    '''
    with open(f'./question_word/初下/{file_name}.yaml', 'a', encoding='utf-8', newline='') as yaml_file:
        for key in word_dict.keys():
            # 第一步先写入单词类型
            if key == 'type':
                yaml_file.write(f"{word_dict['type']}:")
                continue
            # 对单词进行按照yaml_str格式进行fromat
            new_str = yaml_str.format(count=key, kana=word_dict[key]['假名'], japan=word_dict[key]['日本字'], china=word_dict[key]['汉译'])
            # 写入格式化后的单词
            yaml_file.write(new_str)


if __name__ == '__main__':
    # 遍历目录中的文件
    for root, _, files in os.walk('./word_source/初下'):
        for file in files:
            # 取得不带后缀的文件名
            file_name = file.split('.')[0]
            # 取得文件全路径
            file_path = os.path.join(root, file)
            # 名词字典
            noun_dict = {}
            # 副词
            adverb_dict = {}
            # 动词
            verbs_dict = {}
            # 形容词
            adjective_dict = {}
            # 短语
            phrase_dict = {}
            # 调用单词字典作成方法
            make_word_dict(file_path)
            # 字典存在则写入对应单词
            if noun_dict:
                make_yaml(noun_dict, file_name)
            if verbs_dict:
                make_yaml(verbs_dict, file_name)
            if adjective_dict:
                make_yaml(adjective_dict, file_name)
            if adverb_dict:
                make_yaml(adverb_dict, file_name)
            if phrase_dict:
                make_yaml(phrase_dict, file_name)
