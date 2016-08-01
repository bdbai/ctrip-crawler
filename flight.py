#!/usr/bin/env python3

import json
import requests

class CtripFlightCrawler(object):
    def __init__(self, request_session):
        self.conditions = None
        self.request_session = request_session or requests.Session()

    def get_flights(self):
        resp = self.request_session.post(
            'https://sec-m.ctrip.com/restapi/soa2/11782/Flight/International/FlightListV2/Query',
            data=json.dumps({
                "grade": 0,
                "osource": 1,
                "params": [
                    { "typ": 1,"val": 7 },
                    { "typ": 3,"val": 1}
                ],
                "psglst": [
                    { "psgtype": 1,"psgcnt": "1" }
                ],
                "prdid": "",
                "segno": 1,
                "segs": [
                    {
                        "dcity": "BJS",
                        "acity": "SIN",
                        "ddate": "2016-08-03",
                        "segno": 1
                    }
                ],
                "sortinfo": {
                    "idx": 1,
                    "size": 100,
                    "ordby": 105,
                    "meyordby": 2,
                    "dir": 2,
                    "token": {
                        "SecondToken": "2",
                        "MultiToken": None,
                        "TransActionId": ""
                    }
                },
                "triptype": 1,
                "ver": 0,
                "head": {
                    "cid": "",
                    "ctok": "",
                    "cver": "1.0",
                    "lang": "01",
                    "sid": "8888",
                    "syscode": "09",
                    "auth": None,
                    "extension":[
                        {
                            "name": "protocal",
                            "value": "http"
                        }
                    ]
                },
                "contentType": "json"
            })
        )
        return resp.json()

    def crawl(self):
        return self.get_flights()


if __name__ == '__main__':
    crawler = CtripFlightCrawler(requests.Session())
    res = crawler.crawl()
    for flight in res['segs']:
        price = flight['policys'][0]['prices'][0]
        print(str(price['price']))
