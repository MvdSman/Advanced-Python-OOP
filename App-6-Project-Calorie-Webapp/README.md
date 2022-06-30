# Calorie Calculator WebApp

## Description

A web-app that:

* Gets as input (form):
  * Weight
  * Height
  * Age
  * Country
  * City
* Scrapes temperature based on Country and City
* Returns:
  * Required kcal today based on above input

## Initial Design

### Front-End

Basic form with text output.

### Classes, Attributes & Methods

* HomePage
* CalorieForm
* Calorie
  * Required attributes: weight, height, age, temperature
  * Methods: calculate()
* Temperature
  * Required attributes: country, city
  * Methods: get()