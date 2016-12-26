#!/usr/bin/env python2

from setuptools import setup, find_packages

#init __version__
exec(open('blockstack_gpg_cli/version.py').read())

setup(
	name='blockstacl-gpg-cli',
	version=__version__,
	url='https://github.com/vbrandl/blockstack-gpg-cli',
	license='GPLv3',
	author='Valentin Brandl',
	author_email='vbrandl <AT> riseup <DOT> net',
	description='Download and verify GPG keys from blockstack',
	packages=find_packages(),
	install_requires=[
		'blockstack-client>=0.14.0',
		'python-gnupg>=0.3.9'
	],
)
#  vim: set filetype=python ts=4 sw=4 tw=120 noet :
