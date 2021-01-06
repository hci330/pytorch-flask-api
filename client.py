import requests

url = 'http://localhost:5000/predict'
dir = '/Users/vanwars/northwestern/cs330/msai-demos/pytorch-flask-api/samples/'
images = [
    'cat1.jpg', 'lani.jpg', 'seamus.jpg', 'seamus1.jpg',
    'froggie.jpg', 'scout.jpg'
]

# header:
print('-' * 50)
print('{0:>15} | {1}'.format('Image', 'Classification'))
print('-' * 50)

for img in images:
    path = dir + img
    resp = requests.post(
        url,
        files={"file": open(path,'rb')})
    try:
        print('{0:>15} | {1}'.format(img, resp.json().get('class_name').replace('_', ' ')))
    except:
        print(resp.text)

# footer:
print('-' * 50)
