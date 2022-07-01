# NewsFeed Emailer

## Description

An app that:

* Gets as input (Excel):
  * User names
  * Email addresses
  * Interests
* Sends an email to each user with a personalized news feed.

## Initial Design

### Classes, Attributes & Methods

* ExcelFile
  * Required attributes: filepath
  * Methods: get_data()
* Email
  * Required attributes: sender, receiver, subject, body
  * Methods: send()
* NewsFeed
  * Required attributes: data
  * Methods: get()