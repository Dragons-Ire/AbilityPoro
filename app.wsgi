#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/league/html/AbilityPoro")

from app import app as application
application.secret_key = 'thisdhflajksdfhkljahg38r9yq908hg0q8r0sv@JLAJHLFISHJLAK'
