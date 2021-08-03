# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# from flask import render_template
# from flask import request
from model import budgetcalc


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/investment.html')
def investment():
    return render_template('investment.html')
@app.route('/budget.html')
def budget():
    return render_template('budget.html')
    # print(request.form['yes'])
    # access = request.form['yes']
    # calculator = budgetcalc(access)
    # if request.method == "POST":
    #     return render_template('budget.html', access = access, calculator = calculator)
    # else:
    #     return "404 error"
@app.route('/result', methods = ['GET', 'POST'])
def result():
    print(request.form['yes'])
    print(request.form['sal'])
    print(request.form['save'])
    print(request.form['rent_per'])
    print(request.form['foods'])
    print(request.form['kid'])
    print(request.form['mat'])
    print(request.form['school'])

    print(request.form['pay'])
    print(request.form['food_debt'])


    deb = request.form['yes']
    sala = request.form['sal']
    saved = request.form['save']
    monthly_rent = request.form['rent_per']
    monthly_food = request.form['foods']
    counted = request.form['kid']
    material = request.form['mat']
    private = request.form['school']


    tuition = request.form['pay']
    food_w_breakfast = request.form['food_debt']
    debted = budgetcalc(deb, sala, saved, monthly_rent, monthly_food, counted,material,private,tuition, food_w_breakfast)
    
    
    # user_salary = budgetcalc(sala)
    
    
    # user_saved = budgetcalc(saved)
    
    
    # user_rent = budgetcalc(monthly_rent)
    
   
    # user_foods = budgetcalc(monthly_food)
    
    
    # user_kids = budgetcalc(counted)
    if request.method == "POST":
        if request.form['submit_button'] == 'Submit':
            return render_template('result.html', deb = deb, debted=debted, sala = sala, saved = saved, monthly_rent = monthly_rent, monthly_food = monthly_food, counted = counted, material = material, private=private, tuition=tuition, food_w_breakfast = food_w_breakfast )
    else:
        return "404 error"



# sala = sala, user_salary = user_salary, saved = saved, user_saved = user_saved, monthly_rent = monthly_rent, user_rent = user_rent, monthly_food = monthly_food, user_foods = user_foods, counted = counted, user_kids= user_kids