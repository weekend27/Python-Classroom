# -*- coding:utf-8 -*-
#! /bin/env python3 

__author__ = 'weekend27'

# log test

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning: config file %s not found', 'server.conf')
logging.error('Error occured')
logging.critical('Critical error -- shutting down')
