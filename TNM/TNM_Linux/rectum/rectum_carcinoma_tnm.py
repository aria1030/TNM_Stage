def rct_tnm(t,n,m):
    if m == 'm1a':
        print('分期结果：\t ⅣA 期')

    elif m == 'm1b':
        print('分期结果：\t ⅣB 期')

    elif m == 'm1c':
        print('分期结果：\t ⅣC 期')

    elif t == 'tis' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0 期')

    elif ((t == 't1' and n == 'n0' and m == 'm0')
         or (t == 't2' and n == 'n0' and m =='m0')):
        print('分期结果：\t Ⅰ 期')

    elif t == 't3' and n == 'n0' and m == 'm0':
        print('分期结果：\t ⅡA 期')

    elif t == 't4a' and n == 'n0' and m == 'm0':
        print('分期结果：\t ⅡB 期')

    elif t == 't4b' and n == 'n0' and m == 'm0':
        print('分期结果：\t ⅡC 期')

    elif ((t == 't1' and n == 'n1a' and m == 'm0')
          or (t == 't1' and n == 'n1b' and m == 'm0')
          or (t == 't1' and n == 'n1c' and m == 'm0')
          or (t == 't1' and n == 'n2a' and m == 'm0')):
        print('分期结果：\t ⅢA 期')

    elif ((t == 't4a' and n == 'n2a' and m == 'm0')
          or (t == 't3' and n == 'n2b' and m == 'm0')
          or (t == 't4a' and n == 'n2b' and m == 'm0')
          or (t == 't4b' and n == 'n1a' and m == 'm0')
          or (t == 't4b' and n == 'n1b' and m == 'm0')
          or (t == 't4b' and n == 'n1c' and m == 'm0')
          or (t == 't4b' and n == 'n2a' and m == 'm0')
          or (t == 't4b' and n == 'n2b' and m == 'm0')):
        print('分期结果：\t ⅢC 期')

    else:
        print('分期结果：\t ⅢB 期')
