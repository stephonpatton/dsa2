# TODO: Truck needs route data
from distances import wgu_graph
from package import package_hashtable


class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.start_time = []
        self.current_time = []
        self.end_time = []

    def load_package(self, package):
        self.packages.append(package)
        self.route.append(package[1])
        print("Package" + package[1] + " added")


truck1_route = []
truck2_route = []
truck3_route = []

truck1_packages = []
truck2_packages = []
truck3_packages = []


def check_truck_number(package_to_check):
    temp = ''
    if package_to_check[9] == '1':
        # print("TRUCK 1")
        temp = '1'
    elif package_to_check[9] == '2':
        # print("TRUCK 2")
        temp = '2'
    else:
        # print("TRUCK 3")
        temp = '3'

    return temp


def load_all_trucks():
    for i in range(1, 40):
        temp1 = check_truck_number(package_hashtable.search(i))
        temp_pack = package_hashtable.search(i)
        # print("VALUE " + str(temp1))
        if temp1 == '1':
            # truck1_route.append(temp_pack[1])
            # truck1_packages.append(temp_pack)
            truck1.load_package(temp_pack)
        elif temp1 == '2':
            # truck2_route.append(temp_pack[1])
            # truck2_packages.append(temp_pack)
            truck2.load_package(temp_pack)
        else:
            # truck3_route.append(temp_pack[1])
            # truck3_packages.append(temp_pack)
            truck3.load_package(temp_pack)


def find_distance_diff(address1, address2):
    distance = float(wgu_graph.edge_weights[address1, address2])
    print(distance)


truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


pack = package_hashtable.search(1)
print(pack[8])
print(package_hashtable.search(1))
print(truck1.route)
print(truck1.packages)
# truck1.check_truck_number(package_hashtable.search(10))
# print(truck1.packages)
# temp1 = check_truck_number(package_hashtable.search(11))
# print("TEMP!" + temp1)
load_all_trucks()
truck1.packages.append(truck1_packages)
print("TRUCK 1 ROUTE")
print(truck1_route)
print(truck1_packages)
print("TRUCK 2 ROUTE")
print(truck2_packages)
print(truck2_route)
print("TRUCK 3 ROUTE")
print(truck3_route)
print(truck3_packages)
print(truck1.packages)
print(truck1.route)
print(truck2.packages)
print(truck2.route)
print(truck3.packages)
print(truck3.route)

for i in range(len(wgu_graph.edge_weights)):
    print(truck1.route[i] + truck1.route[i+1])
    print(find_distance_diff(truck1.route[i], truck1.route[i+1]))

print(wgu_graph.edge_weights)


