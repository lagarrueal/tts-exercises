# Docker Manual
You will be running Festival inside a Docker container using an image that the LVL has developed.

## Installing Docker
* Install the Docker engine for your OS : `https://docs.docker.com/engine/install/`
* Recommended for Linux users (needed for Visual Studio Code integration):
    * Add yourself to the docker system group:
        * `sudo usermod -aG docker $USER`
        * restart your system
* You have to be minimally able to successfully run a container with the ubuntu image: `docker run --rm -it ubuntu:xenial /bin/bash`.

## Installing VS code and extensions (recommended)
This is recommended for those with little prior experience with Docker.
* [Install VS Code](https://code.visualstudio.com/)
* Open VS Code (VSC)
* Install the `docker` VSC extension by opening the extensions pane on the left (ctrl+shift+X) and search for `ms-azuretools.vscode-docker` and hit install
* Install the `remote development` VSC extension, search for `ms-vscode-remote.vscode-remote-extensionpack`. Follow the [guide here](https://code.visualstudio.com/docs/remote/containers) to complete installation

## Setting up a Container

### Get the Image
You can either:
* Clone the image from `Docker Hub`:
    1. `docker pull thorsteinndg/lvlis`
* Build the image yourself from a `Dockerfile`:
    1. Clone [this repository](https://github.com/cadia-lvl/docker-festival)
    2. Build the image. In VSC you can simply right click the `Dockerfile` and select `Build image...`. Otherwise you `cd` into the repository and issue the command `docker build --pull --rm -f "Dockerfile" -t dockerfestival:latest "."`
    3. This process will take a very long time.

### Create the Container
1. List all docker images using `docker images`. Locate your `dockerfestival` and note it's `TAG`.
2. Then run:
    * If you built the image yourself: `docker run -it  dockerfestival:latest` where `latest` is the `TAG`.
    * If you pulled the image using `docker pull` then run: `docker run -it thorsteinndg/lvlis:latest`
3. You now have an interactive shell for your container

**Attaching VSC to container**
1. Click the Docker icon on the left side in VSC
2. A running container will have appeared under the `Containers` list view in the Docker pane. Right click your container and select `Attach Visual Studio Code`.
3. Now point VSC to `/usr/local/src` which contains the code for the project by clicking the `open` button on the left side in the newly opened VSC window.

Note: If the icon in front of your container is a red *stop* icon, you have to right click and select `start` first. Then attach VSC.

### Using the image
Make sure you have followed the steps above and start the container for your image. This is an `ubuntu` image so you can do many of the things you are used to when using Linux. You might want to use some familiar tools. Do:
* `apt-get update`
* Install a package, e.g. `apt-get install nano`