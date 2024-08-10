from odoo import models, fields, api

class SaleOrder(models.Model):
    # _name = 'total_delivery'
    _inherit = 'sale.order'
    currency_id = fields.Many2one('res.currency', string="Currency",
                                 related='company_id.currency_id',
                                 default=lambda
                                 self: self.env.user.company_id.currency_id.id)
    
    total_delivered_amount = fields.Monetary(string='Total Delivered Amount', compute='_compute_total_delivered_amount',compute_sudo=True)

    @api.depends('order_line')
    def _compute_total_delivered_amount(self):
        for order in self:
            #filter lines where only get delivered lines
            filtered_lines = order.order_line.filtered(lambda x: x.qty_delivered > 0)

            # go through the lines and multiply qty_delivered * unit price, then sum it
            total_amount = sum(line.qty_delivered * line.price_unit for line in filtered_lines)

            # TODO : add in line taxes

            # pass the total amount delivered to the model field
            order.total_delivered_amount = total_amount * 1.19
