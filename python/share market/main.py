import time


share_name = input("Enter The Name of The Share : ")


def main():
    intrensic_value = input("Enter The Intrensic Value is less than price of Share (y/n) : ")

    x = 0
    if intrensic_value == "y" or intrensic_value == "Y":
        PE = float(input("Enter The PE Ratio of Share : "))
        PB = float(input("Enter The PB Ratio of Share : "))
        Current = float(input("Enter The Current Ratio Of the Share : "))
        Debt_to_equity = float(input("Enter The Debt To Equity Ratio : "))
        nifti_50 = input("Is The Company is in Nifty 50 (y/n) : ")

        if PE <= 32 and PE >= 18:
            x += 1
        if PB > 2:
            x += 1
        if Current > 1:
            x += 1
        if Debt_to_equity >= 2:
            x += 1
        if nifti_50 == "y":
            x += 1
        # print(x)
        if x == 5:
            print("This Stock Could be Great perfomer .....")
        if x == 4:
            print("This Stock Could perfome good ....")
        if x == 3:
            print("This Stock Can Do Well But May be containing some risk ...")
        if x == 2:
            print("This Stock May not Perfome Well ...... ")
        if x == 1:
            print("This Stock is Too risky ... ")
        if x == 0:
            print("You may Ignore this Stock for Value Investing ...")

    elif intrensic_value == "n" or intrensic_value == "N":
        print("This Stock Is Not for value Investment ......")
    else:
        main()


main()
