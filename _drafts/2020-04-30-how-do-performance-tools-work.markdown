---
layout: post
title:  "Part 2: How do performance testing tools work?"
description: Performance Testing for Decision Makers
date:   2020-02-30 09:00:00 +0000
categories: Big-O Performance Testing Analysis
---

Making a series aimed at shedding some light on the murky world of performance testing. 

In this part, we're going to lift the lid on performance testing tools. We're going to focus on web testing tools which make up the lion's share.

what happens when you look at a web site

browser asks for a page
gets a response
all of this is done using http
so, to run a test, on approach would be to get a load of machines. But there is a cleverer way (sneaky)
We don't actually need to take the html and turn it into beautiful text
and we don't need to actually show a picture (show picture)
All we need to do is just make the calls the browser would do.

How do we know what calls it would make

most tools come with a recording device. This is a sneaky piece of software which sits between the browser and the server and looks at the traffic. Yes, alarm bells should ring and some technologies block this traffic.
But on the whole, it's OK to let these little devices do their thing, capturing the traffic and then just stop them afterwards.

This does create another problem which is how do we work with things that don't exist in the recording and we'll will look at in the next part.