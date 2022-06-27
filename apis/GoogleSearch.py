'''
Google Search API

Uses RapidApi's API at https://rapidapi.com/apigeek/api/google-search3 to send SERP requests to Google.

'''

from mlogger import logger
import requests
import urllib
import urllib.parse
# import urllib.request
import json

logger = logger.get_module_logger(__name__)

RAPIDAPI_GS_URL = "google-search3.p.rapidapi.com"

class GoogleSearchApi(object):

    def __init__(self, api_key):
        self._apiKey = api_key

    def queryKeyword(self, keyword):
        '''
        Makes a SERP query to the API
        :param kwyword: object with keyword, country and language
        :return: result of the query
        '''
        logger.debug(f"Keyword -> {keyword}")
        data = {
            "q": keyword["keyword"]
        }
        urlencoded = urllib.parse.urlencode(data)
        url = "https://" + RAPIDAPI_GS_URL + "/api/v1/search/" + urlencoded
        logger.debug(url)
        headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": keyword["country"],
            'X-RapidAPI-Host': RAPIDAPI_GS_URL,
            'X-RapidAPI-Key': self._apiKey
        }
        logger.debug(f"Headers: {headers}")
        resp = requests.request("GET", url, headers=headers)
        # req = urllib.request.Request(url, headers=headers)
        # resp = urllib.request.urlopen(req)
        logger.info(f"Status: {resp.status_code}")
        # read the results and parse the JSON
        if resp.status_code == 200:
            serp = resp.json()
            entries = []
            for entry in serp["results"]:
                entries.append(entry["link"])
        logger.debug(entries)
        return entries
