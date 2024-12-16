'''
write a function that returns a string that contains a UUID
'''
import random

HEXADECIMAL = '0123456789abcdef'
UUID_CLUSTERS = [8, 4, 4, 4, 12]

def select_random_hex():
    return random.choice(HEXADECIMAL)

def return_UUID():
    uuid_list = []
    for cluster_length in UUID_CLUSTERS:
        cluster = ''
        for _ in range(cluster_length):
            cluster += select_random_hex()
        uuid_list.append(cluster)
    return '-'.join(uuid_list)

print(return_UUID())