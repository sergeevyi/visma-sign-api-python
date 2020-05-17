# Python bindings for the Visma Sign API v1

Visma Sign is used for electronically signing documents like agreements, terms of service, etc. The Visma Sign Python library provides convenient access to the Visma Sign API v1 from applications written in the Python language. 

## Documentation

See the [API docs](https://sign.visma.net/api/docs/v1/).

## Requirements

-  Python 3.6+

## Installation

* Install from source with:

```sh
python setup.py install
```

## Configuring 

```python
import visma_sign

visma_sign.identifier = 'organization-identifier-uuid-here'
visma_sign.secret = 'organization-secret-here'
visma_sign.api_url = 'https://sign.visma.net'
```

## Usage

```python
import visma_sign

payload = {"document":{"name":"Java test"}}
client = ApiClient()
documentUuid = client.createDocument( json.dumps(payload) )
```
