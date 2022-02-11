#devs_money = 9
#dev_can_play_smash = True

#if devs_money > 10 and dev_can_play_smash:
#    print("Dev enters a smash tournament!")
#elif devs_money < 10 and dev_can_play_smash:
#    print("Dev is too poor to enter")
#else:
#    print("Dev just can't play smash")

mark = int(input("Enter your test score: "))

if  mark >= 101:
    print("Not a valid test score")
elif  mark >= 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")

    