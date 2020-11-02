import os
import time
import common_carcinoma_tools as cct
import lung.lung_carcinoma_tnm
import gastric.gastric_carcinoma_tnm
import esophagus.esophagus_carcinoma_tnm
import kidney.kidney_carcinoma_tnm
import bladder.bladder_carcinoma_tnm
import rectum.rectum_carcinoma_tnm

def show_menu():
    print('\n',"肿瘤TNM分期".center(40,"="),end = '\n\n')
    print("请输入以下选择（小写）！\n随时输入 [Q] 退出或返回！\n不要输入 [TX、T0、NX] 等不需要分期的因素！\n")
    print("-" * 44)
    print("| 肺癌（L）\t胃癌（G）\t食管癌（E）|\n| 肾癌（K）\t膀胱癌（B）\t直肠癌（R）|")
    print("-" * 44,end = '\n\n')

def header(describe):
    '''
    为各个肿瘤分别定义表头
    :param describe: 为肿瘤名字
    :return: 无
    '''
    print('\n',describe.center(53,'='),end = '\n\n')


def print_result(func, describe, t, T, n, N, m, M):
    exec_time = time.asctime(time.localtime(time.time()))
    print('\n', describe.center(40, '-'), end='\n')
    print('输入分期：\t', t.capitalize(), n.capitalize(), m.capitalize())

    func(t, n, m)

    print('\n' + t.capitalize() + '\t\t' + T)
    print(n.capitalize() + '\t\t' + N)
    print(m.capitalize() + '\t\t' + M, end='\n')
    print('按回车返回！'.center(40, '-'))

    print('\n', exec_time.center(43))


def read_file(file_name):
    '''
    读取文件
    :param file_name:
    :return:
    '''
    with open(file_name, 'r', encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)


def print_sep_40():
    print('\n', '请输入以上选择（小写）！随时输入q退出或返回！'.center(40, '-'), end='\n\n')


def print_sep_60():
    print('\n', '-' * 60, end='\n\n')

def e_judge_tnm(tnm_dict):
    '''
    分别判断食管癌t、n、m并返回其键-值对，为最后的输出准备变量
    :param tnm_dict:
    :return:
    '''
    tumor = {'tis': '原位癌/重度不典型增生',
             't1a': '肿瘤侵及固有层或粘膜肌层',
             't1b': '肿瘤侵及粘膜下层',
             't2': '肿瘤侵及固有肌层',
             't3': '肿瘤侵及外膜',
             't4a': '肿瘤侵及胸膜、心包、奇静脉、膈肌或腹膜',
             't4b': '肿瘤侵及临近器官，如主动脉、椎体、呼吸道等',
             'q':'返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1': '1-2个区域淋巴结',
            'n2': '3-6个区域淋巴结',
            'n3': '7个及以上区域淋巴结',
            'q':'返回'}

    metastasis = {'m0': '无远处转移',
                  'm1': '有远处转移',
                  'q':'返回'}
    	
    while ((tnm_dict not in tumor )
        and (tnm_dict not in node )
        and (tnm_dict not in metastasis)):    
        tnm_dict = input('请输入上述中的选择： ')

    if tnm_dict in tumor:
        return tnm_dict,tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict,node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict,metastasis[tnm_dict]


def b_judge_tnm(tnm_dict):
    '''
    判断膀胱癌
    :param tnm_dict:
    :return:
    '''
    tumor = {'ta': '非浸润性乳头状尿路上皮癌',
             'tis': '原位癌：扁平肿瘤',
             't1': '肿瘤浸润粘膜下层',
             't2a': '肿瘤浸润浅肌层（内侧1/2肌层）',
             't2b': '肿瘤浸润深肌层（外侧1/2肌层）',
             't3a': '显微镜下观察，肿瘤已经长入膀胱周围组织',
             't3b': '肉眼、影像可见膀胱周围肿块',
             't4a': '肿瘤浸润前列腺/精囊/子宫/阴道',
             't4b': '肿瘤浸润盆壁/腹壁',
             'q': '返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1': '真骨盆单个区域淋巴结转移（膀胱周围、闭孔、髂内/外、骶前淋巴结转移）',
            'n2': '真骨盆多个区域淋巴结转移（膀胱周围、闭孔、髂内/外、骶前淋巴结转移）',
            'n3': '髂总动脉淋巴结转移',
            'q': '返回'}

    metastasis = {'m0': '无远处转移',
                  'm1a': '超过髂总动脉的淋巴结转移',
                  'm1b': '非淋巴结远处转移',
                  'q': '返回'}

    while ((tnm_dict not in tumor)
           and (tnm_dict not in node)
           and (tnm_dict not in metastasis)):
        tnm_dict = input('请输入上述中的选择： ')

    if tnm_dict in tumor:
        return tnm_dict, tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict, node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict, metastasis[tnm_dict]

def g_judge_tnm(tnm_dict):
    '''
    判断胃癌
    :param tnm_dict:
    :return:
    '''
    tumor = {'tis': '原位癌',
             't1a': '肿瘤侵及固有层或粘膜肌层',
             't1b': '肿瘤侵及粘膜下层',
             't2': '肿瘤侵及固有肌层',
             't3': '肿瘤侵及浆膜下层',
             't4a': '肿瘤穿透浆膜层',
             't4b': '肿瘤侵及周围结构',
             'q': '返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1': '1-2个区域淋巴结',
            'n2': '3-6个区域淋巴结',
            'n3a': '7-15个区域淋巴结',
            'n3b': '16个及以上区域淋巴结',
            'q': '返回'}

    metastasis = {'m0': '无远处转移',
                  'm1': '有远处转移',
                  'q': '返回'}

    while ((tnm_dict not in tumor)
           and (tnm_dict not in node)
           and (tnm_dict not in metastasis)):
        tnm_dict = input('请输入上述中的选择： ')

    if tnm_dict in tumor:
        return tnm_dict, tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict, node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict, metastasis[tnm_dict]

