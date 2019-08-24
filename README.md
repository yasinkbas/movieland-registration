# Movieland
This project uses Django2.2.4 | python 3.7 | rest_framework3.10


## Registration

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /auth/register/ | `POST` | { username: 'foo', email: 'email@mail.com', password1:'1234' password2:'1234' } | Create a new user. Generate a token.|
| /auth/login/ | `POST` | { username: 'foo', password:'1234' } | Generate a token. |
| /auth/logout/ | `POST` | Empty | Remove token |

## Movies (Must be authenticated with Token)

| Route | HTTP Verb	| POST body	| Description |
| --- | --- | --- | --- |
| /movies/ | `GET` | Empty | List all movies. |
| /movies | `POST` | {'title':'foo', 'imdb':7.5, 'director':director_id,'image':image file, isPublish: true } | Create a new movie. |
| /movies/:movie_id | `GET` | Empty | Get the movie. |
| /movies/:movie_id | `PUT` | {'title':'foo', 'imdb':7.5,'director':director_id,'image': image file, isPublish: true} | Update the movie with new info. |
| /movies/:movie_id | `DELETE` | Empty | Delete a movie. |
| /movies/newest/ | `GET` | Empty | Get the newest movie. |
| /movies/published/ | `GET` | Empty | Get the published movies. |
| /api/movies/?title__icontains=:[query_title] | `GET` | Empty | Get all result which ones include the query in title |
| /api/movies/?imdb__gte=:[query_imdb] | `GET` | Empty | Get all result which ones greater than query imdb |

## Directors (Must be authenticated with Token)

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /directors/ | `GET` | Empty | List all directors. |
| /directors/ | `POST` | { name: 'foo' } | Create a new director. | 
| /directors/:director_id | `GET` | Empty | Get the director. |
| /directors/:director_id | `PUT` | {'name':'foo'} | Update the director with new info. |
| /directors/:director_id | `DELETE` | Empty | Delete the director. |

## Users (Must be authenticated with Token)

| Route | HTTP Verb | POST body	 | Description	 |
| --- | --- | --- | --- |
| /users/ | `GET` | Empty | List all users. |
| /users/:user_id | `GET` | Empty | Get a user. |

## Installation
```shell
$ virtualenv venv -p python3
$ sourve venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

## If you want to deploy heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/yasinkbas/movieland-registration)