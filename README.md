# Docker Image(s) for the Geopsy Suite

> Joseph P. Vantassel, Texas Advanced Computing Center - The University of Texas at Austin

## About `geopsy-docker`

The [geopsy suite](https://www.geopsy.org/) is a powerful set of open-source tools for geophysics research,
however the installation of those tools can be challenging, especially on systems where
a user does not have root privileges. Therefore, this repository includes instructions for building
the `geospy suite` inside of a Docker container.

The repository currently hosts instructions (i.e., Dockerfiles) for:

- :white_check_mark: geopsy v3.4.2 with qt v5.14
- :white_check_mark: geopsy v2.10.1 with qt v4.8

__The pre-build images can be found on
[dockerhub](https://hub.docker.com/repository/docker/jpvantassel/geopsy-docker)__.

## Run

```
docker build -f Dockerfile -t geopsy:1.0.0 .
xhost +local:docker
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd)/:/app/files geopsy:1.0.0
```