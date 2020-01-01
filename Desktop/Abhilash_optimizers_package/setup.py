# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:47:43 2019

@author: 45063883
"""


from distutils.core import setup
setup(
  name = 'Abhilash_optimizers',         
  packages = ['Abhilash_optimizers'],   
  version = '0.1',       
  license='MIT',        
  description = 'Stochastic Optimizers for gradient convergence including activation functions',   
  author = 'ABHILASH MAJUMDER',
  author_email = 'abhilash.majumder@hsbc.co.in',
  url = 'https://github.com/abhilash1910/Abhilash_optimizers_package',   
  download_url = 'https://github.com/abhilash1910/Abhilash_optimizers_package/archive/v_02.tar.gz',    
  keywords = ['adam', 'adagrad', 'adamax','optimizers','stochastic','sgd','rmsprop','momentum','nesterov adam'],   
  install_requires=[           

          'numpy',         
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
