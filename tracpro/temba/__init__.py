from __future__ import unicode_literals

import requests
import time

from django.conf import settings


class TembaException(Exception):
    def __init__(self, msg, caused_by=None):
        self.msg = msg
        self.caused_by = caused_by

    def __unicode__(self):
        text = self.msg
        if self.caused_by:
            text += "\ncaused by:\n%s" % self.caused_by
        return text


class TembaAPI(object):
    def __init__(self, host, token, ssl=True):
        self.root_url = '%s://%s/api/v1' % ('https' if ssl else 'http', host)
        self.token = token

    def get_contact(self, uuid):
        return self._get_single('contacts', uuid=uuid)

    def get_group(self, uuid):
        return self._get_single('groups', uuid=uuid)

    def get_groups(self):
        return self._get_all('groups')

    def _get_single(self, endpoint, **kwargs):
        """
        Gets a single result from the given endpoint. Return none if there are no results and throws an exception if
        there are multiple results.
        """
        url = '%s/%s.json' % (self.root_url, endpoint)

        response = self._get(url, **kwargs)
        num_results = len(response['results'])

        if num_results > 1:
            raise TembaException("Request for single object returned %d objects" % num_results)
        elif num_results == 0:
            return None
        else:
            return response['results'][0]

    def _get_all(self, endpoint, **kwargs):
        """
        Gets all results from the given endpoint
        """
        start = time.time()
        num_requests = 0
        results = []

        url = '%s/%s.json' % (self.root_url, endpoint)
        while url:
            response = self._get(url, **kwargs)
            num_requests += 1
            results += response['results']
            url = response['next']

        if settings.DEBUG:  # pragma: no cover
            print "Fetched all from endpoint '%s' in %f (%d requests)" % (endpoint, time.time() - start, num_requests)

        return results

    def _get(self, url, **kwargs):
        """
        Makes a GET request to the given URL and returns the parsed JSON
        """
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': 'Token %s' % self.token}
        try:
            response = requests.get(url, params=kwargs, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError, ex:
            raise TembaException("Request error", ex)