#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tweepy
import locale
import commands
from time import time

# oAuth Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# unix time
current_time = time()

# voyager Parameter
epoch_0 = 1362931200
epoch_1 = 1363017600

dist_0_v1 = 18479843215.8939
dist_1_v1 = 18479190162.0889
       
dist_0_v2 = 15186607409.6049
dist_1_v2 = 15186068826.0609
    
dist_0_v1s = 18488521755.6647
dist_1_v1s = 18489988010.2818
    
dist_0_v2s = 15124563072.3367
dist_1_v2s = 15125858167.3065

# distansce from sun
v1_km_distance = (((current_time - epoch_0) / (epoch_1 - epoch_0)) * (dist_1_v1s - dist_0_v1s)) + dist_0_v1s
v2_km_distance = (((current_time - epoch_0) / (epoch_1 - epoch_0)) * (dist_1_v2s - dist_0_v2s)) + dist_0_v2s

n1 = v1_km_distance
n2 = v2_km_distance

locale.setlocale(locale.LC_ALL,'ja_JP.UTF-8')

s1 = locale.format("%d", n1, True)
s2 = locale.format("%d", n2, True)

mypost = 'ボイジャー1号は太陽から' + s1 + 'km。2号は' + s2 + 'kmのくらいの位置を飛行してるよ。'

print mypost

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(mypost)
