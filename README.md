# AdEase API
This project is designed to serve as a MVP for Adease. Built with Python, Flask, Celery, Redis & MongoDB

## Configuration
Below are the steps required to run this app

Create a virtual env and activate it
```
python3 -m venv /path-to-project/venv
source ./venv/bin/activate
```

Install requirements
`pip install -r requirements.txt`

Run flask app (in debug mode)
`python run.py`

Run celery task queue (in debug mode)
`celery worker -A app.celery --loglevel=debug`

Setup mongoDb, redis and update urls in `constants.py`

## CRUD Operations

#### Create - `/api/v1/ad/add` - `POST`
Key -
```
data: {
    destination_url: String,
    headline: String(30),
    primary_text: String(120),
    name: String,
    type: 'IMAGE_AD' or 'VIDEO_AD'
}
```
Minified Sample Value -

`data` -
```
[{"destination_url":"https://imgur.com/gallery/YZ1yC5a","headline":"ikaqvdgtuhlhynbtgztf Ad","name":"Ad no 02","primary_text":"yvxjvmjwkctbgzkjxnogrnrxzeepxzetttzxgotkvsjhgldbcjbrherlxvehuvxiztfslqeatveieqbqpcgxxngqajikinrlwbtc","type":"IMAGE_AD"},{"destination_url":"https://www.youtube.com/watch?v=O3-Jiejdr7E","headline":"ikaqvdgtuhlhynbtgztf Ad","name":"Ad no 52","primary_text":"yvxjvmjwkctbgzkjxnogrnrxzeepxzetttzxgotkvsjhgldbcjbrherlxvehuvxiztfslqeatveieqbqpcgxxngqajikinrlwbtc","type":"VIDEO_AD"}]
```

#### Read - `/api/v1/ad/` - `GET`

#### Update - `/api/v1/ad/update` - `POST` `PUT`
Key -
```
name: String,
replace: {
    destination_url: String,
    headline: String(30),
    primary_text: String(120),
    name: String,
    type: 'IMAGE_AD' or 'VIDEO_AD'
}
```
Minified Sample Value -

`name` - `Ad no 24`
`replace` -
```
{"content_url":"https://imgur.com/gallery/4nv4xRN","created_at":"2022-02-09 15:15:33.040172","destination_url":"https://imgur.com/gallery/4nv4xRN","headline":"xqnajxfpcxcdfkozuhnj Ad","meta_data":"","name":"Ad no 91","primary_text":"vcpmjkdkdhtunannkcrogucllkbcnjpxbufqvozqyojffjamlbyzjgndcwgkmynuonamsjvpucgjkmoqkfplpyqsvvsaqxvvkdqc","type":"IMAGE_AD","updated_at":"2022-02-09 15:15:33.040174"}
```

#### Delete - `/api/v1/ad/delete` - `DELETE`


#### Random Data Generation - `/api/v1/ad/random` - `POST`
Key -
```
size: Integer
```
Minified Sample Value -
`size` - `30`

### LICENSE
MIT License

Copyright (c) 2022 Raajesh