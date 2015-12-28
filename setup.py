#!/ust/bin/env python

from setuptools import setup

setup(name='ImageCount',
      version='1.0.0',
      description='Display an image with counter',
      author='Oren Miller',
      author_email='orenmiller@gmail.com',
      scripts=['image_count'],
      install_requires=['Pillow'],
      include_package_data=True
      )
