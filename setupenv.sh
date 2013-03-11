#!/bin/sh

virtualenv env && \
env/bin/python bootstrap.py --distribute && \
bin/buildout