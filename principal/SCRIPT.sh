sudo docker build -t imagenapi -f /home/ubuntu/principal/dfapi .
sudo docker run -t -d -p 1001:1001 --name dockerapi imagenapi
sudo docker build -t imagenfront -f /home/ubuntu/principal/dffront .
sudo docker run -t -d -p 80:80 --name dockerfront imagenfront
sudo docker build -t imagendb -f /home/ubuntu/principal/dfdb .
sudo docker run -t -d -p 1002:1002 --name dockerdb imagendb
sudo docker ps >> /home/ubuntu/principal/logs.txt
