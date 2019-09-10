#!/usr/bin/env python3

import json
import requests

class CtripFlightCrawler(object):
    def __init__(self, request_session):
        self.conditions = None
        self.request_session = request_session or requests.Session()

    def get_flights(self):
        resp = self.request_session.post(
            'https://sec-m.ctrip.com/restapi/soa2/13212/flightListSearch',
            headers={
                'referer': 'x',
                'content-type': 'application/json'
            },
            data=json.dumps({
                "searchitem": [
                    {
                        "dccode": "SHA",
                        "accode": "SIN",
                        "dtime": "2019-09-11",
                    }
                ],
                "psgList": [{
                    "type": 1,
                    "count": 1
                }],
                "trptpe": 1,
                "head": { },
                "seat": 0,
                "segno": 1
            })
        )
        return resp.json()

    def crawl(self):
        return self.get_flights()


if __name__ == '__main__':
    crawler = CtripFlightCrawler(requests.Session())
    res = crawler.crawl()
    for flight in res['fltitem']:
        price = flight['policyinfo'][0]['priceinfo'][0]
        print(str(price['price'] + price['tax']))
