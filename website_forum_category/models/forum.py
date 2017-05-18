# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


from odoo import models, fields, api, _


class ForumCategory(models.Model):
    _name = 'forum.category'
    _order = 'sequence, id, name'
    _inherit = ['mail.thread', 'website.seo.metadata']

    name = fields.Char(
        string="Name",
        translate=True)
    sequence = fields.Integer(
        string='Sequence',
        default=1)
    forum_ids = fields.One2many(
        comodel_name='forum.forum',
        inverse_name='category_id',
        string='Forums',
        required=False,
        help="Forums by categories")


class Forum(models.Model):
    _inherit = 'forum.forum'

    @api.multi
    def _compute_post_count(self):
        for forum in self:
            domain = [('forum_id', '=', forum.id), ('state', '=', 'active')]
            forum.post_count = self.env['forum.post'].search_count(domain)

    @api.multi
    def _compute_topic_count(self):
        for forum in self:
            domain = [
                ('forum_id', '=', forum.id),
                ('state', '=', 'active'),
                ('parent_id', '=', False)]
            forum.topic_count = self.env['forum.post'].search_count(domain)

    @api.one
    def _compute_post_last_id(self):
        self.ensure_one()
        domain = [('forum_id', '=', self.id), ('state', '=', 'active')]
        posts = self.env['forum.post'].search(domain)
        if posts:
            self.post_last_id = posts[-1]
        else:
            self.post_last_id = None

    category_id = fields.Many2one(
        comodel_name='forum.category',
        string='Category',
        required=True,
        help="Forum Category")
    post_count = fields.Integer(
        string='Post Count',
        compute=_compute_post_count)
    topic_count = fields.Integer(
        string='Topic Count',
        compute=_compute_topic_count)
    post_last_id = fields.Many2one(
        comodel_name='forum.post',
        string='Last Post',
        compute=_compute_post_last_id,
        help="Last Post")

