# What is Container?
    * Package -  application with all the necessary 
    * Makes development and deployment "more efficent"
    * Container is made up od images
    * Mostly "Linux Base Image", because small in size (alpine3.10) Layer - Linux base image
    * Run same app with different versions on containers 
<br>

Link: https://hub.docker.com - Public docker images repo.
! First time pull repo Layers it take more times next time it doesn't

<br>

# Docker Image vs Docker Container

## Docker Image:
    * "Image" is actual package (DockerHub)


<br>

## Docker Container
    * "Container" is when We pull that images on our local machine and started so the application inside actually starts that creates the container environment.
    * Port bind: talk to application runnnig inside of container. :5000
    * virtual file system
<br>

# Docker vs Virtual Machine
    * How operating system is made up?
        1) Operatin system have 2 layers: "OS Kernel" and "Applications" layers:
            * OS Karnel - cominicate the hardware components like CPU and memory, ...
            * Applications run on the "KERNEL" layer
            * All linux use same "Linux Kernel but" implamented different application.
            * Docker run in "Application" Layer(so that images small MB size / faster)
            * Virtual machine is Applications + OS Kernel (GB memory size / slow)


# Docker command
    * 'docker pull {image_repo}' -> pull image from DockerHub
    * 'docker images' -> list of images
    * 'docker run {image_id}' -> run image
    * 'docker ps -a' -> List of Docker containers
    * 'docker run -d {image}' -> detached mode (background)
    * 'docker start/stop/ {container_id}' -> Start/Stop containter
    * 'docker run -p600:6379 {container_id}' -> bind port id if same app with same port
    * 'docker log {container_id}' -> log of this container
    * 'docker run -d --name {name of container} {image}' -> Container names defaul auto random generate, by this way u can set custom name.
    * 'docker build . ' -> Build custom image in 'Dockerfile' 
    * 'docker rm {container_id}' -> remove container
    * 'docker system prune -a' ->  Delete all containers data 

    * 'docker-compose build' -> build default docker-compose.yml file
    * 'docker-compose up' -> run default docker-compose.yml file








#### List of running containers:
```bash
docker ps
```
#### List of all containers:
```bash
docker ps -a
```
#### List of all containers (only id):
```bash
docker ps -aq
```
#### Download image from official site:
```bash
docker pull <image_name>
```
#### List or images:
```bash
docker images
```
#### Remove images
```bash
docker image rm <image_name>
```
#### Run container:
```bash
docker run <image_name>:<tag>
```
#### Run container on background (detached) mode:
```bash
docker run -d <image_name>:<tag>
```
#### Map port localhost 8080 to port 80 in the container:
```bash
docker run -d -p 8080:80 <image_name>:<tag>
```
#### List of containers:
```bash
docker container ls
```
#### Stop running container:
```bash
docker stop <container id or name> 
```
#### Start stopped container:
```bash
docker start <container id or name>
``` 
#### Remove container:
```bash
docker rm <container id or name>
```
#### Force Remove container:
```bash
docker rm -f <container id or name>
```
#### Remove all containers:
```bash
docker rm $(docker ps -aq)
```
#### Naming containers:
```bash
docker run --name <container_name>
```
#### List of containers pretty formatted:
##### Format:
```bash
export FORMAT="ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"
```
```bash
docker run --format=$FORMAT
```
#### Mount current folder to container volume read-only:
```bash
docker run --name website -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 nginx
```
#### Enter into container:
```bash
docker exec -it <container_name> bash
```
#### Share volumes between containers:
```bash
docker run --name <container_name> --volumes-from <from_container_name> -d nginx
```
#### Build image with tag from Dockerfile in currenct directory:
```bash
docker build --tag <name:tag> .
```
#### Tagging images:
```bash
docker tag <from image:tag> <to image:new-tag>
```
#### Information about container:
```bash
docker inspect <container_id or name>
```
#### See logs:
```bash
docker logs <container_id>
```
#### See logs with following:
```bash
docker logs -f <container_id>
```
#
## Dockerfile configurations
#### Simple configuration for build node express image:
```Dockerfile
FROM node:latest
WORKDIR /app
ADD package*.json ./
RUN npm install
ADD . .
CMD node index.js
```

