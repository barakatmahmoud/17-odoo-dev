import json
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request

class PropertyApi(http.Controller):
    ###CREATE OPERATION
    @http.route('/post/property', methods=['POST'], type='http', auth='none', csrf=False)
    def post_property(self):
        ## json data
        args = request.httprequest.data.decode()
        print("ARGS", args)
        ## transfer json to dictionary
        vals = json.loads(args)
        print("VALS", vals)
        ## check required field
        if not vals.get('name'):
            return request.make_json_response(
                {
                    'message': 'Field Name is Required!!',
                }, status=400
            )
        ## handle error
        try:
            ## create record
            res = request.env['property'].sudo().create(vals)
            if res:
                ## handle response
                return request.make_json_response(
                    {
                        'message': 'Property Created',
                        'name': res.name,
                        'id': res.id
                    },status=201
                )
        except Exception as error:
            return request.make_json_response(
                {
                    'message': error,
                }, status=400
            )


    ###CREATE OPERATION JSON
    @http.route('/post/property/json', methods=['POST'], type='json', auth='none', csrf=False)
    def post_property_json(self):
        ## json data
        args = request.httprequest.data.decode()
        print("ARGS", args)
        ## transfer json to dictionary
        vals = json.loads(args)
        print("VALS", vals)
        ## create record
        res = request.env['property'].sudo().create(vals)
        if res:
            ## handle response
            return(
                {
                    'message': 'Property Created',
                }
            )

    ###WRITE OPERATION
    @http.route('/update/property/<int:property_id>', methods=['PUT'], type='http', auth='none', csrf=False)
    def update_property(self, property_id):
       try:
           property_id = request.env['property'].sudo().search([('id', '=', property_id)])
           ##Check ID is right
           if not property_id:
               return request.make_json_response(
                   {
                       'message': 'ID IS INCORRECT',
                   }, status=400
               )
           args = request.httprequest.data.decode()
           print("ARGS", args)
           ## transfer json to dictionary
           vals = json.loads(args)
           print("VALS", vals)
           ## update data
           property_id.write(vals)
           return request.make_json_response(
               {
                   'message': 'Property Updated',
                   'name': property_id.name,
               }, status=200
           )
       except Exception as error:
           return request.make_json_response(
               {
                   'message': error,
               }, status=400
           )

    ###READ OPERATION
    @http.route('/read/property/<int:property_id>', methods=['GET'], type='http', auth='none', csrf=False)
    def read_property(self, property_id):
       try:
           property_id = request.env['property'].sudo().search([('id', '=', property_id)])
           ##Check ID is right
           if not property_id:
               return request.make_json_response(
                   {
                       'message': 'ID IS INCORRECT',
                   }, status=400
               )
           ## read data
           return request.make_json_response(
               {
                   'message': 'READ Property',
                   'name': property_id.name,
                   'ref': property_id.ref,
                   'post_code': property_id.post_code
               }, status=200
           )
       except Exception as error:
           return request.make_json_response(
               {
                   'message': error,
               }, status=400
           )

    ###DELETE OPERATION
    @http.route('/delete/property/<int:property_id>', methods=['DELETE'], type='http', auth='none', csrf=False)
    def delete_property(self, property_id):
       try:
           property_id = request.env['property'].sudo().search([('id', '=', property_id)])
           ##Check ID is right
           if not property_id:
               return request.make_json_response(
                   {
                       'message': 'ID IS INCORRECT',
                   }, status=400
               )
           ## delete data
           property_id.unlink()
           return request.make_json_response(
               {
                   'message': 'Property Deleted',
               }, status=200
           )
       except Exception as error:
           return request.make_json_response(
               {
                   'message': error,
               }, status=400
           )

    ###READ OPERATION LIST
    @http.route('/read/properties', methods=['GET'], type='http', auth='none', csrf=False)
    def read_properties(self):
       try:
           ## get parameter
           params = parse_qs(request.httprequest.query_string.decode('utf-8'))
           property_domain = []
           ## check Specific parameter
           if params.get('state'):
               ## add parameter to domain
               property_domain += [('state', '=', params['state'][0])]
           print("PROPERTY DOMAIN", property_domain)
           properties_ids = request.env['property'].sudo().search(property_domain)
           ##Check IDs is right
           if not properties_ids:
               return request.make_json_response(
                   {
                       'message': 'NOT FOUND PROPERTIES',
                   }, status=400
               )
           ## read data
           return request.make_json_response(
               [{
                   'message': 'READ Property',
                   'name': property_id.name,
                   'ref': property_id.ref,
                   'post_code': property_id.post_code
               }for property_id in properties_ids], status=200
           )
       except Exception as error:
           return request.make_json_response(
               {
                   'message': error,
               }, status=400
           )


