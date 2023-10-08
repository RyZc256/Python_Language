import re
def get_word_list(line):
    regEx = re.compile('[\\W]')
    res = re.compile(r"[\u4e00-\u9fa5]")
    pl = regEx.split(line)
    str1_list = []
    for str in pl:
        if res.split(str) is None:
            str1_list.append(str)
        else:
            ret = res.split(str)
            for ch in ret:
                str1_list.append(ch)
    list_word1 = [ x for x in str1_list if len(x.strip()) > 0]
    return list_word1

def word_count(filename, word):
    word_count = 0
    with open(filename) as fp:
        for line in fp:
            key_words = get_word_list(line)
            for x in key_words:
                if x.lower() == word.lower():
                    word_count += 1
    return word_count

def main():
    word = input('请输入单词: ')
    print(word + ',在文件中出现'+str(word_count('password2.txt',word))+'次')

if __name__ == '__main__':
    main()