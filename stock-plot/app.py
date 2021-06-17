import matplotlib.pyplot as plt
import csv
from flask import Flask

app = Flask(__name__)

x = []
y = []

@app.route("/")
def plot():


    with open('returns.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))

    plt.plot(x, y, color = 'g', linestyle = 'dashed',
            marker = 'o',label = "Stock Returns")

    plt.xticks(rotation = 25)
    plt.xlabel('Dates')
    plt.ylabel('Returns')
    plt.title('SWAT Fin Exp', fontsize = 20)
    # plt.grid()
    # plt.legend()
    # final_output = plt.show()

    return plt.show()


if __name__ == "__main__":
    app.run()