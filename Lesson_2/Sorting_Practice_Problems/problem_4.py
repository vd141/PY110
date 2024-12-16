'''
sort the list of dicts based on the year of publication of each book, from earliest
to most recent?
'''

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def publish_key(dictionary):
    return int(dictionary['published'])

print(sorted(books, key=publish_key))