from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import sympy
from DerivTest import diff, diff2, trapz
from sympy.parsing.sympy_parser import parse_expr
from sympy import Symbol

#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

def functionGraph(function):
    #x=np.array(range(10))
    x1 = -5;
    x2 = 5;
    print("1st input:")
    y=function
    def f(x):
        return eval(y)
    print("Domain Val 1:")
    x1 = float(input())
    print("Domain Val 2:")
    x2 = float(input())
    print("Range Val 1:")
    y1 = float(input())
    print("Range Val 2:")
    y2 = float(input())
    print("Processing...")
    xRange1 = np.arange(x1, x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    yParsed = parse_expr(y, evaluate=False)
    n, d = yParsed.as_numer_denom()
    #s = Symbol('s', real = True)
    undef = sympy.solve(d)
    numzero = sympy.solve(n)
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)
    plt.autoscale(False)
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count+1
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2,2,1)
    ax1.plot(xVal1, yVal1, 'g')
    for x in undef:
        if x not in numzero:
            try:
                ax1.axvline(x=x, linestyle = '--')
            except:
                pass
        else:
            x=x+0.01
            ax1.plot(x, eval(y), "o", markersize=7, markeredgewidth=1, markeredgecolor='g',markerfacecolor='None')
    count = 0
    '''for zero in numzero:
        if zero in undef:
            ax1.plot(zero, f(zero), marker='s', color='green')
        count = count + 1'''
    #ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    #plt.axis([0,6,0,30])
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/graph.png', bbox_inches = 'tight')

    #############################################
    # Relative Extrema
    #############################################

    xRange2 = np.arange(x1, x2, 0.01)
    count = 0
    yRange2 = np.empty(xRange2.size)
    for x in np.nditer(xRange2):
        yRange2[count] = diff(y, x)
        count = count + 1
    xVal2 = xRange2.tolist()
    yVal2 = yRange2.tolist()
    ax1.plot(xVal2, yVal2, 'r', alpha=0.2)
    # ax2.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    count = 1
    limit = len(yVal2) - 1
    for z in yVal2:
        if count == limit:
            break
        if (yVal2[count - 1]>0 and yVal2[count + 1]<0):
            ax1.plot(xVal1[count], yVal1[count], marker='s', color='c')
            ax1.axvline(x=xVal1[count], linestyle='--')
        count = count + 1
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/relmax.png', bbox_inches='tight')
    plt.clf()

    xRange1 = np.arange(x1, x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count + 1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')

    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(xVal1, yVal1,'g')
    # ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')

    xRange2 = np.arange(x1, x2, 0.01)
    count = 0
    yRange2 = np.empty(xRange2.size)
    for x in np.nditer(xRange2):
        yRange2[count] = diff(y, x)
        count = count + 1
    xVal2 = xRange2.tolist()
    yVal2 = yRange2.tolist()
    ax1.plot(xVal2, yVal2, 'r', alpha=0.2)
    # ax2.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    count = 1
    limit = len(yVal2) - 1
    for z in yVal2:
        if count == limit:
            break
        if (yVal2[count - 1] < 0 and yVal2[count + 1] > 0):
            ax1.plot(xVal1[count], yVal1[count], marker='s', color='c')
            ax1.axvline(x=xVal1[count], linestyle='--')
        count = count + 1
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/relmin.png', bbox_inches='tight')
    plt.clf()


    #############################################
    # First Derivative
    #############################################

    xRange1 = np.arange(x1,x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count+1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2,2,1)
    ax1.plot(xVal1, yVal1, 'g')
    #ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    xRange2 = np.arange(x1, x2, 0.01)
    count = 0
    yRange2 = np.empty(xRange2.size)
    for x in np.nditer(xRange2):
        yRange2[count] = diff(y,x)
        count = count+1
    xVal2 = xRange2.tolist()
    yVal2 = yRange2.tolist()
    ax1.plot(xVal2, yVal2, 'r')
    #ax2.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    if d == 1:
        plt.xlim(left=x1, right=x2)
        plt.ylim(top=y2, bottom=y1)
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/deriv_graph.png', bbox_inches = 'tight')

    #############################################
    # SECOND DERIVATIVE
    #############################################
    xRange1 = np.arange(x1, x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count + 1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(xVal1, yVal1, 'g')
    # ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    xRange2 = np.arange(x1, x2, 0.01)
    count = 0
    yRange2 = np.empty(xRange2.size)
    for x in np.nditer(xRange2):
        yRange2[count] = diff(y, x)
        count = count + 1
    xVal2 = xRange2.tolist()
    yVal2 = yRange2.tolist()
    ax1.plot(xVal2, yVal2, 'r')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    xRange3 = np.arange(x1, x2, 0.01)
    yRange3 = np.empty(xRange3.size)
    '''for x in np.nditer(xRange3):
        yRange3[count] = diff2(y, x)
        count = count + 1'''
    count = 1
    limit = yRange2.size-1
    for x in np.nditer(xRange3):
        if count == limit:
            break
        yRange3[count] = diff2(yRange2[count-1], yRange2[count+1])
        count = count + 1
    np.delete(xRange3, -1)
    np.delete(yRange3, -1)
    xVal3 = xRange3.tolist()
    yVal3 = yRange3.tolist()
    print("XXXXXXXXXX")
    for x in xVal3:
        print (x)
    print("YYYYYYYYYY")
    for yVal in yVal3:
        print (yVal)
    ax1.plot(xVal3, yVal3, 'b')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    if d == 1:
        plt.xlim(left=x1, right=x2)
        plt.ylim(top=y2, bottom=y1)
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/deriv2_graph.png', bbox_inches='tight')
    plt.clf
    #############################################
    #POINTS OF INFLECTION
    #############################################
    xRange1 = np.arange(x1, x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count + 1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(xVal1, yVal1, 'g')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    xRange2 = np.arange(x1, x2, 0.01)
    count = 0
    yRange2 = np.empty(xRange2.size)
    for x in np.nditer(xRange2):
        yRange2[count] = diff(y, x)
        count = count + 1
    xVal2 = xRange2.tolist()
    yVal2 = yRange2.tolist()
    ax1.plot(xVal2, yVal2, 'r', alpha=0.2)
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    xRange3 = np.arange(x1, x2, 0.01)
    yRange3 = np.empty(xRange3.size)
    count = 1
    limit = yRange2.size - 1
    for x in np.nditer(xRange3):
        if count == limit:
            break
        yRange3[count] = diff2(yRange2[count - 1], yRange2[count + 1])
        count = count + 1
    np.delete(xRange3, -1)
    np.delete(yRange3, -1)
    xVal3 = xRange3.tolist()
    yVal3 = yRange3.tolist()
    ax1.plot(xVal3, yVal3, 'b', alpha=0.2)
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    if d == 1:
        plt.xlim(left=x1, right=x2)
        plt.ylim(top=y2, bottom=y1)

    count = 1
    limit = len(yVal2) - 1
    for z in yVal3:
        if count == limit:
            break
        if yVal3[count - 1] < 0 and yVal3[count + 1] > 0:
            points1 = ax1.plot(xVal2[count], yVal1[count], marker='s', color='c')
            ax1.axvline(x=xVal2[count], linestyle='--')
        count = count + 1
    count = 1
    limit = len(yVal2) - 1
    for z in yVal3:
        if count == limit:
            break
        if yVal3[count - 1] > 0 and yVal3[count + 1] < 0:
            points1 = ax1.plot(xVal2[count], yVal1[count], marker='s', color='c')
            ax1.axvline(x=xVal2[count], linestyle='--')
        count = count + 1
    if d == 1:
        plt.xlim(left=x1, right=x2)
        plt.ylim(top=y2, bottom=y1)
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/poi.png', bbox_inches='tight')
    plt.clf()

    #############################################
    # FTC
    #############################################
    xRange1 = np.arange(x1, x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    n, d = yParsed.as_numer_denom()
    undef = sympy.solve(d)
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)
    plt.autoscale(False)
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count + 1
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(xVal1, yVal1, 'g')
    n, d = yParsed.as_numer_denom()
    s = Symbol('s', real=True)
    undef = sympy.solve(d, s)
    for xc in undef:
        ax1.axvline(x=xc, linestyle='--')
    print("Integration x1:")
    x1int = float(input())
    print("Integration x2:")
    x2int = float(input())
    print("Processing...")
    sectionx = np.arange(x1int, x2int, 0.00001)
    sectiony = np.empty(sectionx.size)
    count = 0
    for x in np.nditer(sectionx):
        sectiony[count] = eval(y)
        count = count+1
    plt.fill_between(sectionx, sectiony)
    area = 0
    count = 0
    limit = sectionx.size-1
    for x in np.nditer(sectionx):
        if(count == limit):
            break
        trapSum = trapz(sectiony[count], sectiony[count+1])
        area = area + trapSum
        count = count + 1
    print(area)
    # ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    if d == 1:
        plt.xlim(left=x1, right=x2)
        plt.ylim(top=y2, bottom=y1)
    plt.xlim(left=x1, right=x2)
    plt.ylim(top=y2, bottom=y1)
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/ftc.png', bbox_inches='tight')

area=0

x1 = -5;
x2 = 5;
xRange1 = np.arange(x1,x2, 0.01)
print("1st input")
y=input()
yParsed = parse_expr(y, evaluate=False)
functionGraph(y)

##############################################
#works on CHROME ONLY, caching issue in Safari
##############################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
            input = request.form['Function']
            print(input)
    #functionGraph(input)
    return render_template("graph.html")
    #return render_template("graph.html", result=input)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    return render_template('input.html')

'''@app.route('/input', methods=['GET', 'POST'])
def input_post():
    if request.method == 'POST':
        result = request.form['Function']
        print(result)
        return render_template("graph.html", result=result)'''

@app.route('/der', methods=['GET', 'POST'])
def derGraph():
    return render_template('graph2.html')

@app.route('/der2', methods=['GET', 'POST'])
def der2Graph():
    return render_template('graph3.html')

@app.route('/relmax', methods=['GET', 'POST'])
def relmax():
    return render_template('relmax.html')

@app.route('/relmin', methods=['GET', 'POST'])
def relmin():
    return render_template('relmin.html')

@app.route('/poi', methods=['GET', 'POST'])
def poi():
    return render_template('poi.html')

@app.route('/ftc', methods=['GET', 'POST'])
def ftc():
    return render_template('ftc.html')

@app.route('/in1', methods=['GET', 'POST'])
def in1():
    return render_template('in1.html')

@app.route('/out1', methods=['GET', 'POST'])
def out1():
    return render_template('out1.html')

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


