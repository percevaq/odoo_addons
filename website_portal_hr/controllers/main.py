# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


import datetime

from odoo import http, _
from odoo.http import request

from odoo.addons.website_portal.controllers.main import website_account


class PortalHrWebsiteAccount(website_account):

    def get_employee(self):
        user = request.env.user
        if user.employee_ids:
            return user.employee_ids and user.employee_ids[0]
        return None

    def _prepare_contracts(self):
        employee_id = self.get_employee()
        contracts = request.env['hr.contract'].sudo().search([
            ('employee_id', '=', employee_id)])
        return contracts

    def _prepare_payslips(self):
        employee_id = self.get_employee()
        payslips = request.env['hr.payslip'].sudo().search([
            ('employee_id', '=', employee_id), ('state', '=', 'done')])
        return payslips

    def _prepare_portal_layout_values(self):
        values = super(PortalHrWebsiteAccount, self)._prepare_portal_layout_values()
        if not request.env.user.employee_ids:
            return values
        employee_id = self.get_employee()
        contracts_count = request.env['hr.contract'].sudo().search_count([
            ('employee_id', '=', employee_id)])
        payslips_count = request.env['hr.payslip'].sudo().search_count([
            ('employee_id', '=', employee_id), ('state', '=', 'done')])
        values.update({
            'contracts_count': contracts_count,
            'payslips_count': payslips_count,
            })
        return values

    @http.route(['/my/hr/contracts'], type='http', auth='user', website=True)
    def contracts(self, **kw):
        values = self._prepare_portal_layout_values()
        contracts = self._prepare_contracts()
        values.update({
            'contracts': contracts,
            'page_name': 'contract',
            'default_url': '/my/hr/contracts',
        })

        return request.render('website_portal_hr.contracts', values)

    @http.route(
        ['/my/hr/contracts/<int:contract_id>'], type='http', auth='user',
        website=True)
    def contract(self, contract_id=None):
        contract = request.env['hr.contract'].sudo().search([
            ('id', '=', contract_id)])
        if not contract:
            return request.render("website.404")
        attachments = request.env['ir.attachment'].sudo().search([
            ('res_model', '=', 'hr.contract'),
            ('res_id', '=', contract.id)
        ])
        return request.render("website_portal_hr.contract_details", {
            'contract': contract,
            'attachments': attachments,
            'page_name': 'contract',
        })

    @http.route(['/my/hr/payslips'],
                type='http', auth='user', website=True)
    def payslips(self, page=1, **kwargs):
        employee_id = self.get_employee()

        values = self._prepare_portal_layout_values()
        payslips = self._prepare_payslips()
        values.update({
            'payslips': payslips,
            'page_name': 'payslip',
            'default_url': '/my/hr/payslips',
        })

        return request.render('website_portal_hr.payslips', values)

    @http.route(
        ['/my/hr/payslips/<int:payslip_id>'], type='http', auth='user',
        website=True)
    def payslip(self, payslip_id=None):
        payslip = request.env['hr.payslip'].sudo().search([
            ('id', '=', payslip_id), ('state', '=', 'done')])
        employee_id = self.get_employee()
        if not payslip or not employee_id:
            return request.render("website.404")
        attachments = request.env['ir.attachment'].sudo().search([
            ('res_model', '=', 'hr.payslip'),
            ('res_id', '=', payslip_id)])
        return request.render("website_portal_hr.payslip_details", {
            'payslip': payslip,
            'attachments': attachments,
            'page_name': 'payslip',
        })
