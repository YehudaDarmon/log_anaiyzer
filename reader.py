import csv

def load_network_traffic(path):
    with open(path ,'r') as f:
        reader = list(csv.reader(f))
        return reader

def external_addresses(data):
    external_addresses_list = [i for i in data if not (i[1].startswith("192") or i[1].startswith("10"))]
    return external_addresses_list

def sensitive_port(data):
    sensitive_port_list = [i for i in data if (i[3] == '22' or i[3] == '23' or i[3] == '3389')]
    return sensitive_port_list

def filter_by_size(data):
    filter_by_size_list = [i for i in data if int(i[5]) > 5000]
    return filter_by_size_list

def package_size(data):
    package_size_list = []
    for i in data:
        if int(i[5]) >= 5000:
            i.append('LARGE')
            package_size_list.append(i)
        else:
            i.append('NORMAL')
            package_size_list.append(i)
    return package_size_list