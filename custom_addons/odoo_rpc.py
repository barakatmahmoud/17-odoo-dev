import odoorpc

odoo = odoorpc.ODOO('localhost', port='8069')
print(odoo.db.list())

odoo.login('DB17', 'admin', '123')

property = odoo.env['property'].search([])
print("property>>>", property)

property_obj = odoo.env['property'].browse(property)
print('property_obj>>>>', property_obj)
for p in property_obj :
    p.write({
        'living_area' : 10
    })
# print(property_obj.living_area)
print("RUN SUCCESSFULLY!!!")
