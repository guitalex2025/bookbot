import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def wordcount(filepath):
    words = get_book_text(filepath)
    separate = words.split()
    howmany = len(separate)
    print(f"Found {howmany} total words")
    return separate


def lettercount(separate):
    separate_string = str(separate)
    lowercase = separate_string.lower()
    result={}
    for character in lowercase:
        if character not in result and character.isalpha():
            result[character]=0
        else:
            continue

            

    #result={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for word in lowercase:
        spelling = word.split()
        # print(spelling)
        for character in spelling:
            if character.isalpha():
                    result[character] += 1
    return result





    