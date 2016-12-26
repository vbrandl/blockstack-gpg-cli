#!/usr/bin/env python2

import os
import sys

import blockstack_client
from blockstack_client import get_logger, get_config
from blockstack_client import BlockstackHandler
from blockstack_client import list_accounts, list_immutable_data, list_mutable_data
from blockstack_client import make_mutable_data_url, make_immutable_data_url

BEGIN_BLOCK = '-----BEGIN PGP PUBLIC KEY BLOCK-----'
END_BLOCK = '-----END PGP PUBLIC KEY BLOCK-----'

def get_config_dir( config_dir=None ):
	"""
	Get the default configuration directory.
	"""
	if config_dir is None:
		config = get_config()
		config_dir = config['dir']

	return config_dir

def gpg_list_profile_keys( name, proxy=None, wallet_keys=None, config_dir=None ):
	"""
	List all GPG keys in a user profile:
	Return a list of {'identifier': key ID, 'contentUrl': URL to the key data} on success
	Raise on error
	Return {'error': ...} on failure
	"""

	config_dir = get_config_dir( config_dir )
	client_config_path = os.path.join(config_dir, blockstack_client.CONFIG_FILENAME )

	if proxy is None:
		proxy = blockstack_client.get_default_proxy( config_path=client_config_path )

	accounts = list_accounts( name, proxy=proxy )
	if 'error' in accounts:
		raise Exception("Blockstack error: %s" % accounts['error'] )

	# extract
	accounts = accounts['accounts']
	ret = []
	for account in accounts:
		if account['service'] != 'pgp':
			continue 

		info = {
			"identifier": account['identifier'],
			"contentUrl": account['contentUrl']
		}

		if 'keyName' in account.keys():
			info['keyName'] = account['keyName']

		ret.append(info)

	return ret

print gpg_list_profile_keys(sys.argv[1])
#  vim: set filetype=python ts=4 sw=4 tw=120 noet :
