# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
import requests
import json

import logging
_logging = _logger = logging.getLogger(__name__)


class Callmyway(http.Controller):
    
    
    
    @http.route('/callmyway/contact', auth='public', csrf=False, methods=['GET'])
    def get_user(self, **kw):
        headers = http.request.httprequest.headers
        args = http.request.httprequest.args

        params = {}
        result = {} 
        
        company_int = 1
        params_company['id'] = company_int
    
        
        company_id = self.search_company(params_company)
        
        if not self.exist(company_id): 
            return ( { 'status' : False, 'error' : 'INVALID COMPANY'} )
        
        if key:=headers.get('key'): 
            if company.callmyway_key != key:
                return ( {'status' : False,'error' : 'INVALID KEY'} )
            
            else : pass
        
        else:
            return ( {'status' : False,'error' : 'KEY DONT SENT'} )
        
        
        
        
        if phone:=headers.get('phone'): 
            params['phone'] = phone
        else: 
            return json.dumps( {'status' : False,'error' : 'PHONE DONT SENT'} )
         
        
        contact_id = self.search_contact(params)
        
        if self.exist(contact_id.id):
            
            if self.exist(contact_id.id): result['id'] = contact_id.id
            if self.exist(contact_id.name): result['name'] = contact_id.name
            if self.exist(contact_id.phone): result['phone'] = contact_id.phone
            if self.exist(contact_id.mobile): result['mobile'] = contact_id.mobile
            if self.exist(contact_id.email): result['email'] = contact_id.email
            if self.exist(contact_id.user_id.id): result['consultant'] = contact_id.user_id.name
            
            return json.dumps( result )
        
        else:
            result = {
            'error' : 'CONTACT DONT FOUND'
            }
            return json.dumps( result )
        
        
        
    @http.route('/callmyway/contact', auth='public', csrf=False, methods=['POST'], type='json')
    def oruschat_post(self, **kw):
                
        data = (json.loads((http.request.httprequest.data).decode('utf-8'))).get('data')
        header= http.request.httprequest.headers
        args = http.request.httprequest.args
        params_partner= {}
        params_company = {}
        confirm_partner = {}
        company_int = 1
        params_company['id'] = company_int
    
        
        company_id = self.search_company(params_company)
        
        if not self.exist(company_id): 
            return ( { 'status' : False, 'error' : 'INVALID COMPANY'} )
        
        if key:=header.get('key'): 
            if company_id.callmyway_key != key:
                return ( {'status' : False,'error' : 'INVALID KEY'} )
            
            else : pass
        
        else:
            return ( {'status' : False,'error' : 'KEY DONT SENT'} )
        
        
        
        
        if partner_name:=data.get('name') : params_partner['name'] = partner_name
        if partner_phone:=data.get('phone') : 
            params_partner['phone'] = partner_phone
            confirm_partner['phone'] = partner_phone
        else:
            return({"Error" : "Phone dont sent", "satus" : False})
        
        if partner_email:=data.get('email') : 
            params_partner['email'] = partner_email
            confirm_partner['email'] = partner_phone
        
        confirm_partner_id = self.search_contact(confirm_partner)
        
        if self.exist(confirm_partner_id):
            return({"Error" : "A partner already has this phone or email", "satus" : False})
        
        
        if agent_email:=data.get('agent_email') :
            params_agent = {}
            params_agent['email'] = agent_email
            user_id = self.search_user(params_agent)
            if self.exist(user_id.id) : params_partner['user_id'] = user_id.id
            
            
        partner_id = self.create_partner(params_partner)
    
    
        if self.exist(partner_id):
            params_partner['status'] = True
            params_partner['id'] = partner_id.id
        else:
            params_partner['status'] = False
            
            
        return params_partner
            
        #producto, origen del interes, asesor encargado del contacto
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
   
                
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def search_user(self, params) : return self.search_in_model(params, model = "res.users")
    def search_contact(self, params) : return self.search_in_model(params, model = "res.partner")
    def search_company(self, params) : return self.search_in_model(params, model = "res.company")
    
    
    
    def search_in_model(self, params, model):
        result_id = {}
        for key in params:
            result_id = http.request.env[model].sudo().search([
                    (key, '=', params[key] )
            ])
        return result_id
    
    def create_partner(self, params):
        partner_id = http.request.env['res.partner'].sudo().create(params)
        return partner_id
    
    
    
    def exist(self, data):
        aux_null = [None, False, ""]
        if data in aux_null or len(str(data)) == 0:
            return False
        else:
            return True
         
    
    
