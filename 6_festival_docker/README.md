# Festival in Docker

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


## Prepare the data (in the right format)
