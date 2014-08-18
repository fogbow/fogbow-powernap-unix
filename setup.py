#!/usr/bin/env python

import os, sys
from distutils.core import setup

data_files = [('/etc/fogbow-powernap', ['powernap/config'])]
              
for action_dir in os.listdir('actions'):
  action_scripts = [os.path.join('actions', action_dir, 'stop-node'), 
                    os.path.join('actions', action_dir, 'start-node')]
  data_files.append((os.path.join('actions', action_dir), action_scripts))

setup(name = 'fogbow-opportunism',
      version = '1.0',
      description = 'Opportunism module for fogbow cloud',
      author = 'Marcos Nobrega',
      author_email = 'marcosancj@lsd.ufcg.edu.br',
      url = 'https://github.com/fogbow/fogbow-opportunism',
      packages = ['powernap', 'powernap.monitors'],
      package_dir = {'powernap': 'powernap/powernap'},
      scripts = ['powernap/sbin/powernapd'],
      data_files = data_files
     )
     
if "install" in sys.argv:     
  os.system('cp contrib/upstart/fogbow-powernap.conf /etc/init')
  os.system('initctl reload-configuration')
  os.system('service fogbow-powernap start')
  
