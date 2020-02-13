#!/usr/bin/env python

from os import path
from distutils.core import setup

pwd = path.abspath(path.dirname(__file__))
with open(path.join(pwd, 'README.md')) as input:
    long_description = input.read()
	
setup(
	name='Baubles',
	version='1.3',
	license='MIT',
	description='logging decorator',
    long_description=long_description,
    long_description_content_type='text/markdown',
	url='https://github.com/eddo888/baubles',
	download_url='https://github.com/eddo888/baubles/archive/1.3.tar.gz',
	author='David Edson',
	author_email='eddo888@tpg.com.au',
	packages=[
		'Baubles',
	],
)
