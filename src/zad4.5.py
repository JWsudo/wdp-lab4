def bmi(waga, wzrost):
    bmi_var = waga / (wzrost*wzrost)
    if bmi_var < 18.5:
        print("niedowaga")
    elif 18.5 < bmi_var < 25:
        print("ok")
    elif 25 <= bmi_var <30:
        print("nadwaga")
    elif 30 <= bmi_var <35 :
        print("otylosc I")
    elif 35 <= bmi_var < 40:
        print("otylosc II ")
    elif bmi_var > 40:
        print("otylosc III")

    return bmi_var

print(bmi(65,1.65))