# encoding: utf-8

import unittest
import cloudsight
import vcr

class ApiTest(unittest.TestCase):

    def testAuth(self):
        auth = cloudsight.SimpleAuth('your-api-key')

        assert auth.key == 'your-api-key'

    def testNewApi(self):
        auth = cloudsight.SimpleAuth('your-api-key')
        api = cloudsight.API(auth)

        assert api.auth == auth

    @vcr.use_cassette('fixtures/vcr_cassettes/send_request.yaml')
    def testSendRequest(self):
        auth = cloudsight.SimpleAuth('test-token')
        api = cloudsight.API(auth)
        response = api.remote_image_request('https://storage.googleapis.com/iex/api/logos/AAPL.png', {
            'image_request[locale]': 'en-US',
        })

        assert response['status'] == 'not completed'
        assert response['token']  == 'BjMGgyIZQt7QNPNZKmzq2A'

    @vcr.use_cassette('fixtures/vcr_cassettes/get_response_completed.yaml')
    def testGetCompletedResponse(self):
        auth = cloudsight.SimpleAuth('test-token')
        api = cloudsight.API(auth)

        response = api.image_response('BjMGgyIZQt7QNPNZKmzq2A')

        assert response['status'] == 'completed'
        assert response['token']  == 'BjMGgyIZQt7QNPNZKmzq2A'
        assert response['name']   == 'Apple logo'
