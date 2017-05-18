# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.

import logging
from odoo import models, fields, api


_log = logging.getLogger(__name__)


class AttachmentType(models.Model):
    _name = 'ir.attachment.mimetype'
    _description = 'Attachment MimeType'

    code = fields.Char(
        size=64)
    active = fields.Boolean(
        string='Active',
        default=True,
        help="Active")
    name = fields.Char(
        string='Name',
        required=True,
        help="Content Name")
    mime_type = fields.Char(
        string='MimeType',
        required=True,
        help="Universal Mimetype")
    icon = fields.Char(
        string='Icon',
        required=False,
        help="Relative Url localize icon")


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    @api.multi
    def _compute_icon(self):
        for document in self:
            if document.mimetype:
                type_id = self.env['ir.attachment.mimetype'].search([
                    ('mime_type', '=', document.mimetype),
                    ('active', '=', True)])
            else:
                type_id = self.env.ref('document_icon._blank')
            document.file_type_icon = type_id and type_id.icon

    file_type_icon = fields.Char(
        string='Icon',
        compute=_compute_icon)
