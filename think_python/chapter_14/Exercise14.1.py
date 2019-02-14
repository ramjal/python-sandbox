import os

def sed(pat, rep, fname1, fname2):
    try:        
        f1 = open(fname1, 'r')
        f2 = open(fname2, 'w')

        for line in f1:
            print(line, end='')
            f2.write(line.replace(pat, rep))
                    
    except Exception as e:
        print('An error happened: '+ str(e))

    finally:  
        f1.close()
        f2.close()

sed('line', 'newline', 'chapter_14\\test1.txt', 'chapter_14\\test2.txt')
