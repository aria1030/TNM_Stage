import os
import time
import bladder.bladder_carcinoma_tnm
import common_carcinoma_tools as cct

def bladder_carcinoma_main():
    cct.header('膀胱癌TNM分期')
    cct.read_file('bladder\\bladder_carcinoma_t.txt')
    cct.print_sep_40()
    t, T = cct.b_judge_tnm(input('请输入原发肿瘤的性质： '))
    os.system('cls')

    if t == 'q':
        os.system('cls')
        return

    cct.print_sep_60()
    cct.read_file('bladder\\bladder_carcinoma_n.txt')
    cct.print_sep_40()
    n, N = cct.b_judge_tnm(input('请输入淋巴结转移情况： '))
    os.system('cls')

    if n == 'q':
        os.system('cls')
        return

    cct.print_sep_60()
    cct.read_file('bladder\\bladder_carcinoma_m.txt')
    cct.print_sep_40()
    m, M = cct.b_judge_tnm(input('请输入远处转移情况： '))
    os.system('cls')

    if m == 'q':
        os.system('cls')
        return

    cct.print_result(bladder.bladder_carcinoma_tnm.bct_tnm, '膀胱癌TNM分期', t=t, T=T, n=n, N=N, m=m, M=M)

    input()
    os.system("cls")
