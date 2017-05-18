# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import http, modules, SUPERUSER_ID, tools, _
from odoo.http import request

from odoo.addons.website_forum.controllers.main import WebsiteForum


class WebsiteForum(WebsiteForum):

    @http.route(
        ['/forum_categories'], type='http', auth='public', website=True)
    def forum_categories(self, **kwargs):
        categories = request.env['forum.category'].sudo().search([])
        return request.render(
            'website_forum_category.categories', {'categories': categories})
