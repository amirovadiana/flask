import requests


response = requests.post(
    'http://127.0.0.1:5000/advertisements/',
    json={
        'title': 'Piano for sale at a low price',
        'description': 'Here is the description of the advertisement',
        'author': 'Ivanova Svetlana'
    }
    )

response = requests.post(
    'http://127.0.0.1:5000/advertisements/',
    json={
        'title': 'English language course',
        'description': 'Here is the description of the advertisement',
        'author': 'Markov Anton'
    }
    )

response = requests.post(
    'http://127.0.0.1:5000/advertisements/',
    json={
        'title': 'Alabai puppies for sale',
        'description': 'Here is the description of the advertisement',
        'author': 'Steclova Karina'
    }
    )

# response = requests.post(
#     'http://127.0.0.1:5000/advertisements/',
#     json={
#         'title': 'Exchange interesting books',
#         'description': 'Here is the description of the advertisement',
#     }
#     )

# response = requests.post(
#     'http://127.0.0.1:5000/advertisements/',
#     json={
#         'title': 'Exchange interesting books. We prioritize the following genres: detective stories, classic literature. Editions published no later than 2000 will be considered',
#         'description': 'Here is the description of the advertisement',
#         'author': 'Steclova Karina'
#     }
#     )

response = requests.patch(
    'http://127.0.0.1:5000/advertisements/3',
    json={
        'title': 'Alabai puppies for free in good homes',
        'description': 'Here is the description of the advertisement',
        'author': 'Steclova Karina'
    }
    )

# response = requests.get(
#     'http://127.0.0.1:5000/advertisements/',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/advertisements/1',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/advertisements/2',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/advertisements/3',
#     )

# response = requests.delete(
#     'http://127.0.0.1:5000/advertisements/1',
#     )

# response = requests.get(
#     'http://127.0.0.1:5000/advertisements/1',
#     )


print(response.json())
print(response.status_code)
