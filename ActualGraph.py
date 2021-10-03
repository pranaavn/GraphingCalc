from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt, mpld3
app = Flask(__name__)

@app.route("/")
def calc():
    message = "Graphing Calculator"
    plt.plot([3, 1, 4, 1, 5], 'ks-', mec='w', mew=5, ms=20)
    plt.show()
    plt.savefig('deriv_graph.png')
    return render_template("graph.html", message = message)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)