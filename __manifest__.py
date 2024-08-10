{
    'name': 'Total Livré',
    'version': '0.1',
    'license':'LGPL-3',
    'category': 'Sales',
    'summary': 'Add field Total livré to sales order',
    'description': """
        Add field total livré to sales order triggered after qty_delivered in model sale.order.line is updated.
    """,
    'author': 'Saad BOUTERAA',
    'website': 'https://tbgroup-dz.com',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/sale_order_tree.xml'

        # 'views/res_partner_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
