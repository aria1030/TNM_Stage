def ect_tnm(t,n,m):
    if m == 'm1':
        print('分期结果：\t ⅣB 期')

    elif t == 'tis' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0 期')

    elif ((t == 't1a' and n == 'n0' and m =='m0')
        or(t == 't1b' and n == 'n0' and m =='m0')
        or (t == 't1a' and n == 'n1' and m == 'm0')
        or (t == 't1b' and n == 'n1' and m == 'm0')):
        print('分期结果：\t Ⅰ 期')

    elif ((t == 't2' and n == 'n0' and m == 'm0')
          or (t == 't2' and n == 'n1' and m == 'm0')
          or (t == 't3' and n == 'n0' and m == 'm0')):
        print('分期结果：\t Ⅱ 期')

    elif ((t == 't1a' and n == 'n2' and m == 'm0')
          or (t == 't1b' and n == 'n2' and m == 'm0')
          or (t == 't2' and n == 'n2' and m == 'm0')
          or (t == 't3' and n == 'n1' and m == 'm0')
          or (t == 't3' and n == 'n2' and m == 'm0')):
        print('分期结果：\t Ⅲ 期')

    else:
        print('分期结果：\t ⅣA 期')
