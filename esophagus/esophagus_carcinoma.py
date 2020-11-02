import os
import esophagus.esophagus_carcinoma_tnm
import common_carcinoma_tools as cct

def esophagus_carcinoma_main():
    cct.header('食管鳞癌cTNM分期')
    cct.read_file('esophagus\\esophagus_carcinoma_t.txt')
    cct.print_sep_40()
    t,T=  cct.e_judge_tnm(input('请输入原发肿瘤的性质： '))
    os.system('cls')

    if t == 'q':
        os.system('cls')
        return

    cct.print_sep_60()
    cct.read_file('esophagus\\esophagus_carcinoma_n.txt')
    cct.print_sep_40()
    n,N =  cct.e_judge_tnm(input('请输入淋巴结转移情况： '))
    os.system('cls')

    if n == 'q':
        os.system('cls')
        return

    cct.print_sep_60()
    cct.read_file('common_carcinoma_m.txt')
    cct.print_sep_40()
    m,M =  cct.e_judge_tnm(input('请输入远处转移情况： '))
    os.system('cls')

    if m == 'q':
        os.system('cls')
        return

    cct.print_result(esophagus.esophagus_carcinoma_tnm.ect_tnm,'食管鳞癌cTNM分期',t=t,T=T,n=n,N=N,m=m,M=M)

    input()
    os.system("cls")
