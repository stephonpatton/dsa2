# TODO: Truck needs route data
import package
from distances import wgu_graph
from package import package_hashtable
from greedy_algorithm import greedy_algorithm, greedy_algorithm_distance, get_total_distance
from datetime import timedelta, datetime, time
from collections import Counter
import time


class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.speed = 0.2999  # 18mph to miles per minute
        self.start_time = None
        self.current_time = None
        self.end_time = None
        self.total_distance = 0

    def load_package(self, package):
        self.packages.append(package)
        self.route.append(package[1])
        # print("Package #" + str(package[0]) + " added")

    def add_distance(self, num):
        self.total_distance += num

    def remove(self, package):
        self.packages.remove(package)
        # self.route.remove(package[1])


truck1_route = []
truck2_route = []
truck3_route = []

truck1_packages = []
truck2_packages = []
truck3_packages = []

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


def check_truck_number(package_to_check):
    temp = ''
    if package_to_check[9] == '1':
        temp = '1'
    elif package_to_check[9] == '2':
        temp = '2'
    else:
        temp = '3'

    return temp


def load_all_trucks():
    for i in range(1, 41):
        temp1 = check_truck_number(package_hashtable.search(i))
        temp_pack = package_hashtable.search(i)
        if temp1 == '1':
            truck1.load_package(temp_pack)
        elif temp1 == '2':
            truck2.load_package(temp_pack)
        else:
            truck3.load_package(temp_pack)


def simulate_package_delivery():
    truck1.start_time = datetime(2022, 1, 10, 8, 0)
    truck3.start_time = datetime(2022, 1, 10, 8, 0)

    # load_all_trucks()
    truck1.packages.append(truck1_packages)
    truck1.route.append(truck1_packages)
    truck1.route.pop()
    truck1.packages.pop()

    best_route1 = greedy_algorithm(truck1.route)
    best_route2 = greedy_algorithm(truck2.route)
    best_route3 = greedy_algorithm(truck3.route)

    best_route1.append('4001 South 700 East')
    # best_route2.append('410 S State St')
    # best_route2.append('4001 South 700 East')
    best_route3.append('4001 South 700 East')
    truck1.current_time = truck1.start_time
    # print("Delivering for truck1...")
    # print("Start time is: " + str(truck1.start_time))
    truck_delivery(truck1, best_route1)

    # print("Delivering for truck3...")
    # print("Start time is: " + str(truck3.start_time))
    truck3.current_time = truck3.start_time
    truck_delivery(truck3, best_route3)

    truck2.start_time = truck3.end_time
    truck2.current_time = truck2.start_time
    # print("Delivering for truck2...")
    # print("Start time is: " + str(truck2.start_time))
    truck_delivery(truck2, best_route2)


def show_metrics(truck1_distance, truck2_distance, truck3_distance):
    print("Delivery complete for all trucks!")
    print("Truck1 metrics\n------------------------------")
    print("Departure Time: " + str(truck1.start_time))
    print("Return Time: " + str(truck1.end_time))
    truck1_time_hour = truck1.end_time.hour - truck1.start_time.hour
    truck1_time_min = truck1.end_time.minute - truck1.start_time.minute
    if truck1_time_min < 0:
        truck1_time_hour -= 1
        truck1_time_min = 60 - abs(truck1_time_min)
    print("Drive Time: " + str(truck1_time_hour) + " hour(s) and " + str(truck1_time_min) + " minutes")
    print("Truck1 Distance: " + str(truck1_distance))

    print("\nTruck2 (Truck3 Second Trip) metrics\n------------------------------")
    print("Departure Time: " + str(truck2.start_time))
    print("Return Time: " + str(truck2.end_time))
    truck2_time_hour = truck2.end_time.hour - truck2.start_time.hour
    truck2_time_min = truck2.end_time.minute - truck2.start_time.minute
    if truck2_time_min < 0:
        truck2_time_hour -= 1
        truck2_time_min = 60 - abs(truck2_time_min)
    print("Drive Time: " + str(truck2_time_hour) + " hour(s) and " + str(truck2_time_min) + " minutes")
    print("Truck2 Distance: " + str(truck2_distance))

    print("\nTruck3 metrics\n------------------------------")
    print("Departure Time: " + str(truck3.start_time))
    print("Return Time: " + str(truck3.end_time))
    truck3_time_hour = truck3.end_time.hour - truck3.start_time.hour
    truck3_time_min = truck3.end_time.minute - truck3.start_time.minute
    print("Drive Time: " + str(truck3_time_hour) + " hour(s) and " + str(truck3_time_min) + " minutes")
    print("Truck3 Distance: " + str(truck3_distance))

    combined_hours = truck1_time_hour + truck2_time_hour + truck3_time_hour
    combined_min = truck1_time_min + truck2_time_min + truck3_time_min

    distance = truck1_distance + truck2_distance + truck3_distance

    print("\nCombined mileage for all trucks: " + str(round(distance, 1)))
    print("Time to deliver all packages: " + str(combined_hours) + " hours and " + str(combined_min) + " minutes")


