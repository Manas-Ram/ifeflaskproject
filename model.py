
# needed_kids = float(input("What is the maximum amount of money do you think you will have to spend per month on food: "))


def budgetcalc(debt, salary, saved_money, rent, food, kids):
    # salary = float(input("How much money do you make per month: "))
    # saved_money = float(input("How much money have you saved: "))
    # rent = float(input("How much rent do you pay per month: "))
    # food = float(input("How much money do you spend on food per month: "))
    # debt = float(input("How much debt do you have: "))
    # kids = float(input("How many kids do you have: "))
    float_debt = float(debt)
    float_salary = float(salary)
    float_saved = float(saved_money)
    float_rent = float(rent)
    float_food = float(food)
    float_kids = float(kids)
    if float_debt == 0:
        if float_salary <= 8750 and float_salary >= 7900:
            salary2 = float_salary - float_rent  # Subtract food
            salary3 = salary2 - float_food  # Subtract
            other_salary = salary3 * 0.6
            new_salary = salary3 * 0.4
            new_saved_money = float_saved + new_salary  # Adding to saved money
            additional_Savings = new_saved_money - float_saved
            print("You have $" + str(new_saved_money) + " in your savings. You have saved an additional $" +
                  str(additional_Savings) + "! Thank you for using this calculator")
            if float_kids >= 1:

                clothes = 300*float_kids
                salary_after_clothing = other_salary - clothes
                print("You can spend a maximum of " + str(clothes) +
                      " on clothes for your children per year. You have $" + str(salary_after_clothing) + " left")
                materials = float(
                    input("How much do you pay for school materials every year per kid? "))
                school_mat = materials * float_kids
                good_mat = 450
                total_mat = good_mat*2
                if school_mat >= 450*float_kids:
                    print("You should spend $" + str(good_mat) +
                          " per kid, which is $" + str(total_mat) + " in total")
                    salary_after_mat = salary_after_clothing - total_mat
                    print("You have $" + str(salary_after_mat) + " left")
                    # this is for kids who go to school with tuition
                    school = input(
                        "Do you have to pay for your kids to go to school? ")

                    if school.lower() == "yes":
                        yearly_pay = input("Do you pay per year or month? ")
                        if yearly_pay.lower() == "year":
                            school_pay = float(
                                input("How much money do you pay per year: "))
                            other_salary2 = other_salary - school_pay
                            return "You now have $" + str(other_salary2) + " left."
                        elif yearly_pay.lower() == "month":
                            monthly_school_pay = float(
                                input("How much money do you pay per month: "))
                            other_salary2 = other_salary - monthly_school_pay
                            return "You now have $" + str(other_salary2) + " left."

                    else:
                        return "You can move on"
                elif school_mat <= 450*float_kids:
                    print("You can raise that amount to $" + str(good_mat) +
                          " per kid, which is $" + str(total_mat) + " in total")
                    salary_after_mat = salary_after_clothing - total_mat
                    print("You have $" + str(salary_after_mat) + " left")
                    # this is for kids who go to school with tuition
                    school = input(
                        "Do you have to pay for your kids to go to school? ")

                    if school.lower() == "yes":
                        yearly_pay = input("Do you pay per year or month? ")
                        if yearly_pay.lower() == "year":
                            school_pay = float(
                                input("How much money do you pay per year: "))
                            other_salary2 = other_salary - school_pay
                            return "You now have $" + str(other_salary2) + " left."
                        elif yearly_pay.lower() == "month":
                            monthly_school_pay = float(
                                input("How much money do you pay per month: "))
                            other_salary2 = other_salary - monthly_school_pay
                            return "You now have $" + str(other_salary2) + " left."
                    else:
                        return "You can move on"
            else:
                return ("Thank you for using this calculator!")

    if float_debt >= 0:
        print("We can lead you in the right direction to get rid of $" + str(float_debt))
        if float_salary <= 4500 and float_salary >= 2100:
            debt_salary = float_salary-float_rent
            print("Your money after rent is $" + str(debt_salary))
            food_spend = float(input("How much money do you regularly spend for food each meal (Breakfast, Lunch, Dinner)"))
            if food_spend > 7:
                print("Try to manage your food prices. Look for foods that are $7 or less. ")
            savings_food = food_spend - 7
            food_wo_sal = debt_salary - 245
            print("If you manage to eat foods that are $7 or less you will have + $" + str(food_wo_sal))
            if savings_food > 0:
                print("If or when you try and stick to the $7 foods for breakfast, lunch, dinner, you now save $" + str(savings_food) + " in your savings account. You should do this everyday for atleast a year")
            debt_may_pay = food_wo_sal - float_debt
            if debt_may_pay >= 100:
                if float_kids == 0:
                    print("Your debt is now gone! You've paid it off! You still have $" + str(debt_may_pay) + " left in your savings, but this should be for emergencies only")
