---
layout: post
title:  "Performance Testing"
description: What performance testing involves.
date:   2019-05-01 09:00:00 +0000
categories: Performance Testing Investigtion Optimisation
---
### What is performance testing?
You probably have a good idea of whether your software is functional and maybe how well it performs when running in a development environment. But how well will it cope when:
- fully populated with data?
- under typical or peak load?
- under expectional stress, perhaps a denial of service attack?

What will be the impact on users and data?

Performance testing focusses on answering these questions.

We do it by designing a series of tests which shows how the systems deals with different circumstances. Typical tests are:
- Normal operation
- peak load
- soak with spikes (and manual exploratory window) 
- stress tests.

#### Data and environment
Testing will tell you little unless the system under test is realistic by being populated with a realisitically sized set of data and is deployed to an environment that is either like live or at least sufficiently sized to draw inferences.

Helping generate data to both drive tests and populate systems is a key activity.

#### Monitoring
Monitoring is key to understanding how healthy your systems are and if there are issues where the problems are located. Performance testing is an ideal opportunity to make sure you have adequate monitoring in place.

#### Baked-in performance
It's good to find performance issues before going live but it's better if they don't happen in the first place. This means making sure that performance is front and centre of thinking in the design and development of systems and then building testing into the delivery pipeline using continous integration tools.

#### Testing Tools
There is a wide variety of tools available (the list is growing), both commercial and open source.

Most organisation I have worked with want to work with tools that are widely known and supported, which is why JMeter often comes out on top. In any event, I can help you choose the best fit for your organisation.

However, a tool to execute tests is only part of the picture. Additional tools and scripts are usually needed to ease the process of building test environments, data, monitoring, reporting as well as analysis of existing live data.
