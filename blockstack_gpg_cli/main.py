#!/usr/bin/env python2

import sys
from blockstack_gpg import gpg_list_profile_keys, gpg_fetch_key

debug = False

gpg_keys = gpg_list_profile_keys(sys.argv[1])

for gpg_key in gpg_keys:
	if debug:
		print "contentUrl: " + gpg_key['contentUrl']
		print "identifier: " + gpg_key['identifier']
	print gpg_fetch_key(gpg_key['contentUrl'], gpg_key['identifier'])

#  vim: set filetype=python ts=4 sw=4 tw=120 noet :