def k_judge_tnm(tnm_dict):
    '''
    判断胃癌
    :param tnm_dict:
    :return:
    '''
    tumor = {'t1a': '最大径 <= 4cm',
             't1b': '4cm < 最大径 <= 7cm',
             't2a': '7cm < 最大径 <= 10cm',
             't2b': '最大径 >= 10cm',
             't3a': '''①肿瘤侵及肾静脉或肾静脉分支
            ②或肿瘤侵及肾盂肾盏系统或侵犯肾周脂肪
            ③和（或）肾窦脂肪（肾盂旁脂肪），但未超过肾周筋膜''',
             't3b': '肿瘤侵及横膈膜下的下腔静脉',
             't3c': '肿瘤侵及横膈膜上的下腔静脉或侵及下腔静脉壁',
             't4': '肿瘤侵透肾周筋膜，包括侵及邻近肿瘤的同侧肾上腺',
             'q': '返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1': '有区域淋巴结',
            'q': '返回'}

    metastasis = {'m0': '无远处转移',
                  'm1': '有远处转移',
                  'q': '返回'}

    while ((tnm_dict not in tumor)
           and (tnm_dict not in node)
           and (tnm_dict not in metastasis)):
        tnm_dict = input('请输入上述中的选择： ')

    if tnm_dict in tumor:
        return tnm_dict, tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict, node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict, metastasis[tnm_dict]

def l_judge_tnm(tnm_dict):
    '''
    判断肺癌
    :param tnm_dict:
    :return:
    '''
    tumor = {'tis': '原位癌（原位鳞癌、原位腺癌：纯贴壁生长、最大径 <= 3cm）',
             't1a': '''①最大径 <= 1cm 
            ②任何大小的表浅扩散型肿瘤，但局限于气管壁或主支气管壁，罕见''',
             't1b': '1cm < 最大径 <= 2cm',
             't1c': '2cm < 最大径 <= 3cm',
             't2a': '3cm < 最大径 <= 4cm',
             't2b': '4cm < 最大径 <= 5cm',
             't3': '''肿瘤 5< 最大径 <= 7cm
            直接侵犯以下任一器官：胸壁（含肺上沟瘤）、膈神经、心包
            同一肺叶出现孤立性癌结节''',
             't4': '''肿瘤最大径 > 7cm
            侵犯以下任一器官：纵隔、膈肌、心脏、大血管、喉返神经、隆突、气管、食管、椎体
            同侧不同肺叶孤立性癌结节''',
             'q': '返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1': '同侧支气管周围和/或同侧肺门淋巴结以内以及肺内淋巴结又转移，包括原发肿瘤直接侵犯',
            'n2': '同侧纵隔内和/或隆突下淋巴结转移',
            'n3': '对侧纵隔、对侧肺门、同侧或对侧前斜角肌及锁骨上淋巴结转移',
            'q': '返回'}

    metastasis = {'m0': '无远处转移',
                  'm1a': '''①对侧肺叶内孤立性癌结节
            ②胸膜播散（恶性胸腔积液*、心包积液或胸膜结节
            *:[细胞学检查阴性、非血性、非渗出性的不能作为分期因素]''',
                  'm1b': '远处单个器官单发转移',
                  'm1c': '远处单个或多个器官多发转移',
                  'q': '返回'}

    while ((tnm_dict not in tumor)
           and (tnm_dict not in node)
           and (tnm_dict not in metastasis)):
        tnm_dict = input('请输入上述中的选择： ')

    if tnm_dict in tumor:
        return tnm_dict, tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict, node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict, metastasis[tnm_dict]

def r_judge_tnm(tnm_dict):
    '''
    判断直肠癌
    :param tnm_dict:
    :return:
    '''
    tumor = {'tis': '原位癌',
             't1': '肿瘤浸润黏膜下层',
             't2': '肿瘤浸润固有肌层',
             't3': '肿瘤侵及浆膜下层或侵犯无腹膜覆盖的结肠旁或直肠旁组织织',
             't4a': '肿瘤穿透脏层腹膜',
             't4b': '肿瘤直接侵犯其他器官或组织',
             'q': '返回'}

    node = {'n0': '无区域淋巴结转移',
            'n1a': '1个区域淋巴结转移',
            'n1b': '2-3个区域淋巴结转移',
            'n1c': '''浆膜下、肠系膜或无腹膜覆盖的结直肠周围软组织有腹膜种植（TD）
    	无区域淋巴结转移''',
            'n2a': '4-6个区域淋巴结转移',
            'n2b': '7个或更多区域淋巴结转移',
            'q': '返回'}

    metastasis = {'m0': '无远处转移',
                  'm1a': '''转移局限于1个器官（肝、肺、卵巢、无区域淋巴结）
            无腹膜转移''',
                  'm1b': '''一个以上气管有远处转移
            无腹膜转移''',
                  'm1c': '转移到腹膜，伴或不伴其他器官转移',
                  'q': '返回'}

    while ((tnm_dict not in tumor)
           and (tnm_dict not in node)
           and (tnm_dict not in metastasis)):
        tnm_dict = input('请输入上述中的选择： ')


    if tnm_dict in tumor:
        return tnm_dict, tumor[tnm_dict]
    elif tnm_dict in node:
        return tnm_dict, node[tnm_dict]
    elif tnm_dict in metastasis:
        return tnm_dict, metastasis[tnm_dict]