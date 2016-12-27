#!/usr/bin/env python2

import os
import sys

import blockstack_gpg
from blockstack_gpg import gpg_list_profile_keys

BEGIN_BLOCK = '-----BEGIN PGP PUBLIC KEY BLOCK-----'
END_BLOCK = '-----END PGP PUBLIC KEY BLOCK-----'



gpg_keys = gpg_list_profile_keys(sys.argv[1])

for gpg_key in gpg_keys:
	print gpg_key['contentUrl']
	print gpg_key['identifier']
#	if gpg_fetch_key(gpg_key['contentUrl'], gpg_key['identifier']):
#	    print gpg_fetch_key(gpg_key['contentUrl'])

#  vim: set filetype=python ts=4 sw=4 tw=120 noet :
