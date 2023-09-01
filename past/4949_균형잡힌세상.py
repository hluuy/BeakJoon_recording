while True:
    STR = input()
    if STR == '.':
        break

    lst = []
    if STR == '.':
        break
    for i in STR:
        if i in '(){}[]':
            lst.append(i)
            if len(lst) > 1:
                if (lst[-1] == ')' and lst[-2] == '(') or (lst[-1] == '}' and lst[-2] == '{') or (lst[-1] == ']' and lst[-2] == '['):
                    lst.pop()
                    lst.pop()

    if len(lst) > 0:
        print('no')
    else:
        print('yes')
