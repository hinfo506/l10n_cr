# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    bccr_username = fields.Char(string="Nombre de usuario del BCCR", required=False, )
    bccr_email = fields.Char(string="e-mail registrado en el BCCR", required=False, )
    bccr_token = fields.Char(string="Token para utilizar en el BCCR", required=False, )
    
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            bccr_username=get_param('bccr_username'),
            bccr_email=get_param('bccr_email'),
            bccr_token=get_param('bccr_token'),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('bccr_username', self.bccr_username)
        set_param('bccr_email', self.bccr_email)
        set_param('bccr_token', self.bccr_token)

