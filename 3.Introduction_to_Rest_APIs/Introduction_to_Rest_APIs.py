# Introduction to REST APIs :

# Understanding the concept of REST and its principles
# HTTP methods (GET, POST, PUT, DELETE)
# Request and response structures
# API endpoints and resource identification
# Introduction to JSON (JavaScript Object Notation)
# References
# https://www.geeksforgeeks.org/rest-api-introduction/
# https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
# https://www.geeksforgeeks.org/json-introduction/

# REST API stands for Representational State Transfer API. It is a type of API (Application Programming Interface) that allows communication between different systems over the internet. REST APIs work by sending requests and receiving responses, typically in JSON format, between the client and server.
# A request is sent from the client to the server via a web URL, using one of the HTTP methods.
# The server then responds with the requested resource, which could be HTML, XML, Image, or JSON, with JSON being the most commonly used format for modern web services.
# These methods map to CRUD operations (Create, Read, Update, Delete) for managing resources on the web.
# NOTE: REST is an architectural design style for APIs, while HTTP is the communication protocol used for data transfer over the web. REST APIs use HTTP methods to interact with resources, but they are not the same thing. REST defines how the APIs should behave, while HTTP defines the rules for communication over the web. They commonly work together, but they serve different purposes

# Common HTTP Methods Used in REST API
#  In HTTP, there are five methods that are commonly used in a REST-based Architecture, i.e., POST, GET, PUT, PATCH, and DELETE. These correspond to create, read, update, and delete (or CRUD) operations, respectively. There are other methods that are less frequently used, like OPTIONS and HEAD.

# GET
# Used to fetch/read data from the server.
# Returns status 200 OK on success, 404 or 400 on error.
# It is safe and idempotent.

# POST
# Used to create a new resource.
# Returns status 201 Created with the location of the new resource.
# It is neither safe nor idempotent.

# PUT
# Used to update or create a resource.
# Replaces the entire resource with new data.
# It is idempotent.

# PATCH
# Used to partially update a resource.
# Updates only the specified fields, not the whole resource.
# It is not always idempotent.

# DELETE
# Used to remove a resource.
# Returns 200 OK on successful deletion.
# It is idempotent.

# PUT vs PATCH (Quick Difference)

# PUT → Full update (send all data)

# PATCH → Partial update (send only changes)

# Idempotence
# An idempotent method gives the same result even if called multiple times.
# Examples: GET, PUT, DELETE
# Non-idempotent: POST, sometimes PATCH

# Introduction to JSON (JavaScript Object Notation) :
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for
# humans to read and write, and easy for machines to parse and generate. It is commonly used in REST APIs for data exchange between clients and servers.
# JSON is built on two structures:
# A collection of name/value pairs (often called an object, record, struct, dictionary,
# hash table, keyed list, or associative array).
# An ordered list of values (often called an array, vector, list, or sequence).
# JSON supports the following data types:
# Strings: Text enclosed in double quotes.
# Numbers: Integer or floating-point numbers.
# Booleans: true or false.
# Null: Represents a null value.
# Arrays: Ordered lists of values enclosed in square brackets [].
# Objects: Collections of name/value pairs enclosed in curly braces {}.
# Example of a JSON object:
# {
#   "name": "Omkar Khopade",
#   "age": 20,
#   "isStudent": True,
#  "courses": ["Math", "Science", "History"],
#   "address": {
#     "street": "123 Main St",
#     "city": "Pune",
#     "zip": "411043"
# }