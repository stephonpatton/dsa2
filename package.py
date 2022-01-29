import csv

from hashtable_ds import ChainingHashTable


def load_package_data(file):
    packages = ChainingHashTable()
    with open(file) as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None)
        for row in csv_reader:
            pack_id = int(row[0])
            pack_address = row[1]
            pack_city = row[2]
            pack_state = row[3]
            pack_zip = row[4]
            pack_deadline = row[5]
            pack_weight = row[6]
            pack_notes = row[7]
            pack_status = 'At Hub'
            pack_truck = row[8]
            pack_time = ''

            temp_list = [pack_id, pack_address, pack_city, pack_state, pack_zip, pack_deadline, pack_weight, pack_notes,
                         pack_status, pack_truck, pack_time]

            k = pack_id
            v = temp_list

            packages.insert(k, v)
        return packages


def print_search_result(package_id):
    result = package_hashtable.search(package_id)
    print(result)


def print_all():
    for i in range(41):
        print_search_result(i)


print("---------")


def print_truck_count(truck):
    for i in range(41):
        one = package_hashtable.search(i)
        if one[9] == '1':
            print(True)


package_hashtable = load_package_data("packageCSV.csv")

# print_search_result(3)
# print_all()
