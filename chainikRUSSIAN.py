import time
teapot_body = r"""
                          (
            _           ) )
         _,(_)._        ((
    ___,(_______).        )
  ,'__.           \    /\_
 /,' /             \  /  /
| | |              |,'  /
 \`.|                  /
  `. :           :    /
    `.            :.,'
      `-.________,-'
"""
teapot_liquid =r"""
                   _
         _,(_)._
    ___,(_______).      ____
  ,'__.           \    /\___\-.
 /,' /             \  /  /     \
 | | |              |,'  /       \
 \`.|                  /       _|_
  `. :           :    /        MMM
    `.            :.,'        IMMMI
      `-.________,-'          IMMMI 
"""
coffeemilksug = r"""
            ) _ )  ( _ )
         (   (   )   )
          ) _ )  ( _ )     
              (   )   (   )
          ) _ )  ( _ )
         (   (   )   )
          ) _ )  ( _ )
         ___________
        <___________>___

         |         | /  \
         |         ||    |
         |         ||    |
         |         | \__/
         \_________/
"""
while True:
    time.sleep(1)
    print("ВЫ ХОТИТЕ ВКЛЮЧИТЬ ЧАЙНИК? ДА/НЕТ: ")
    chainik = input(" ").strip().lower()
    if chainik in ["да", "нет"]:
        break
        time.sleep(1)
