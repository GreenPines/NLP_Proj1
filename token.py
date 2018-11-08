# -*- coding: utf-8 -*-
# 读入字典


def load_Dict():
    Dict = {}
    with open("dic_ec.txt", 'r', encoding='UTF-8') as dict_file:
        lines = dict_file.readlines()
        for line in lines:
            sp = line.strip().split(' ')
    # print(sp[0])
            ll = len(sp)
            for i in range(2, ll):
                sp[1] = sp[1] + ' ' + sp[i]
            Dict[sp[0]] = sp[1]

    return Dict

# 读入不规则动词列表


def load_IrVerb():
    file_dict = open('irregular verbs.txt', 'rb')
    Dict = {}
    for line in file_dict.readlines():
        lineVec = str(line).replace('\\r\\n', '').split('\\t')
        for word in lineVec[1:-1]:
            Dict[str(word)] = str(lineVec[0]).replace("b'", '')
    return Dict

# 读入不规则名词列表


def load_IrNoun():
    file_dict = open('irregular verbs.txt', 'rb')
    Dict = {}
    for line in file_dict.readlines():
        lineVec = str(line).replace('\\r\\n', '').split('\\t')
        for word in lineVec[1:-1]:
            Dict[str(word)] = str(lineVec[0]).replace("b'", '')
    return Dict


def is_Exsit(new_word, Dict):
    # print("is_Exsit")
    # print(new_word)
    # print(Dict)
    if new_word in Dict.keys():
        #print("单词原型:" + new_word + '\t' + Dict[new_word])
        return True
    else:
        return False


def is_Verb(test_word, Dict):
    wd = test_word
    ll = len(wd)
    if 'ies' == wd[-3:ll]:
        nwd = wd[0:-3] + 'y'
        if is_Exsit(nwd, Dict):
            return nwd

    if 'es' == wd[-2:ll]:
        nwd = wd[0:-2]
        if is_Exsit(nwd, Dict):
            return nwd

    if 's' == wd[-1:ll]:
        nwd = wd[0:-1]
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ing' == wd[-3:ll] and wd[-4] == wd[-5]:
        nwd = wd[0:-4]
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ying' == wd[-4:ll]:
        nwd = wd[0:-4] + 'ie'
        if is_Exsit(nwd, Dict):
            print(23333)
            return nwd

    if 'ing' == wd[-3:ll]:
        nwd = wd[0:-3]
        if is_Exsit(nwd, Dict):
            return nwd
        nwd = nwd + 'e'
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ed' == wd[-2:ll] and wd[-3] == wd[-4]:
        nwd = wd[0:-2] + wd[-3]
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ied' == wd[-3:ll]:
        nwd = wd[0:-3] + 'y'
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ed' == wd[-2:ll]:
        nwd = wd[0:-2]
        if is_Exsit(nwd, Dict):
            return nwd
        nwd = wd[0:-2] + 'e'
        if is_Exsit(nwd, Dict):
            return nwd

    else:
        return None


def is_Noun(test_word, Dict):
    wd = test_word
    ll = len(test_word)

    if 'ves' == wd[-3:ll]:
        nwd = wd[0:-3] + 'f'
        if is_Exsit(nwd, Dict):
            return nwd
        nwd = wd[0:-3] + 'fe'
        if is_Exsit(nwd, Dict):
            return nwd

    if 'ies' == wd[-3:ll]:
        nwd = wd[0:-3] + 'y'
        if is_Exsit(nwd, Dict):
            return nwd

    if 'es' == wd[-2:ll]:
        nwd = wd[0:-2]
        if is_Exsit(nwd, Dict):
            return nwd

    if 's' == wd[-1]:
        nwd = wd[0:-1]
        if is_Exsit(nwd, Dict):
            return nwd

    else:
        return None


def main():
    irVerbDict = load_IrVerb()
    irNounDict = load_IrNoun()
    wordDict = load_Dict()
    # print(wordDict)
    # print(irVerbDict)
    # print(irNounDict)

    flag = False
    test_word = input("请输入单词：")
    if test_word in wordDict.keys():
        print("词典中已存在这个单词")
        print(wordDict[test_word])
        flag = True

        origin_word = is_Verb(test_word, wordDict)
        print(origin_word)
        if origin_word != None:
            print("存在单词原型:" + origin_word + "\n" +
                  "单词词意:" + wordDict[origin_word])
        origin_word = is_Noun(test_word, wordDict)
        if origin_word != None:
            print("存在单词原型:" + origin_word + "\n" +
                  "单词词意:" + wordDict[origin_word])
        if test_word in irVerbDict.keys():
            print("这个单词可以是不规则动词，原型是:" + irVerbDict[test_word] + '\n'
                  + "单词词意:" + wordDict[irVerbDict[test_word]])
        if test_word in irNounDict.keys():
            print("这个单词可以是不规则名词，原型是:" + irNounDict[test_word] + '\n'
                  + "单词词意:" + wordDict[irNounDict[test_word]])

    if flag == False:
        origin_word = is_Verb(test_word, wordDict)
        print(origin_word)
        if origin_word != None:
            print("单词原型:" + origin_word + "\n" +
                  "单词词意:" + wordDict[origin_word])
            flag = True
        origin_word = is_Noun(test_word, wordDict)
        if origin_word != None and flag == False:
            print("单词原型:" + origin_word + "\n" +
                  "单词词意:" + wordDict[origin_word])
            flag = True

    if flag == False:
        if test_word in irVerbDict.keys():
            print("是不规则动词，原型是:" + irVerbDict[test_word] + '\n'
                  + "单词词意:" + wordDict[irVerbDict[test_word]])
            flag = True
        if flag == False and test_word in irNounDict.keys():
            print("是不规则名词，原型是:" + irNounDict[test_word] + '\n'
                  + "单词词意:" + wordDict[irNounDict[test_word]])
            flag = True
    if flag == False:
        print("未找到该单词或该单词原型")


if __name__ == '__main__':
    while True:
        main()
