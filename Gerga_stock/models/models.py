# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gerga_sales(models.Model):
#     _name = 'gerga_sales.gerga_sales'
#     _description = 'gerga_sales.gerga_sales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
