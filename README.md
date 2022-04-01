# Shiphero Python GraphQL client

HELP: we want to keep building on this project, but we do not have access anymore to user and password from shiphero account. If you could give that credentials, we could keep moving on. Feel free to contact Pipe on this subject.

* Feel free to contribute to this project.

## Example code

- Init shiphero instance
```
from shiphero import Shiphero

shiphero = Shiphero(
    username=SHIPHERO_USERNAME,
    password=SHIPHERO_PASSWORD
    )
```

### Getting fulfillment_status from a given order_id

```
order_id='your_order_id'

# Build the query
query = shiphero.query

# Building the order query
order = query.order(id=order_id)

# Make sure to request the complexity and request_id
order.complexity() 
order.request_id()

# Put fulfillment_status information
order.data.fulfillment_status()

# Executing the call
data = shiphero.endpoint(query)

print(data)
```

### Getting all information from a given order_id

```
order_id='your_order_id'

# Build the query
query = shiphero.query

# Building the order query
order = query.order(id=order_id)

# Make sure to request the complexity and request_id
order.complexity() 
order.request_id()

# Put fulfillment_status information
order.data()

# Executing the call
data = shiphero.endpoint(query)

print(data)
```