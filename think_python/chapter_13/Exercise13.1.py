import string
import collections

def cleanup(str2clean):
    for ch in string.punctuation:
        str2clean = str2clean.replace(ch, '')
    return str2clean


# the same as above but using str.translate
def cleanup2(str2clean):
    tran = str.maketrans('', '', string.punctuation + '”“’‘')
    return str2clean.translate(tran)


def add_to_dict(wdict, line):
    wordCount = 0
    for w in line.split(' '):
        if w is not '':
            wdict[w] = wdict.get(w, 0) + 1
            wordCount += 1
    return wordCount


def main():
    try: 
        fileR = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\Idiot.txt', encoding="UTF-8")
        word_dict = dict()
        lineCount = 0
        wordCount = 0
        for line in fileR:
            l = cleanup2(line.strip().lower())
            # if lineCount > 100:
            #     break
            lineCount += 1
            wordCount += add_to_dict(word_dict, l)

        print('Lines:', lineCount)
        print('Words:', wordCount)
        print('--------')

        fileW = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\Idiot-words.txt', 'w')
        
        # Prints the word_dict
        # for pair in word_dict:
        #     s = '%s: %d' % (pair, word_dict[pair])
        #     print(s)
        #     fileW.writelines(s + '\n')

        # Sorts the word_dict by value descending
        # sorted_by_value = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)
        # for sbv in sorted_by_value:
        #     print(sbv)

        # Sorts the word_dict by value descending
        sortedbyvalue = collections.Counter(word_dict)
        for s in sortedbyvalue.most_common(20):
            print(s)
            
        # Prints the top most common repeated words
        res_list = [x[0] for x in sortedbyvalue.most_common(20)]
        print('\n'.join(res_list))

    except Exception as e:
        print('An error happened: '+ str(e))

    finally:  
        fileR.close()
        fileW.close()


if __name__ == '__main__':
    main()