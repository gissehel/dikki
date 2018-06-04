#!/usr/bin/env python
# coding: utf-8

import docker
from .tools import serialize


class RawDocker(object):
    def __init__(self):
        self._docker = None
        self._debug = False

    def get_docker(self):
        if self._docker is None:
            # self._docker = docker.Client(base_url='unix://var/run/docker.sock', version='1.13', timeout=10)
            self._docker = docker.APIClient(base_url='unix://var/run/docker.sock', version='1.21', timeout=10)
        return self._docker

    def get_images(self):
        images = self.get_docker().images(quiet=False, all=True)
        return self._serialize(images, '__images__')

    def get_containers(self):
        return self._serialize(self.get_docker().containers(quiet=False, all=True), '__containers__')

    def get_container_info(self, id):
        return self._serialize(self.get_docker().inspect_container(id), '__container_{}__'.format(id))

    def get_image_info(self, id):
        # serialize(self.get_docker().history(id), '__image_history_{}__'.format(id))
        return self._serialize(self.get_docker().inspect_image(id), '__image_{}__'.format(id))

    def _serialize(self, data, name):
        if self._debug:
            serialize(data, name)
        return data

    def set_debug(self, value):
        self._debug = value


