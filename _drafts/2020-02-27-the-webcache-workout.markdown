---
layout: post
title:  "The webcache workout"
description: How to tone up your cache.
date:   2020-02-27 21:01:36 +0000
categories: performance webcache nginx
---

#give your cache a health check
review the access logs
breakdown the hits/misses/expireds

if you have a lot of misses
are your parameters letting you down

have a lot of expireds
review expire time 
are you using etags? if so, does the webserver return 304s
consider background fetch - is it wise
