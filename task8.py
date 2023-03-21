def main():
    s = [i for i in range(int(input('dlina massiva ')))]
    print(select(int(input('function ')), s))

def select(a, s):
    if a == 0:
        return len(s)
    elif a == 1:
        x = int(input('dop chislo '))
        return x in s
    elif a == 2:
        x = int(input('dop chislo '))
        return not x in s
    elif a == 3:
        s1 = int(input('dop chislo '))
        return s + s1
    elif a == 4:
        i = int(input('dop chislo '))
        return s[i]
    elif a == 5:
        i = int(input('dop chislo '))
        j = int(input('dop chislo '))
        d = int(input('dop chislo '))
        return s[i:j:d]
    elif a == 6:
        return min(s)
    elif a == 7:
        return max(s)
    elif a == 8:
        i = int(input('dop chislo '))
        x = int(input('dop chislo '))
        s[i] = x
        return s
    elif a == 9:
        i = int(input('dop chislo '))
        j = int(input('dop chislo '))
        d = int(input('dop chislo '))
        t = int(input('dop chislo '))
        s[i:j:d] = t
        return s
    elif a == 10:
        i = int(input('dop chislo '))
        j = int(input('dop chislo '))
        d = int(input('dop chislo '))
        del s[i:j:d]
        return s
    elif a == 11:
        x = int(input('dop chislo '))
        s.append(x)
        return s
    elif a == 12:
        x = int(input('dop chislo '))
        return s.count(x)
    elif a == 13:
        b = [int(input('dop chislo ')) for i in range(int(input('Введите длину последовательности: ')))]
        s = s.extend(b)
        return s
    elif a == 14:
        x = int(input('dop chislo '))
        return s.index(x)
    elif a == 15:
        i = int(input('dop chislo '))
        x = int(input('dop chislo '))
        s.insert(i,x)
        return s
    elif a == 16:
        i = int(input('dop chislo '))
        s.pop(i)
        return s
    elif a == 17:
        s.reverse()
        return s
    elif a == 18:
        return 

if __name__ == '__main__':
    main()