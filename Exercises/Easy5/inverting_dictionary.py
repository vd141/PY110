def invert_dict(hashmap):
    '''
    invert this dictionary so that its keys become values and its
    values become keys, assuming keys and values are unique
    '''

    keys = hashmap.keys()
    values = hashmap.values()

    zipped = zip(values, keys)

    return dict(zipped)

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True