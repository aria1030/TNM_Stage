def kct_tnm(t,n,m):
    if t == 't4' or m == 'm1':
        print('分期结果：\t Ⅳ 期')

    elif ((t == 't1a' and n == 'n0' and m =='m0')
        or(t == 't1b' and n == 'n0' and m =='m0')):
        print('分期结果：\t Ⅰ 期')

    elif ((t == 't2a' and n == 'n0' and m == 'm0')
          or (t == 't2b' and n == 'n0' and m == 'm0')):
        print('分期结果：\t Ⅱ 期')

    else:
        print('分期结果：\t Ⅲ 期')