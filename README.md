# Exercise-04

 > This exercise is still **under construction**. If you would like to proceed, please discuss with the teacher.

Convert the Exchange class to act as a single threaded network server using an event loop. Design and generate a structured protocol using Google protocol buffers.

Suitable for advanced students.

## Event Loops

Convert the Exchange class to act as a single threaded network server using an event loop: https://docs.python.org/3.6/library/asyncio.html

Handle incoming messages from network clients in order to manage their connection to the exchange, and their orders. Dispatch replies describing the state of the client and its orders.

## Structured Protocols

Design and generate a structured protocol using Google protocol buffers: https://developers.google.com/protocol-buffers/docs/pythontutorial

 - Client login request
 - Client login reply
 - Client logout request
 - Client logout reply
 - Order insert request
 - Order insert reply
 - Order delete request
 - Order delete reply
 - Order traded feed
