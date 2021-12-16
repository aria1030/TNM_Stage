def lct_tnm(t,n,m):
    if m == 'm1a' or m == 'm1b':
        print('分期结果：\t ⅣA 期')

    elif m == 'm1c':
        print('分期结果：\t ⅣB 期')

    elif t == 'tis' and n == 'n0' and m == 'm0':
        print('分期结果：\t 0 期 隐匿性癌')

    elif ((t == 't1a' and n == 'n0' and m =='m0')
        or(t == 't1b' and n == 'n0' and m =='m0')
        or (t == 't1c' and n == 'n0' and m == 'm0')):
        print('分期结果：\t ⅠA 期')

    elif (t == 't2a' and n == 'n0' and m =='m0'):
        print('分期结果：\t ⅠB 期')

    elif (t == 't2b' and n == 'n0' and m =='m0'):
        print('分期结果：\t ⅡA 期')

    elif ((t == 't3' and n == 'n0' and m == 'm0')
          or (t == 't1a' and n == 'n1' and m == 'm0')
          or (t == 't1b' and n == 'n1' and m == 'm0')
          or (t == 't1c' and n == 'n1' and m == 'm0')
          or (t == 't2a' and n == 'n1' and m == 'm0')
          or (t == 't2b' and n == 'n1' and m == 'm0')):
        print('分期结果：\t ⅡB 期')

    elif ((t == 't4' and n == 'n0' and m == 'm0')
          or (t == 't3' and n == 'n1' and m == 'm0')
          or (t == 't4' and n == 'n1' and m == 'm0')
          or (t == 't1a' and n == 'n2' and m == 'm0')
          or (t == 't1b' and n == 'n2' and m == 'm0')
          or (t == 't1c' and n == 'n2' and m == 'm0')
          or (t == 't2a' and n == 'n2' and m == 'm0')
          or (t == 't2b' and n == 'n2' and m == 'm0')):
        print('分期结果：\t ⅢA 期')

    elif ((t == 't3' and n == 'n3' and m == 'm0')
          or (t == 't4' and n == 'n3' and m == 'm0')):
        print('分期结果：\t Ⅲc 期')

    else:
        print('分期结果：\t ⅢB 期')
