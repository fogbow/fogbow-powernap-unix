#!/usr/bin/env python

from distutils.core import setup

setup(name = 'fogbow-opportunism',
      version = '1.0',
      description = 'Opportunism module for fogbow cloud',
      author = 'Marcos Nobrega',
      author_email = 'marcosancj@lsd.ufcg.edu.br',
      url = 'https://github.com/fogbow/fogbow-opportunism',
      packages = ['powernap', 'powernap.monitors'],
      package_dir = {'powernap': 'powernap/powernap'},
      scripts = ['powernap/sbin/powernapd'],
      data_files = [('/etc/powernap', ['powernap/config'])]
     )
