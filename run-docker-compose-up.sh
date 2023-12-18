docker rm $(docker ps -aq --filter name=fastapi_crud_container)
sudo docker-compose up --build -d