# Week 12 answers

## Exercise 1 
1. The messages the customer typed: Changing shipping address, it's order A102, 9 Pine Street, Tampa

2. How many tool requests were refused, and why: 2 because the first one used order A100 and the second used 123 Main St.

3. If the customer now types "thanks", how many messages does Ollama receive on the next call?  14 messages

4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable?  The rule looks for card in the message, it is a mistake, a missed payment question may put card details in the front of the model.


## Exercise 3

(.venv) DESKTOP-FJGPNR6% python3 main.py
Type a message, or type quit to stop
You: hello
Sunny: Hello! How may I assist you today?
You: I want to change my shipping address for A100
Sunny: Could you please provide the new shipping address for order A100?
You: 14 Bay Road
Sunny: Your request to change the shipping address for order A100 has been submitted to our staff for approval. Please wait for their confirmation.
You: quit
Messages in this conversation: 8
Staff review
Request 1: A100 to 14 Bay Road
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street