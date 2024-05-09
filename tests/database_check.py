import odoorpc

odoo = odoorpc.ODOO('localhost', port=8069)

print(odoo.db.list())