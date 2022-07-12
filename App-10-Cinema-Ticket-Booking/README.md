# Cinema Ticket Booking App

## Description

An app that:

* Gets as input:
  * Full name.
  * Preferred seat number.
  * Card type.
  * Card number.
  * Card cvc.
  * Card holder name.
* Allows a user to book a seat for the cinema using their card.
* Performs error-checking for card, seat availability and balance.
* Returns:
  * A ticket booking confirmation as PDF.

## Initial Design

### Classes, Attributes & Methods

* Account
  * Required attributes: name
  * Methods: buy()
* Card
  * Required attributes: database, card_type, number, cvc, holder_name
  * Methods: verify(), transfer()
* Seat
  * Required attributes: database, seat_id, price
  * Methods: is_free(), claim()
* Ticket
  * Required attributes: user, seat
  * Methods: generate_ticket()
