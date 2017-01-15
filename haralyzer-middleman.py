#!/bin/env python
# Comment Test
import requests
import time
import os

# GTMetrix User Name
GT_METRIX_USER_NAME = os.environ.get('GT_METRIX_USER_NAME')
# GTMetrix API Key
GT_METRIX_API_KEY = os.environ.get('GT_METRIX_API_KEY')
# Default Base URL is set to GTMetrix API
BASE_URL = os.environ.get('BASE_URL', 'https://gtmetrix.com/api/0.1/test')
# REST API That data will be posted to!
# API_SERVER = 'http://205.186.162.214:5000/tests/'
API_SERVER = os.environ.get('API_SERVER' 'http://localhost:5000/api/')


def create_test(url):
    """ Creates a GTMetrix Test, returns JSON data """
    data = {'url': url}
    r = requests.post(url=BASE_URL, auth=(USER_NAME, API_KEY), data=data)
    return r.json()


def get_results(poll_url):
    """ Checks to see if the test has completed on GTMetrix, returns true if test is finished """
    url_done = requests.get(url=poll_url, auth=(USER_NAME, API_KEY))
    if url_done.json()['status'] == 'completed':
        return url_done.json()
    elif url_done.json()['status'] == 'error':
        raise ValueError(url_done.json()['error'])
    else:
        return False


def post_har_data(har_url):
    """Post HAR file data to the REST API """
        data = requests.get(har_url, auth=(USER_NAME, API_KEY))
        r = requests.post(API_SERVER, data={'har_data': data.text})
        r.raise_for_status()


def main()
    test_data = create_test("https://google.com")
    test_results = get_results(test_data['poll_state_url'])
    while not test_results:
        test_results = get_results(test_data['poll_state_url'])
        time.sleep(2)
    har_url = test_results['har']
    post_har_data(har_url)


if __name__ == '__main__':
    main()
