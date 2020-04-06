from app import app
from flask import render_template, flash, redirect, request
from app.forms import InputForm
from app.forms import Sigaretts
from app.forms import Water
from app.parser import get_grechka, get_siga, get_water

za_grechu = 0
za_ciga = 0
za_water = 0


@app.route('/', methods=['GET', 'POST'])
@app.route('/grecha', methods=['GET', 'POST'])
def grecha():
    form = InputForm()
    global za_grechu
    cena = get_grechka()
    if form.validate_on_submit():
        summa_grechku = ((form.var2.data * form.var1.data) * form.var3.data)
        kilkist_pachok = summa_grechku / 400
        cena_za_vse = kilkist_pachok * cena
        za_grechu = cena_za_vse
        flash(' ціна : {}, кількість пачок на місяць: {} '.format(cena_za_vse, kilkist_pachok))
    return render_template('home.html', form=form, cena=cena, title='Grecha')


@app.route('/cigarette', methods=['GET', 'POST'])
def cigarette():
    form = Sigaretts()
    cena = get_siga()
    global za_ciga
    if form.validate_on_submit():
        kolichestvo_sig = form.var1.data * 30
        kilkist_pachok = kolichestvo_sig / 20
        cena_za_vse = kilkist_pachok * cena
        za_ciga = cena_za_vse
        flash(' ціна : {}, кількість пачок на місяць: {} '.format(cena_za_vse, kilkist_pachok))
    return render_template('cigarette.html', title='Sigarette', form=form, cena=cena)


@app.route('/water', methods=['GET', 'POST'])
def water():
    form = Water()
    cena = get_water()
    global za_water
    if form.validate_on_submit():
        kolichestvo_litriv = form.var1.data * 30
        kilkist_butylok = kolichestvo_litriv / 2
        cena_za_vse = kilkist_butylok * cena
        za_water = cena_za_vse
        flash(' ціна : {}, кількість бутлок на місяць: {} '.format(cena_za_vse, kilkist_butylok))
    return render_template('water.html', title='Water', form=form, cena=cena)


@app.route('/za vse')
def za_vse():
    cena_za_vse = za_ciga + za_grechu + za_water
    return render_template('vse.html', title='Cost', za_grechu=za_grechu, za_ciga=za_ciga,
                           za_water=za_water, cena_za_vse=cena_za_vse)


