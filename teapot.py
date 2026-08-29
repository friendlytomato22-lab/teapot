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
    print("WOULD YOU LIKE TO TURN ON TEAPOT? (yes/no): ")
    chainik = input(" ").strip().lower()
    if chainik == "yes":
        print("TURNIN ON TEAPOT: ")
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
        print("SUCCESS")
        while True:
            time.sleep(1)
            print("WAHT WOULD YOU LIKE TO DRINK? (tea/coffee): ")
            acdc = input (" ").strip().lower()
            if acdc == "coffee":
                import os
                os.system('clear' if os.name != 'nt' else 'cls')
                print(teapot_liquid)
                time.sleep(2)
                print("ADDING A COFFEE")
                time.sleep(2)
                print("SUCCESS")
                time.sleep(1)
                print("WOULD YOU LIKE TO ADD A MILK? (YES/NO)")
                milk = input (" ").strip().lower()
                if milk == "yes":
                    print("ADDING A MILK")
                    time.sleep(1)
                    print("50%")
                    time.sleep(2)
                    print("100%")
                    time.sleep(1)
                    print("SUCCESS")
                    time.sleep(1)
                    print("ADDING A WATER")
                    time.sleep(1)
                    print("50%")
                    time.sleep(2)
                    print("100%")
                    time.sleep(1)
                    print("SUCCESS")
                    time.sleep(1)
                    print("WOULD YOU LIKE A SUGAR? (YES/NO)")
                    sugarcofmilk = input(" ").strip().lower()

                    if sugarcofmilk == "yes":
                        print("HOW MANY CUBES OF SUGAR WOULD YOU LIKE? (1/5)")
                        sugar_amount = input(" ")
                        if sugar_amount.isdigit():
                            sugar = int(sugar_amount)
                            if 1 <= sugar <= 5:
                                print(f"SUCCESSFULY ADDED ({sugar})")
                                time.sleep(3)
                                print("THERE'S YOUR COFFEE WITH MILK: ")
                                time.sleep(1)
                                print(coffeemilksug)
                                time.sleep(1)
                            else:
                                print("NO NO NO")
                        else:
                            print("UNKNOWN ANSWER")
                            time.sleep(1)
                    elif sugarcofmilk == "no":
                        print("WAIT FOR YOUR COFFEEEEEE")
                        time.sleep(4)
                        print("THERE'S YOUR COFFEE WITHOUT SUGAR: ")
                        time.sleep(1)
                        print(coffeemilksug)
                        time.sleep(1)
                    else:
                        print("UNKNOWN ANSWER")
                        time.sleep(1)
                elif milk == "no":
                    print("ADDING WATER")
                    time.sleep(1)
                    print("50%")
                    time.sleep(2)
                    print("100%")
                    time.sleep(1)
                    print("WOULD YOU LIKE A SUGAR? (YES/NO)")
                    sugarcofnomilk = input(" ").strip().lower()

                    if sugarcofnomilk == "yes":
                            print("HOW MANY CUBES OF SUGAR WOULD YOU LIKE? (1/5)")
                            sugar_amountcof = input(" ")
                            if sugar_amountcof.isdigit():
                                sugarcofer = int(sugar_amountcof)
                                if 1 <= sugarcofer <= 5:
                                    print(f"SUCCESSFULY ADDED ({sugar})")
                                    time.sleep(1)
                                    print("WAIT FOR YOUR COFFEEEEEE")
                                    time.sleep(4)
                                    print("THERE'S YOUR COFFEE: ")
                                    time.sleep(1)
                                    print(coffeemilksug)
                                    time.sleep(2)
                            else:
                                print("NO NO NO")
                                time.sleep(2)
                    elif sugarcofnomilk == "no":
                        print("WAIT FOR YOUR COFFEEEEEE")
                        time.sleep(4)
                        print("THERE'S YOUR COFFEE: ")
                        time.sleep(1)
                        print(coffeemilksug)
                        time.sleep(1)
                    else:
                        print("UNKNOWN ANSWER") 
                        time.sleep(1)
                else:
                    print("UNKNOWN ANSWER")
                    time.sleep(2)
            elif acdc == "tea": 
                print("ADDING TEA")
                time.sleep(1)
                print("WOULD YOU LIKE A SUGAR? (YES/NO)")
                sugar = input(" ").strip().lower()

                if sugar == "yes":
                    time.sleep(1)
                    print("HOW MANY CUBES OF SUGAR WOULD YOU LIKE? (1/5)")
                    sugar_amount = input(" ")
                    if sugar_amount.isdigit():
                        sugar = int(sugar_amount)
                        if 1 <= sugar <= 5:
                            print(f"SUCCESSFULY ADDED ({sugar})")
                            time.sleep(1)
                            print("WAIT FOR YOUR TEEEEEEEEEEAAAAAAA")
                            time.sleep(4)
                            print("THERE'S YOUR TEAAAAAAAAAAAAAA: ")
                            time.sleep(1)
                            print(coffeemilksug)
                            time.sleep(2)
                        elif sugar_amount == "0":
                            time.sleep(1)
                            print("NOT ADDED ANY SUGAR")
                            time.sleep(1)
                            print("WAIT FOR YOUR TEEEEEAAAAAAAAAA")
                            time.sleep(4)
                            print("THERE'S YOUR TEAAAAAAAAAAAAAA: ")
                            time.sleep(1)
                            print(coffeemilksug)
                            time.sleep(2)
                        else:
                            print("NO NO NO NO")
                            time.sleep(1)
                    else:
                        print("PRINT NUMBERSSS PLSSSSSSS")
                        time.sleep(1)
                elif sugar == "no":
                    time.sleep(1)
                    print("WAIT FOR YOUR TEEEEEAAAAAAAAAAAA")
                    time.sleep(4)
                    print("THERE'S YOUR TEEEEEEAAAAAAAAAA: ")
                    time.sleep(1)
                    print(coffeemilksug)
                    time.sleep(2)
                else:
                    print("UNKNOWN ANSWER")
                    time.sleep(1)
            else:
                print ("UNKNOWN ANSWER")
    elif chainik == "no":
        print("OK SO")
        time.sleep(2)
    else:
        print("UNKNOWN ANSWER")
        time.sleep(2)
