from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

exampleFile = open('apple dec sample set.csv')
exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)

labels = []
values = []



@app.route("/")
def chart():
	for row in exampleReader:
		labels.append(row[0])
		values.append(row[1])
	return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run()