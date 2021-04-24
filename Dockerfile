FROM python:3-onbuild
MAINTAINER Gissehel "public-maintainer-docker-dikki@gissehel.org"

ENTRYPOINT [ "python3", "./dikki.py" ]

