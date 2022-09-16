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

