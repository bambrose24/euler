import inflect
import string

def main():
    p = inflect.engine()
    s = set(string.ascii_lowercase)
    count = 0
    for i in range(1,1001):
        res = p.number_to_words(i)
        res = res.lower()
        for l in res:
            if l in s:
                count+=1
    print(count)


if __name__ == '__main__':
    main()
