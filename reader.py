import csv

def load_network_traffic():
    with open('network_traffic.log','r') as f:
        reader = csv.reader(f)
        return list(reader)
    