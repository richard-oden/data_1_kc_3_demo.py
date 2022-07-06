# Instructions

Here your tasks, should you choose to undertake them!

**Easy/Intermediate**: See if you can refactor lines 30 - 33. You could due this using either a list comprehension or python's `filter` function.

**Intermediate/Hard**: Implement a caching system when making requests to our API. Since we know that the API only updates its results every 24 hours, we can check to see if it's been at least 24 hours since the last request. The logic of this cache will work as follows:

If we have a local JSON file, and it was last modified less than 24 hours ago, then read from the JSON file. Otherwise, pull in fresh data from the API and write it to the JSON file.

# Resources
- https://api.websitecarbon.com/#response-statistics
- https://realpython.com/python-filter-function/
- https://www.programiz.com/python-programming/list-comprehension
- https://www.geeksforgeeks.org/how-to-get-file-creation-and-modification-date-or-time-in-python/