# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.


import os.path
import logging
from openerp import models, fields, api, exceptions, _


_log = logging.getLogger(__name__)


class DocumentDirectoryContentType(models.Model):
    _inherit = 'document.directory.content.type'

    code = fields.Char(
        size=64)
    icon = fields.Char(
        string='Icon',
        required=False,
        help="Relative Url localize icon")


class DocumentFile(models.Model):
    _inherit = 'ir.attachment'

    @api.multi
    def _compute_icon(self):
        for document in self:
            file_ext = os.path.splitext(
                document.datas_fname or '')[1].lower()[0:]
            if file_ext:
                type_id = self.env['document.directory.content.type'].search([
                    ('code', '=', file_ext), ('active', '=', True)])
            else:
                type_id = None
            document.file_type_icon = type_id and type_id.icon or 'blank-file'

    file_type_icon = fields.Char(compute=_compute_icon)
