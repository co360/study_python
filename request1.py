#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

import requests
import json

url = 'https://view.inews.qq.com/g2/getOnsInfo'
params = {'name': 'disease_h5'}

response = requests.get(url, params=params)
data = json.loads(response.text)
