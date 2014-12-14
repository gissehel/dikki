#!/usr/bin/env python
# coding: utf-8

import docker

class RawDocker(object):
    def __init__(self):
        self._docker = None

    def get_docker(self):
        if self._docker is None:
            self._docker = docker.Client(base_url='unix://var/run/docker.sock', version='1.13', timeout=10)
        return self._docker

    def get_images(self):
        return self.get_docker().images(quiet=False, all=True)

