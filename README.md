# Neopets-Multi-Tool

The goal:
  - Ideally this will end up being an all-in-one auto-player for neopets, only completed functions will be pushed here. Anything I feel is incomplete will not be added.
  - The multi tool is setup so you'll be able to run this 24/7 without sending unnecessary requests to the server, this is done by logging when an action was completed compared to how often a user can do that action. For example: the tool completes Buried Treasure, logs the time it was completed, making it impossible for it to send any requests to the server for Buried Treasure until 3 hours has passed. This makes botting on neopets a lot safer than relying on parsing page data to check if an action can be completed again.
  
Requirements:
  - Python 3.8
  - pip install requests
