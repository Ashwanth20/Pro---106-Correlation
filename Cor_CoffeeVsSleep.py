import csv
import numpy as np

def data(data_path):
    graph = []
    bar = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            graph.append(float(row["Coffee in ml"]))
            bar.append(float(row["sleep in hours"]))
    return{"x": graph, "y": bar}
def correlate(DataSource):
    correlation = np.corrcoef(DataSource["x"],DataSource["y"])
    print(correlation[0,1])
def line():
    data_path = "CoffeeVsSleep.csv"
    DataSource = data(data_path)
    correlate(DataSource)
line()