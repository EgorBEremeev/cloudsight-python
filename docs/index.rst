Welcome to CloudSight API's documentation!
==========================================

.. toctree::
   :maxdepth: 2


.. highlight:: python


Consult full `API documentation <https://cloudsight.readme.io/v1.0/docs>`_ for
details.


Installation
------------

.. code-block:: bash

    $ pip install cloudsight


Configuration
-------------

You need your API key and secret (if using OAuth1 authentication). They are
available on `CloudSight site <https://cloudsightapi.com>`_ after you sign up
and create a project.

Usage
-----

Import the :py:mod:`cloudsight` module::

    import cloudsight

Create an :py:class:`cloudsight.API` instance using simple key-based
authentication::

    auth = cloudsight.SimpleAuth('your-api-key')
    api = cloudsight.API(auth)

Or, using OAuth1 authentication::

    auth = cloudsight.OAuth('your-api-key', 'your-api-secret')
    api = cloudsight.API(auth)

Send the image request using a file::

    with open('your-file.jpg', 'rb') as f:
        response = api.image_request(f, 'your-file.jpg', {
            'image_request[locale]': 'en-US',
        })

Or, you can send the image request using a URL::

    response = api.remote_image_request('http://www.example.com/image.jpg', {
        'image_request[locale]': 'en-US',
    })

Then, update the job status to see if it's already processed::

    status = api.image_response(response['token'])
    if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
        # Done!
        pass

It usually takes 6-12 seconds to receive a completed response. You may use
:py:meth:`cloudsight.API.wait` method to wait until the image is processed::

    status = api.wait(response['token'], timeout=30)

API parameters
--------------

**image_request[image]** *(required)*
    Image attached as a multipart-form-request part. Either this field or
    *image_request[remote_image_url]* must be provided, but not both.

**image_request[remote_image_url]** *(required)*
    URL to a remote image to use. Either this field or the
    *image_request[image]* must be provided, but not both.

**image_request[locale]** *(required)*
    The locale of the request.

**image_request[language]**
    The language of the request. Return the response in this language.

**image_request[device_id]**
    A unique ID generated for the device sending the request. We recommend
    generating a UUID.

**image_request[latitude]**
    Geolocation information for additional context.

**image_request[longitude]**
    Geolocation information for additional context.

**image_request[altitude]**
    Geolocation information for additional context.

**image_request[ttl]**
    Deadline in seconds before expired state is set. Use a high ttl for
    low-priority image requests. Set ``image_request[ttl]=max`` for maximum
    deadline.

**focus[x]**
    Focal point on image (x-coordinate) for specificity.

**focus[y]**
    Focal point on image (y-coordinate) for specificity.

API documentation
-----------------

.. py:module:: cloudsight
.. py:currentmodule:: cloudsight

Possible values for current job status:

.. py:data:: cloudsight.STATUS_NOT_COMPLETED

    Recognition has not yet been completed for this image. Continue polling
    until response has been marked completed.

.. py:data:: cloudsight.STATUS_COMPLETED

    Recognition has been completed. Annotation can be found in Name and
    Categories field of Job structure.

.. py:data:: cloudsight.STATUS_NOT_FOUND

    Token supplied on URL does not match an image.

.. py:data:: cloudsight.STATUS_SKIPPED

    Image couldn't be recognized because of a specific reason. Check the
    `reason` field.

.. py:data:: cloudsight.STATUS_TIMEOUT

    Recognition process exceeded the allowed TTL setting.

The API may choose not to return any response for given image. Below constants
include possible reasons for such behavior.

.. py:data:: cloudsight.REASON_OFFENSIVE

    Offensive image content.

.. py:data:: cloudsight.REASON_BLURRY

    Too blurry to identify.

.. py:data:: cloudsight.REASON_CLOSE

    Too close to identify.

.. py:data:: cloudsight.REASON_DARK

    Too dark to identify.

.. py:data:: cloudsight.REASON_BRIGHT

    Too bright to identify.

.. py:data:: cloudsight.REASON_UNSURE

    Content could not be identified.

.. autoclass:: cloudsight.API
    :members: __init__, image_request, remote_image_request, image_response, repost, wait

.. autoclass:: cloudsight.SimpleAuth
    :members:

.. autoclass:: cloudsight.OAuth
    :members:

.. autoclass:: cloudsight.APIError



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

