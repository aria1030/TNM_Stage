def bct_tnm(t,n,m):
    if m == 'm1b':
        print('分期结果：\t ⅣB 期')

    elif t == 't4b' or m == 'm1a':
        print('分期结果：\t ⅣA 期')

    elif t == 'ta' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0a 期')

    elif t == 'tis' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0is 期')

    elif (t == 't1a' and n == 'n0' and m =='m0'):
        print('分期结果：\t Ⅰ 期')

    elif ((t == 't2a' and n == 'n0' and m == 'm0')
          or (t == 't2b' and n == 'n0' and m == 'm0')):
        print('分期结果：\t Ⅱ 期')

    elif ((t == 't3a' and n == 'n0' and m == 'm0')
          or (t == 't3b' and n == 'n0' and m == 'm0')
          or (t == 't4a' and n == 'n0' and m == 'm0')
          or (t == 't1' and n == 'n1' and m == 'm0')
          or (t == 't2a' and n == 'n1' and m == 'm0')
          or (t == 't2b' and n == 'n1' and m == 'm0')
          or (t == 't3a' and n == 'n1' and m == 'm0')
          or (t == 't3b' and n == 'n1' and m == 'm0')
          or (t == 't4a' and n == 'n1' and m == 'm0')
    ):
        print('分期结果：\t ⅢA 期')

    else:
        print('分期结果：\t ⅢB 期')
