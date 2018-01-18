CloudSight API for Python
=========================

[![Version](https://img.shields.io/pypi/v/cloudsight.svg?style=flat)](https://pypi.python.org/pypi/cloudsight)
[![API Docs](https://img.shields.io/badge/api-docs-blue.svg)](https://cloudsight.github.io/cloudsight-python/)
[![Build Status](https://travis-ci.org/cloudsight/cloudsight-python.svg?branch=master)](https://travis-ci.org/cloudsight/cloudsight-python)

A simple CloudSight API Client for Python programming language. It has been
tested with Python versions 2.7 and 3.5.

Status
======

This package is currently in **beta** status. It means the API may still change
in **backwards incompatible** way.

Installation
============

```
$ pip install cloudsight
```

Configuration
=============

You need your API key and secret (if using OAuth1 authentication). They are
available on [CloudSight site](https://cloudsightapi.com) after you sign up and
create a project.

Usage
=====

Import the `cloudsight` package:

```python
import cloudsight
```

Create an `API` instance using simple key-based authentication:

```python
auth = cloudsight.SimpleAuth('your-api-key')
api = cloudsight.API(auth)
```

Or, using OAuth1 authentication:

```python
auth = cloudsight.OAuth('your-api-key', 'your-api-secret')
api = cloudsight.API(auth)
```

Send the image request using a file:

```python
with open('your-file.jpg', 'rb') as f:
    response = api.image_request(f, 'your-file.jpg', {
        'image_request[locale]': 'en-US',
    })
```

Or, you can send the image request using a URL:

```python
response = api.remote_image_request('http://www.example.com/image.jpg', {
    'image_request[locale]': 'en-US',
})
```

Then, update the job status to see if it's already processed:

```python
status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    pass
```

It usually takes 6-12 seconds to receive a completed response. You may use
`wait()` method to wait until the image is processed:

```python
status = api.wait(response['token'], timeout=30)
```
