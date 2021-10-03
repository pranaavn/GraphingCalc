from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
from DerivTest import diff, diff2
from ParsingClass import Parser

#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

def functionGraph():
    global formInput
    parser = Parser()
    #x=np.array(range(10))
    x1 = -5;
    x2 = 5;
    xRange1 = np.arange(x1,x2, 0.01)
    print("1st input")
    #y=formInput
    y='5*x**2'
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count+1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    #plt.plot(xRange1, y)
    print(xRange1.size)
    print(yRange1.size)
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2,2,1)
    ax1.plot(xVal1, yVal1)
    #ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    #plt.axis([0,6,0,30])
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/graph.png', bbox_inches = 'tight')

    #############################################
    # Relative Extrema
    #############################################

    count=1
    limit = len(yVal1)-1
    for z in yVal1:
        if count == limit:
            break
        if yVal1[count-1]<yVal1[count] and yVal1[count+1]<yVal1[count]:
            print(yVal1[count-1])
            print(yVal1[count])
            print(yVal1[count+1])
            points1 = ax1.plot(xVal1[count], yVal1[count], marker='s', color = 'green')
        count = count+1
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/relmax.png', bbox_inches = 'tight')
    plt.clf()

    x1 = -5;
    x2 = 5;
    xRange1 = np.arange(x1,x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count+1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    #plt.plot(xRange1, y)
    print(xRange1.size)
    print(yRange1.size)
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2,2,1)
    ax1.plot(xVal1, yVal1)
    #ax1.set_aspect('equal')
    ax1.grid(True, which='both')
    ax1.axhline(y=0, color='k')
    ax1.axvline(x=0, color='k')
    count=1
    limit = len(yVal1)
    for q in yVal1:
        if count == limit:
            break
        if yVal1[count-1]>yVal1[count] and yVal1[count+1]>yVal1[count]:
            print(yVal1[count-1])
            print(yVal1[count])
            print(yVal1[count+1])
            points2 = ax1.plot(xVal1[count], yVal1[count], marker='s', color = 'green')
        count = count + 1
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/relmin.png', bbox_inches = 'tight')
    plt.clf()

    #############################################
    # First Derivative
    #############################################

    x1 = -5;
    x2 = 5;
    xRange1 = np.arange(x1,x2, 0.01)
    yRange1 = np.empty(xRange1.size)
    count = 0
    for x in np.nditer(xRange1):
        yRange1[count] = eval(y)
        count = count+1
    plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    #plt.plot(xRange1, y)
    print(xRange1.size)
    print(yRange1.size)
    xVal1 = xRange1.tolist()
    yVal1 = yRange1.tolist()
    ax1 = plt.subplot(2,2,1)
    ax1.plot(xVal1, yVal1)
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
    ax2 = plt.subplot(2,2,1)
    ax2.plot(xVal2, yVal2)
    #ax2.set_aspect('equal')
    ax2.grid(True, which='both')
    ax2.axhline(y=0, color='k')
    ax2.axvline(x=0, color='k')
    print(yRange2[1])
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/deriv_graph.png', bbox_inches = 'tight')

#############################################
#POINTS OF INFLECTION
#############################################
    count = 1
    limit = len(yVal2) - 1
    for z in yVal2:
        if count == limit:
            break
        if yVal2[count - 1] < yVal2[count] and yVal2[count + 1] < yVal2[count]:
            print(yVal2[count - 1])
            print(yVal2[count])
            print(yVal2[count + 1])
            points1 = ax1.plot(xVal2[count], yVal1[count], marker='s', color = 'green')
            ax1.arrow(xVal2[count], yVal1[count], xVal2[count], yVal2[count], linestyle='--')
        count = count + 1
    count = 1
    limit = len(yVal2) - 1
    for z in yVal2:
        if count == limit:
            break
        if yVal2[count - 1] > yVal2[count] and yVal2[count + 1] > yVal2[count]:
            print(yVal2[count - 1])
            print(yVal2[count])
            print(yVal2[count + 1])
            points1 = ax1.plot(xVal2[count], yVal1[count], marker='s', color = 'green')
            ax1.arrow(2, 2, -1, -1, linestyle='--')
        count = count + 1
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/poi.png', bbox_inches='tight')
    plt.clf()

    #############################################
    # SECOND DERIVATIVE
    #############################################

    xRange3 = np.arange(x1, x2, 0.01)
    #print("2nd input")
    #y = StringFunction(input())
    count = 0
    yRange3 = np.empty(xRange3.size)
    for x in np.nditer(xRange3):
        yRange3[count] = diff2(y,x)
        count = count+1
    xVal3 = xRange3.tolist()
    yVal3 = yRange3.tolist()
    ax3 = plt.subplot(2,2,1)
    ax3.plot(xVal3, yVal3)
    #ax2.set_aspect('equal')
    ax3.grid(True, which='both')
    ax3.axhline(y=0, color='k')
    ax3.axvline(x=0, color='k')
    print(yRange3[1])
    plt.savefig('/Users/pranav/PycharmProjects/Main/GraphCalcImplementation/static/images/deriv2_graph.png', bbox_inches = 'tight')


##############################################
#works on CHROME ONLY, caching issue in Safari
##############################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/graph', methods=['GET', 'POST'])
def graph():
    global formInput
    print("Entering path '/graph'")
    if request.method == 'POST':
        formInput = request.form['Function']
    functionGraph()
    print("Done with functionGraph()")
    print(formInput)
    return render_template("graph.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
    print("Entering path '/home'")
    return render_template('home.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    print("Entering path '/input'")
    return render_template('input.html')

'''@app.route('/input', methods=['GET', 'POST'])
def input_post():
    if request.method == 'POST':
        result = request.form['Function']
        print(result)
        return render_template("graph.html", result=result)'''

@app.route('/der', methods=['GET', 'POST'])
def derGraph():
    print("Entering path '/der'")
    return render_template('graph2.html')

@app.route('/der2', methods=['GET', 'POST'])
def der2Graph():
    print("Entering path '/der2'")
    return render_template('graph3.html')

@app.route('/relmax', methods=['GET', 'POST'])
def relmax():
    print("Entering path '/relmax'")
    return render_template('relmax.html')

@app.route('/relmin', methods=['GET', 'POST'])
def relmin():
    print("Entering path '/relmin'")
    return render_template('relmin.html')

'''@app.after_request
def add_header(response):
    print("Entering path '/add_header'")
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response'''

def main():
    global formInput
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    main()


