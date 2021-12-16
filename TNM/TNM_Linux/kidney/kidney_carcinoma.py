import os
import time
import kidney.kidney_carcinoma_tnm
import common_carcinoma_tools as cct

def kidney_carcinoma_main():
    cct.header('肾癌TNM分期')
    cct.read_file('kidney//kidney_carcinoma_t.txt')
    cct.print_sep_40()
    t, T = cct.k_judge_tnm(input('请输入原发肿瘤的性质： '))
    os.system('clear')

    if t == 'q':
        os.system('clear')
        return

    cct.print_sep_60()
    cct.read_file('kidney//kidney_carcinoma_n.txt')
    cct.print_sep_40()
    n, N = cct.k_judge_tnm(input('请输入淋巴结转移情况： '))
    os.system('clear')

    if n == 'q':
        os.system('clear')
        return

    cct.print_sep_60()
    cct.read_file('common_carcinoma_m.txt')
    cct.print_sep_40()
    m, M = cct.k_judge_tnm(input('请输入远处转移情况： '))
    os.system('clear')

    if m == 'q':
        os.system('clear')
        return

    cct.print_result(kidney.kidney_carcinoma_tnm.kct_tnm, '肾癌cTNM分期', t=t, T=T, n=n, N=N, m=m, M=M)

    input()
    os.system("clear")