if chainik == "да":
    print("НАЧИНАЕТСЯ ПРОЦЕСС КИПЯЧЕНИЯ: ")
    time.sleep(1)
    print(teapot_body)
    print("10%")
    time.sleep(2)
    print("20%")
    time.sleep(2)
    print("30%")
    time.sleep(2)
    print("40%")
    time.sleep(2)
    print("50%")
    time.sleep(2)
    print("60%")
    time.sleep(2)
    print("70%")
    time.sleep(2)
    print("80%")
    time.sleep(2)
    print("90%")
    time.sleep(2)
    print("100%")
    time.sleep(1)
    print("ЧАЙНИК УСПЕШНО ЗАВАРИЛСЯ")
    while True:
        time.sleep(1)
        print("ВЫ ХОТИТЕ ПОПИТЬ ЧАЙ, ИЛИ КОФЕ?  (ЧАЙ/КОФЕ): ")
        acdc = input (" ").strip().lower()
        if acdc == "кофе":
            import os
            os.system('clear' if os.name != 'nt' else 'cls')
            print(teapot_liquid)
            time.sleep(2)
            print("НАСЫПЛЕНИЕ ЗЁРЕН КОФЕ")
            time.sleep(2)
            print("УСПЕШНО")
            time.sleep(1)
            print("ВЫ ХОТИТЕ НАЛИТЬ МОЛОКА? (ДА/НЕТ)")
            milk = input (" ").strip().lower()
            if milk == "да":
                print("НАЧИНАЕТСЯ ПРОЦЕСС НАЛИВАНИЯ МОЛОКА")
                time.sleep(1)
                print("50%")
                time.sleep(2)
                print("100%")
                time.sleep(1)
                print("УСПЕШНО")
                time.sleep(1)
                print("НАЧИНИАЕТСЯ ПРОЦЕСС ЗАЛИТИЯ ВОДЫ")
                time.sleep(1)
                print("50%")
                time.sleep(2)
                print("100%")
                time.sleep(1)
                print("УСПЕШНО")
                time.sleep(1)
                print("ВЫ ХОТИТЕ ДОБАВИТЬ САХАР? (ДА/НЕТ)")
                sugarcofmilk = input(" ").strip().lower()
        
                if sugarcofmilk == "да":
                    print("КАКОЕ КОЛ-ВО ЛОЖЕК САХАРА ВЫ ХОТИТЕ ДОБАВИТЬ? (1-5)")
                    sugar_amount = input(" ")
                    if sugar_amount.isdigit():
                        sugar = int(sugar_amount)
                        if 1 <= sugar <= 5:
                            print(f"УСПЕШНО ДОБАВЛЕНО ({sugar})")
                            time.sleep(3)
                            print("ВОТ ВАШЕ КОФЕ С МОЛОКОМ: ")
                            time.sleep(1)
                            print(coffeemilksug)
                            time.sleep(1)
                        else:
                            print("НЕТ")
                    else:
                        print("НЕИЗВЕСТНЫЙ ОТВЕТ")
                        time.sleep(1)
                elif sugarcofmilk == "нет":
                    print("ПОДОЖДИТЕ НЕМНОГО ПОКА КОФЕ ПРИГОТОВИТСЯ")
                    time.sleep(4)
                    print("ВОТ ВАШЕ КОФЕ БЕЗ САХАРА: ")
                    time.sleep(1)
                    print(coffeemilksug)
                    time.sleep(1)
                else:
                    print("НЕИЗВЕСТНЫЙ ОТВЕТ")
                    time.sleep(1)
            elif milk == "нет":
                print("НАЧИНАЕТСЯ ПРОЦЕСС ЗАЛИТИЯ ВОДЫ")
                time.sleep(1)
                print("50%")
                time.sleep(2)
                print("100%")
                time.sleep(1)
                print("ВЫ ХОТИТЕ ДОБАВИТЬ САХАР? (ДА/НЕТ)")
                sugarcofnomilk = input(" ").strip().lower()
        
                if sugarcofnomilk == "да":
                        print("КАКОЕ КОЛ-ВО ЛОЖЕК САХАРА ВЫ ХОТИТЕ ДОБАВИТЬ? (1-5)")
                        sugar_amountcof = input(" ")
                        if sugar_amountcof.isdigit():
                            sugarcofer = int(sugar_amountcof)
                            if 1 <= sugarcofer <= 5:
                                print(f"УСПЕШНО ДОБАВЛЕНО ({sugar_amountcof})")
                                time.sleep(1)
                                print("ПОДОЖДИТЕ НЕМНОГО ПОКА КОФЕ ПРИГОТОВИТСЯ")
                                time.sleep(4)
                                print("ВОТ ВАШЕ КОФЕ БЕЗ МОЛОКА: ")
                                time.sleep(1)
                                print(coffeemilksug)
                                time.sleep(2)
                        else:
                            print("НЕТ")
                            time.sleep(2)
                elif sugarcofnomilk == "нет":
                    print("ПОДОЖДИТЕ НЕМНОГО ПОКА КОФЕ ПРИГОТОВИТСЯ")
                    time.sleep(4)
                    print("ВОТ ВАШЕ КОФЕ БЕЗ САХАРА: ")
                    time.sleep(1)
                    print(coffeemilksug)
                    time.sleep(1)
                else:
                    print("НЕИЗВЕСТНЫЙ ОТВЕТ") 
                    time.sleep(1)
            else:
                print("НЕИЗВЕСТНЫЙ ОТВЕТ")
                time.sleep(2)
        elif acdc == "чай": 
            print("НАЧИНАЕТСЯ ПРОЦЕСС ЧАЕФИКАЦИИ")
            time.sleep(1)
            print("ВЫ ХОТИТЕ ДОБАВИТЬ САХАР? (ДА/НЕТ)")
            sugar = input(" ").strip().lower()
        
            if sugar == "да":
                time.sleep(1)
                print("КАКОЕ КОЛ-ВО ЛОЖЕК САХАРА ВЫ ХОТИТЕ ДОБАВИТЬ? (1-5)")
                sugar_amount = input(" ")
                if sugar_amount.isdigit():
                    sugar = int(sugar_amount)
                    if 1 <= sugar <= 5:
                        print(f"УСПЕШНО ДОБАВЛЕНО ({sugar})")
                        time.sleep(1)
                        print("ПОДОЖДИТЕ НЕМНОГО ПОКА ЧАЙ ПРИГОТОВИТСЯ")
                        time.sleep(4)
                        print("ВОТ ВАШ ЧАЙ: ")
                        time.sleep(1)
                        print(coffeemilksug)
                        time.sleep(2)
                    elif sugar_amount == "0":
                        time.sleep(1)
                        print("НЕ ДОБАВЛЕНО ЛОЖЕК САХАРА")
                        time.sleep(1)
                        print("ПОДОЖДИТЕ НЕМНОГО ПОКА ЧАЙ ПРИГОТОВИТСЯ")
                        time.sleep(4)
                        print("ВОТ ВАШ ЧАЙ БЕЗ САХАРА: ")
                        time.sleep(1)
                        print(coffeemilksug)
                        time.sleep(2)
                    else:
                        print("НЕТ")
                        time.sleep(1)
                else:
                    print("ВВЕДИ В ЦИФРАХ")
                    time.sleep(1)
            elif sugar == "нет":
                time.sleep(1)
                print("ПОДОЖДИТЕ НЕМНОГО ПОКА ЧАЙ ПРИГОТОВИТСЯ")
                time.sleep(4)
                print("ВОТ ВАШ ЧАЙ БЕЗ САХАРА: ")
                time.sleep(1)
                print(coffeemilksug)
                time.sleep(2)
            else:
                print("НЕИЗЫЕСТНЫЙ ОТВЕТ")
                time.sleep(1)
        else:
            print ("НЕИЗВЕСТНЫЙ ОТВЕТ")
elif chainik == "нет":
    print("НУ ЛАДНО")
    time.sleep(2)
else:
    print("НЕИЗВЕСТНЫЙ ОТВЕТ")
    time.sleep(2)
