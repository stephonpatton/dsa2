# Chaining HashTable from ZyBook

class ChainingHashTable:
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=10):
        # Initialize hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts new item into the hash table
    def insert(self, package_id, package):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == package_id:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [package_id, package]
        bucket_list.append(key_value)
        return True

    # Searches for an item with given key in the hash table
    # Returns the item if found, None if not found
    def search(self, key):
        # Get bucket where key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for key in bucket
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

