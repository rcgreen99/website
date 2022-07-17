# Provisioning

## Create User

```sh
# login to host w/o config
ssh -i ~/.ssh/digitalocean_rsa root@164.92.101.129
```

```sh
# login to host w/ config
ssh website

# add dev user once logged in
sudo adduser dev

# add dev user to sudo group
sudo adduser dev sudo

# login as dev user
su -l dev
```

## Install Docker

```sh
# install docker repo
sudo apt install docker.io

# enable docker on start up (is alrady done by default on Ubuntu)
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# start docker daemon  (is alrady done by default on Ubuntu)
sudo systemctl start docker

# create docker group (is alrady done by default on Ubuntu)
sudo groupadd docker 

# add dev user to docker group
sudo usermod -aG docker dev

# log out (to refresh permissions)
exit

# log in
ssh website
```
