---
layout: post
title:  "Part 1: The Big Deal About Big-O"
description: Performance Testing for Decision Makers
date:   2020-02-30 09:00:00 +0000
categories: Big-O Performance Testing Analysis
---

I'm making a series of posts to shed some light on the murky world of performance testing. 

In this part, I've taken it as a personal challenge to see how briefly the whole art, craft and science behind perfomance testing be summed up, (and hopefully it will be longer than this sentence) and it is: I think I can do it in one letter.

- O, or as it is more commonly known Big-O

Performance testers try to find out whether something is fit for purpose.

This is often framed in practical questions like, can the new release cope with the expected number of registrations?

Create and run tests simulating different scenarios with pretend users doing the sorts of things we expect real users to do. By running various tests with ramps, spikes and various durations, we start to build up a picture of what the app looks like. And then we can characterise it. (Good news, we're finally getting to the bit where I promised it would be only one letter).

We how different parts behave.

Some parts of the system behave well - the goodies: (halo symbol)
Some, no matter what the strain, just keep doing there thing. It doesn't matter what the volume, the timings are the same. These are:
O(1)
Others increase proportionally to the load. These we call
O(n)

Some look like this:
O(log(n))
others like this:
O(n2)

and then we get to the baddies:
O(n3)
and then the real baddies:
O(c^{n})
O(n!)

The purpose of perforance testing is to identify the baddies - and try and turn them into goodies:
So, for a database, an index is more likely to follow one of the good curves
(show log curve and symbol)
rather than a bad curve
(show square)

With a well configured web cache, we can turn one of these
(show really baddie O(n!))
into one of these
(show n(1))

