---
layout: post
title:  "Why testing web caches is important and how to do it"
description: How to test a web cache with Groundhog
date:   2020-04-11 08:00:00 +0000
categories: performance webcache nginx varnish iis groundhog
---

At this extraordinary time, it's not surprising that some of our systems are struggling.

For anybody supporting web applications and their infrastructure, a key activity has to be getting the web cache working to an optimum. This isn't an easy task.

Web caches are designed to act as a temporary store which can quickly serve up pages and other resources, saving a trip to a backend server. Some are designed purely to act as a cache such as [Varnish](https://varnish-cache.org/). Others are integrated with a web server like [nginx](htps://nginx.org), [Apache](https://httpd.apache.org/docs/2.4/mod/mod_cache.html) or [IIS](https://www.iis.net/overview/reliability/dynamiccachingandcompression).

![alt text](../../images/web_cache_model.png "web cache in action")


Over time, web caches have become more powerful and flexible and this has given us great opportunities to relieve the pressure from back end systems. However, the increased utility has meant that configuration changes need careful consideration and it is not always obvious what the consequences of making a change will be.

Even when the changes are well understood, the trade-off between speed and accuracy (such as with time-sensitive data) needs to be fully thought through.

So how can we do this?

[Groundhog](https://howardosborne.github.io/groundhog) is designed to test web caches by playing the parts of both users and web (or origin) servers.

![alt text](../../images/groundhog_in_action.png "groundhog in action")

It allows you to create test schedules, based on access (or web) logs, and then replay them in a test environment. The results can then be chewed over to determine whether to promote the configuration change to live or tweak it some more.

Systems like nginx provide good analysis tools to do this, so Groundhog doesn't attempt to replicate or replace this. But, if you do need a bit of help with this, let me know.

If you would like to learn more or find out how to contribute, have a look at the [GitHub repository](https://howardosborne.github.io/groundhog/)