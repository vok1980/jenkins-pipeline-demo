#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

image = 'vok1980/jenkins:latest'
subprocess.check_call('docker pull {image}'.format(image=image), shell=True)

# see https://github.com/jenkinsci/docker/blob/master/README.md
subprocess.check_call('docker run --rm --name jenkinsci -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 {image}'.format(image=image), shell=True)

# Prune unused Docker objects
# https://docs.docker.com/config/pruning/
