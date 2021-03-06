#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for key, value in self.items():
            all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        # Collect all values in each of the buckets
        all_values = []
        for key, value in self.items():  # items()
            all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.as_list())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: need to check the whole list for item
        pair = bucket.find(lambda pair: pair[0] == key)
        return pair is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        # if not self.contains(key):
        #     raise KeyError('Key not found')
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        pair = bucket.find(lambda pair: pair[0] == key)
        # assoc_value = bucket.find(lambda pair: pair[1] if pair[0]==key)
        # print 'assoc value:', assoc_value

        if pair is None:
            raise KeyError('Key not found')
        value = pair[1]
        return value

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # Insert or update the given key-value entry into a bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # check if value already exists
        if self.contains(key):
            self.delete(key)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        pair = bucket.find(lambda pair: pair[0] == key)

        if pair is None:
            raise KeyError('Key not found')
        else:
            bucket.delete(pair)


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Length of table:')
    print(ht.length())

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))
    print 'Hash table as list: ', ht.items()
    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))

    print 'Hash table as list: ', ht.items()


if __name__ == '__main__':
    test_hash_table()
