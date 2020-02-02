---
layout: post
title:  "Using mandolin on gherkin"
description: How to make BDD regression tests work across environments.
date:   2019-05-23 21:03:36 +0530
categories: BDD Gherkin
---
I have a lot of sympathy for Behaviour Driven Development champions who get frustrated at the misuse of tools like Cucumber. However, isn't it inevitable that organisations which have invested in BDD will want the resulting assets to be as widely used as possible?

The structure of flat feature files, written in Gherkin, is great but one of its main strengths, having a simple clear editable-by-anyone format, can also present issues with scalability and maintenance when reusing the scenarios for regression testing. Let's take an example:

Imagine we are testing a web form which allows people to renew their account. The form contains the following fields:
```
First name
Surname
Account ID
Postcode
Debit card number
Expiry Date
```
Our feature file which was used to develop the form is below and contains two scenarios. one which specifies what happens for a successful renewal and another which sets out what error messages should appear for the different types renewal failure.
```
Feature: Apply for account renewal
  In order to renew their account
  Users should be able to
  complete a form with their details

Scenario Outline: unsuccessful renewal
    Given I am on the account renewal form
    When I enter "Bob" in the Firstname field
    And "Jones" in the Surname field
    And "Acc12345" in the Account ID field
    And "AB12 1AT" in the postcode field
    And "342523523535252" in the Debit card field
    And "01/16" in the Expiry Date field
    And click "Renew Account"
    Then I see "Account renewed"
  Examples:
    | firstname | surname | account_id | postcode | debit_card | expiry_date | error_message |
    | Bob | Jones | Acc12344 | AB12 1AT | 342523523535252 | 01/16 | Invalid Account ID |
    | Bob | Jones | Acc12345 | AB12 3TZ | 342523523535252 | 01/16 | Invalid Postcode |
    | Bob | Jones | Acc12345 | AB12 1AT | 342523523535253 | 01/16 | Invalid debit card |
    | Bob | Jones | Acc12345 | AB12 1AT | 342523523535252 | 01/14 | Invalid expiry date |
```
Scenario outlines are a neat way of expressing a lot of different scenarios is a concise way. So how about using this for any regression testing on future releases?

Well, our tests will continue to work for as long as all the fields are valid.

However, we don't always have full control over test environments instead having to make do with getting an extract of valid test accounts before we run our tests.

Also details don't always come from a single source.

What if the postcode had to be checked against a list of approved postcodes for a particular region and this was held in a different source?

What if the card details are authenticated against a third party payment gateway, which provides lists of valid cards and expiry dates?

Now imagine a feature file with multiple tables each relying on data from a different source:Usernames from a database. Postcodes from a test file. Card details from a third party an whatever format they choose to use this year. Account IDs from a different department who email you a spreadsheet when you've chased them for the fourth time...

Now imagine a stack of feature files each containing tables relying on data from these diverse sources.

And what about a stack of directories each containing a stack of feature files each containing tables relying on data from these diverse sources.

Data management for regression testing can get very messy, very quickly.

We might be able to write our feature code to get suitable test data at run time but then we can loose the readability of the original format. We also loose the ability to run our scenarios manually. - an overlooked but valuable part of the process.

In order to overcome this, I have made a tool, mandolin (really it's just a short script) which will look for tables in feature files and extract them into separate pipe delimited (guess why I chose a pipe) test files. A placeholder is put into the feature file in the following format <<Tablen>>

The data can then be managed independently and when a suitable set of files have been gathered, merged back into one file ready for use. If you want to just extract one table - do it manually and then run the merge when ready.

You could also create multiple feature files with different data where other environments are being tested.
