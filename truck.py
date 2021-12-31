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


# wgu_graph.add_to_adjacency_list(package_hashtable)
# print(wgu_graph.adjacency_list)
# wgu_graph.put_packages_in_delivery_dict(package_hashtable)
truck1 = Truck()
truck1.load_package(package_hashtable.search(2))
