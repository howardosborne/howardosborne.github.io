---
layout: post
title:  "RailEurope: Stop! You're going in the wrong direction..."
description: How persuading more people to use trains instead of planes means rethinking optimisation.
date:   2020-02-21 09:00:00 +0000
categories: Climate-change Optimisation
---
In an age of [flight shaming](https://www.ft.com/content/5c635430-1dbc-11ea-97df-cc63de1d73f4), it ought to be encouraging to see rail sites like loco2 get a makeover to become [RailEurope](https://raileurope.co.uk/).

The trouble is many holidaymakers will be put off when they actually look at the cost and travel time. Incidentally, I'm picking on RailEurope because they focus on the holiday market, but other sites are also missing how more people could be nudged people onto the rails.

It may feel like an uneven fight because trains are slower and airlines don't pay duty on fuel but there is an overlooked factor which anyone who specialises in performance engineering might notice.

First let's take a step back and see how train booking sites work at present. A very nice [article](https://medium.com/omio-engineering/how-routing-works-4-simple-algorithms-5919a88c3648) on journey planning has been provided by Bastian Buch who works with Rome2Rio.

It walks through some of the algorithms used to present options to users who want to travel between two places. Anyone familiar with the [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) will recall that computer science is about finding pragmatic solutions which may not be perfect, but near enough to actually be useful. They are known as optimisation algorithms.

In that case of planning and booking a train journey, rail sites do a similar thing to flight sites like [skyscanner](https://www.skyscanner.net/) and look to offer two things: The fastest route and the cheapest route. Both of those things are fine, if you're a travelling salesman, but for a holidaymaker we are forgetting something.

Let's take an example of two sun-starved parents who wanted a holiday last year. They planned it in the following stages (can you guess who it is?):

1. Look at possible destinations
2. Look for accomodation and travel in those places
3. Book both travel and accommodation
4. Book a hire car
5. Look for things to do in the area

Notice this is a list.

There is another word for a list of actions - an algorithm.

We were instinctively applying our own optimisation algorithm to the seemingly infinite variety of things to do with our free time.

So, when we consider the travel part of this list, and use a journey planner, we are attempting to optimise an optimisation, which in the case of long distance rail travel is... sub-optimal.

For rail travel to really compete, that list needs to be subverted. 

Long distance train travel comes in multiple parts and this is where trains have the advantage over planes. Activites don't need to be just at a destination. They can be scattered en-route - as can great places to stay. Imagine a TripAdvisor but not just for single destinations.

Let's rethink that list above removing the items that were just there because it's how we thought we would get what we wanted and replacing it with what we really wanted.
- feel hot
- go to a water park with slides
- go in the sea and do some snorkelling
- do something in 'the great outdoors' like canoeing
- get some nice food
- see some nice scenery
- do something a bit cultural museums/old towns
- do something different (anything within reason)
- buy some souvenirs (for ourselves and family)
- don't spend too much

It was a big ask of any destination to do all of this and we didn't. Maybe we could have if we had gone by rail...

As things stand, planning such a holiday would have taken a fair heap of time and effort, even with help from sites like [Seat61](https://www.seat61.com/). 

So, here's an opportunity for developing journey planners which guide users on possible journeys through places with fun things to do and places to stay and so build their own holiday. This is where software engineers who specialise in performance come in.

We need data integration and an algorithmic rethink. We need to be able to evaluate journeys and places in a way that presents options based on what people were really after rather than on how they thought they would get it. Perhaps holiday planning needs to be 'gamified'. Imagine playing a game like [Ticket to Ride](https://www.daysofwonder.com/tickettoride/en/) and picking up all the things you wanted to do on the way.

A key task is to bring these various datasets together which alas, in Europe, is hampered by our transport data being fragmented. Groups like Shift2Rail need to step up a gear...

In the meantime, we have to work with the limitations we have, and a bit of imagination. So, where next?
