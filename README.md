# Welcome to Virtual Cloud Storage System 
## Place where you can store and manage your data. 

## To run the system 

## Make Build and run 
### $ docker compose up -d --build and docker compose logs -f

## Go in the web container and run migrations
### 1) $ docker compose exec web bash
### 2) $ python manage.py makemigrations
### 3) $ python manage.py migrate

# Run these and enjoy your virtual cloud storage system