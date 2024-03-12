import os, sys, requests, bs4

		

def guard():
	cookie = input ("\n- masukkan cookie fb : ")
	token = input ("- masukan token fb : ")
	open('cookie.txt','w').write(cookie)
	open('token.txt','w').write(token)
	print("\n1. aktifkan propil guard facebook ")
	print("2. nonaktifkan propil guard")
	print("0. log out ")
	
	tanya = input ("\n- pilih : ")
	if tanya == "":
		print ("\n- ngetik yang bener dong sayang !!!")
		exit()
	elif tanya =="1" or tanya =="01":
		scrap1(True)
	elif tanya =="2" or tanya =="02":
		scrap1(False)
	elif tanya =="0" or tanya =="00":
		exit()
	else:
		print ("\n- ngetik yang bener dong sayang !!!")
		exit()
		

		
	

def get_id():
	token = open("token.txt","r").read()
	cok = open("cookie.txt","r").read()
	cookie = {"cookie":cok}
	id = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token),cookies={"cookie":cok}).json()["id"]	    
	return (id)
	

def scrap1(stat):
	token = open("token.txt","r").read()
	cok = open("cookie.txt","r").read()
	cookie = {"cookie":cok}
	id   = get_id()
	
	
	
	var  = {
            '0': {
                'is_shielded'        : stat,
                'session_id'         : '9b78191c-84fd-4ab6-b0aa-19b39f04a6bc',
                'actor_id'           : str(id),
                'client_mutation_id' : 'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
	
	data = {
            'variables'                : json.dumps(var),
            'method'                   : 'post',
            'doc_id'                   : '1477043292367183',
            'query_name'               : 'IsShieldedSetMutation',
            'strip_defaults'           : 'true',
            'strip_nulls'              : 'true',
            'locale'                   : 'en_US',
            'client_country_code'      : 'US',
            'fb_api_req_friendly_name' : 'IsShieldedSetMutation',
            'fb_api_caller_class'      : 'IsShieldedSetMutation'}
            
	
	head = {
            'Content-Type'  : 'application/x-www-form-urlencoded',
            'Authorization' : 'OAuth %s'%token}
     
	url  = 'https://graph.facebook.com/graphql'
	req  = requests.post(url, data=data, headers=head, cookies=cookie)
	if '"is_shielded":true' in req.text:
		print("\n- berhasil mengaktifkan profil guard")
		exit()
	elif '"is_shielded":false' in req.text:
		print("\n- berhasil menonaktifkan profil guard")
		exit()
		
guard()

