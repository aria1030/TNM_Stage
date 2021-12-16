
import os
# import time
import common_carcinoma_tools as cct
import lung.lung_carcinoma
import gastric.gastric_carcinoma
import esophagus.esophagus_carcinoma
import kidney.kidney_carcinoma
import bladder.bladder_carcinoma
import rectum.rectum_carcinoma

# exec_time = time.asctime(time.localtime(time.time()))
# print(exec_time.center(43))

while True:
    cct.show_menu()
    select = input("请输入你要分期的肿瘤： ")
    os.system("clear")

    if select in ["l","g","e","k","b","r","q"]:
        if select == "l":
            lung.lung_carcinoma.lung_carcinoma_main()
        elif select == "g":
            gastric.gastric_carcinoma.gastric_carcinoma_main()
        elif select == "e":
            esophagus.esophagus_carcinoma.esophagus_carcinoma_main()
        elif select == "k":
            kidney.kidney_carcinoma.kidney_carcinoma_main()
        elif select == "b":
            bladder.bladder_carcinoma.bladder_carcinoma_main()
        elif select == "r":
            rectum.rectum_carcinoma.rectum_carcinoma_main()
        elif select == "q":
            print("谢谢使用，再见！")
            input()
            break
    else:
        print("您的输入有误，请重新输入！\n\n")
