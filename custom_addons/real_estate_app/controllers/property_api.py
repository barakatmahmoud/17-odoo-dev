import json

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