def gct_tnm(t,n,m):
    if m == 'm1':
        print('分期结果：\t Ⅳ 期')

    elif t == 'tis' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0 期')

    elif ((t == 't1a' and n == 'n0' and m =='m0')
        or(t == 't1b' and n == 'n0' and m =='m0')):
        print('分期结果：\t ⅠA 期')

    elif ((t == 't1a' and n == 'n1' and m =='m0')
        or (t == 't1b' and n == 'n1' and m =='m0')
        or (t == 't2' and n == 'n0' and m == 'm0')):
        print('分期结果：\t ⅠB 期')

    elif ((t == 't3' and n == 'n0' and m == 'm0')
          or (t == 't2' and n == 'n1' and m == 'm0')
          or (t == 't1a' and n == 'n2' and m == 'm0')
          or (t == 't1b' and n == 'n2' and m == 'm0')):
        print('分期结果：\t ⅡA 期')

    elif ((t == 't4a' and n == 'n1' and m == 'm0')
          or (t == 't3' and n == 'n2' and m == 'm0')
          or (t == 't2' and n == 'n3a' and m == 'm0')
          or (t == 't2' and n == 'n3b' and m == 'm0')):
        print('分期结果：\t ⅢA 期')

    elif ((t == 't4b' and n == 'n0' and m == 'm0')
          or (t == 't4b' and n == 'n1' and m == 'm0')
          or (t == 't4a' and n == 'n2' and m == 'm0')
          or (t == 't3' and n == 'n3a' and m == 'm0')
          or (t == 't3' and n == 'n3b' and m == 'm0')):
        print('分期结果：\t ⅢB 期')

    else:
        print('分期结果：\t ⅢC 期')
