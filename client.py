import requests


response = requests.post(
    'http://127.0.0.1:5000/all_advertisements/',
    json={
        'title': 'Piano for sale at a low price',
          'author': 'Ivanova Svetlana'
    }
    )

response = requests.post(
    'http://127.0.0.1:5000/all_advertisements/',
    json={
        'title': 'English language course',
          'author': 'Markov Anton'
    }
    )

response = requests.post(
    'http://127.0.0.1:5000/all_advertisements/',
    json={
        'title': 'Alabai puppies for sale',
          'author': 'Steclova Karina'
    }
    )

# response = requests.post(
#     'http://127.0.0.1:5000/all_advertisements/',
#     json={
#         'title': 'Exchange interesting books',
#     }
#     )

# response = requests.post(
#     'http://127.0.0.1:5000/all_advertisements/',
#     json={
#         'title': 'Exchange interesting books. We prioritize the following genres: detective stories, classic literature. Editions published no later than 2000 will be considered',
#         'author': 'Steclova Karina'
#     }
#     )

response = requests.patch(
    'http://127.0.0.1:5000/all_advertisements/3',
    json={
        'title': 'Alabai puppies for free in good homes',
        'author': 'Steclova Karina'
    }
    )

# response = requests.get(
#     'http://127.0.0.1:5000/all_advertisements/1',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/all_advertisements/2',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/all_advertisements/3',
#     )

# response = requests.delete(
#     'http://127.0.0.1:5000/all_advertisements/1',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/all_advertisements/1',
#     )


print(response.json())
print(response.status_code)
