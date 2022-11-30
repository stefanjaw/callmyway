# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
import requests
import json

import logging
_logging = _logger = logging.getLogger(__name__)

 
class Callmyway(http.Controller):
    
    
    
    @http.route('/callmyway/contact', auth='public', csrf=False, methods=['GET'])
    def partner_get(self, **kw):
        headers = http.request.httprequest.headers
        args = http.request.httprequest.args

        params = result = params_company = {} 
        company_int = 1
        params_company['id'] = company_int
    
        
        company_id = self.search_company(params_company)
         
        
        if key:=headers.get('key'): 
            if company_id.callmyway_key != key:
                return json.dumps( {'status' : False,'error' : 'INVALID KEY'} )
        
        else : return json.dumps( {'status' : False,'error' : 'KEY DONT SENT'} )
    
        
        if phone:=headers.get('phone'): 
            params['phone'] = phone
        else: 
            return json.dumps( {'status' : False,'error' : 'PHONE DONT SENT'} )
         
        
        contact_id = self.search_partner(params)
        
        if self.exist(contact_id.id):
            
            if self.exist(contact_id.id): result['id'] = contact_id.id
            if self.exist(contact_id.name): result['name'] = contact_id.name
            if self.exist(contact_id.phone): result['phone'] = contact_id.phone
            if self.exist(contact_id.mobile): result['mobile'] = contact_id.mobile
            if self.exist(contact_id.email): result['email'] = contact_id.email
            if self.exist(contact_id.user_id.id): result['consultant'] = contact_id.user_id.name
            if self.exist(product_id.id): result['product'] = product_id.name
            
            return json.dumps( result )
        
        else:
            result = {
            'error' : 'Contact dont found'
            }
            return json.dumps( result )
        

        
    @http.route('/callmyway/contact', auth='public', csrf=False, methods=['POST'], type='json')
    def partner_post(self, **kw):
                
        data = (json.loads((http.request.httprequest.data).decode('utf-8'))).get('data')
        headers= http.request.httprequest.headers
        args = http.request.httprequest.args
        params_partner = params_company = confirm_partner = {}
        company_int = 1
        params_company['id'] = company_int
        company_id = self.search_company(params_company)   
        
        
        if key:=self.get_data('key'): 
            if company_id.callmyway_key != key:
                return ( {'status' : False,'error' : 'INVALID KEY'} )    
        else:
            return ( {'status' : False,'error' : 'KEY DONT SENT'} )
        
        
        if partner_name:=self.get_data('name') : params_partner['name'] = partner_name
        
        if partner_phone:=self.get_data('phone') : 
            params_partner['phone'] = partner_phone
            confirm_partner['phone'] = partner_phone
        else:
            return({"Error" : "Phone dont sent", "satus" : False})
        
        
        if partner_email:=self.get_data('email') : 
            params_partner['email'] = partner_email
            confirm_partner['email'] = partner_phone
        
        confirm_partner_id = self.search_partner(confirm_partner)
        
        if self.exist(confirm_partner_id.id) : 
            return({"Error" : "A partner already has this phone or email", "satus" : False})
        
        
        if agent_email:=self.get_data('agent_email') :
            params_agent = {}
            params_agent['email'] = agent_email
            user_id = self.search_user(params_agent)
            if self.exist(user_id.id) : params_partner['user_id'] = user_id.id
            
            
        if product_name:=self.get_data('product'):
            product_id = self.search_product(product_name)
            if self.exist(product_id.id):
                params_partner[product_id.id] = product_id.id
            
            
            
            
        partner_id = self.create_partner(params_partner)
        if self.exist(partner_id):
            params_partner['status'] = True
            params_partner['id'] = partner_id.id
        else:
            params_partner['error'] = "Error creating the contact"
            params_partner['status'] = False
            
            
        return params_partner 
            
        
        
        
        
        
    @http.route('/callmyway/contact', auth='public', csrf=False, methods=['PUT'], type='json')    
    def partner_put(self, **kw):
        data = (json.loads((http.request.httprequest.data).decode('utf-8'))).get('data')
        headers= http.request.httprequest.headers
        args = http.request.httprequest.args
        params_partner = params_company = confirm_partner = {}
        company_int = 1
        params_company['id'] = company_int
        company_id = self.search_company(params_company)   
        
        
        if key:=self.get_data('key'): 
            if company_id.callmyway_key != key:
                return ( {'status' : False,'error' : 'INVALID KEY'} )    
        else:
            return ( {'status' : False,'error' : 'KEY DONT SENT'} )
        
        
        if partner_name:=self.get_data('name') : params_partner['name'] = partner_name
        
        if partner_phone:=self.get_data('phone') : 
            params_partner['phone'] = partner_phone
            confirm_partner['phone'] = partner_phone
            
        
        if partner_email:=self.get_data('email') : 
            params_partner['email'] = partner_email
            confirm_partner['email'] = partner_email
            
            
        partner_id = self.search_partner(confirm_partner)
        
        for key in confirm_partner:
            
            confirm_partner = http.request.env['res.partner'].sudo().search([
                ( key, 'like', confirm_partner[key] )
            ])

            
            if partner_id.id not in confirm_partner.ids and len(confirm_partner.ids) > 0:
                return({"Error" : f"A partner already has this {key}", "satus" : False})
            elif len(confirm_partner.ids) > 1:
                return({"Error" : f"A partner already has this {key}", "satus" : False})
        
        
        if not self.exist(partner_id.id) : 
            return({"Error" : "Partner not found", "satus" : False})
        
        
        if agent_email:=self.get_data('agent_email') :
            params_agent = {}
            params_agent['email'] = agent_email
            user_id = self.search_user(params_agent)
            if self.exist(user_id.id) : params_partner['user_id'] = user_id.id
            
            
        if product_name:=self.get_data('product'):
            product_id = self.search_product(product_name)
            if self.exist(product_id.id):
                params_partner[product_id.id] = product_id.id
            
        
            
        partner_id.write(params_partner)
            
        
        if self.exist(partner_id):
            params_partner['status'] = True
            params_partner['id'] = partner_id.id
        else:
            params_partner['error'] = "Error creating the contact"
            params_partner['status'] = False
            
            
        return params_partner 
    
    
    
        
    def get_data(self, param):
        data = (json.loads((http.request.httprequest.data).decode('utf-8'))).get('data')
        headers= http.request.httprequest.headers
        args = http.request.httprequest.args
        
        if input:=data.get(param) : 
            return input
        elif input:=args.get(param) : 
            return input
        else:
            return False
        

    def search_user(self, params) : return self.search_in_model(params, model = "res.users")
    def search_partner(self, params) : return self.search_in_model(params, model = "res.partner")
    def search_company(self, params) : return self.search_in_model(params, model = "res.company")
    
    
    def search_in_model(self, params, model):
        result_id = {}
        for key in params:
            result_id = http.request.env[model].sudo().search([
                    (key, 'like', params[key] )
            ])
            if self.exist(result_id.id):
                break
        return result_id
    
    def search_product(self, param):
        result_id = {}
        result_id = http.request.env['product.product'].sudo().search([
                ( 'name', 'ilike', param )
        ])
        
        return result_id
    
    
    def create_partner(self, params):
        partner_id = http.request.env['res.partner'].sudo().create(params)
        return partner_id
    
    def write_partner(self, params):
        partner_id = http.request.env['res.partner'].sudo().write(params)
        return partner_id
    
    def exist(self, data):
        aux_null = [None, False, ""]
        if data in aux_null or len(str(data)) == 0:
            return False
        else:
            return True
          
    
    
