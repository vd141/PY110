def count_occurrences(vehicles):
    '''
    write a functino that counts the number of occurrences ofeach element in a
    given list. once counted, print each element alongside the number of occurrences.
    consider the words case sensitive e.g. (sub != SUV)

    store all vehicles in a dict with vehicle name as key and vehicle count as
    value
    '''

    vehicle_count = {}

    for vehicle in vehicles:
        vehicle_count[vehicle] = vehicle_count.get(vehicle, 0) + 1

    for count in vehicle_count:
        print(f'{count} ==> {vehicle_count[count]}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
    'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)