# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Incoterms(models.Model):
    _inherit = 'stock.incoterms'

    @api.multi
    def name_get(self):
        result = []
        for incoterm in self:
            result.append((incoterm.id, "%s - %s" % (
                incoterm.code or '', incoterm.name or '')))
        return result

    name = fields.Char(translate=True)