def deliver_package(point_a, point_b, truck):
    dist_between = wgu_graph.edge_weights[point_a, point_b]
    truck.add_distance(dist_between)
    delt = timedelta(minutes=dist_between / truck.speed)
    newest_time = truck.current_time + delt
    truck.current_time = newest_time
    return truck.current_time


def mark_as_delivered(package, time):
    package[8] = 'Delivered'
    package[10] = str(time)


def show_packages_at_time(time):
    delivered_packages = []
    for index in range(1, 41):
        pack = package_hashtable.search(index)
        if pack in truck1.packages:
            if str(time) > pack[10]:
                delivered_packages.append(
                    "Package #" + str(pack[0]) + " Delivered at " + str(pack[10]) + " STATUS: " + str(pack[8]))
                index += 1
            elif str(time) < pack[10]:
                delivered_packages.append("Package #" + str(pack[0]) + " " + 'STATUS: En Route')
        if pack in truck3.packages:
            if str(time) > pack[10]:
                delivered_packages.append(
                    "Package #" + str(pack[0]) + " Delivered at " + str(pack[10]) + " STATUS: " + str(pack[8]))
                index += 1
            elif str(time) < pack[10]:
                delivered_packages.append("Package #" + str(pack[0]) + " " + 'STATUS: En Route')

        if pack in truck2.packages:
            if str(time) > pack[10]:
                delivered_packages.append(
                    "Package #" + str(pack[0]) + " Delivered at " + str(pack[10]) + " STATUS: " + str(pack[8]))
            elif pack[10] > str(time) > str(truck2.start_time):
                delivered_packages.append("Package #" + str(pack[0]) + " " + 'STATUS: En Route')
            else:
                delivered_packages.append("Package #" + str(pack[0]) + " " + 'STATUS: At the Hub')

    print(*delivered_packages, sep="\n")


def truck_delivery(truck, optimal_route):
    temp_list = {}
    for pack in truck.packages:
        for location in optimal_route:
            if location not in temp_list:
                temp_list[location] = 0
            if location in temp_list and pack[1] == location:
                temp_list[location] += 1
    temp_list.pop('4001 South 700 East')
    index = 0
    for address in range(len(optimal_route)):
        str_address = optimal_route[address]
        if index == len(optimal_route) - 1:
            break
        else:
            if str_address == '4001 South 700 East':
                continue
            if temp_list.get(str_address) > 1:
                delivery_list = []

                for pack in truck.packages:
                    if pack[1] == optimal_route[address]:
                        delivery_list.append(pack[0])

                for delivery in delivery_list:
                    mark_as_delivered(package_hashtable.search(delivery), truck.current_time)
                truck.current_time = deliver_package(optimal_route[address], optimal_route[address + 1], truck)
                index = index + 1

            elif temp_list.get(str_address) == 1:
                deli_list = []
                for pack in truck.packages:
                    if pack[1] == optimal_route[address]:
                        deli_list.append(pack[0])

                for delivery in deli_list:
                    mark_as_delivered(package_hashtable.search(delivery), truck.current_time)

                truck.current_time = deliver_package(optimal_route[index], optimal_route[index + 1], truck)
                index = index + 1

    truck.end_time = truck.current_time
