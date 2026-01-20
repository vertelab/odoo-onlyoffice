from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError, ValidationError
import logging

_logger = logging.getLogger(__name__)

extensions = [
    "doc", 
    "docm", 
    "dot", 
    "dotm", 
    "dotx", 
    "epub", 
    "fb2", 
    "fodt", 
    "html", 
    "mht", 
    "odt", 
    "ott", 
    "oxps", 
    "pdf", 
    "rtf", 
    "txt", 
    "xps", 
    "xml", 
    "csv", 
    "fods", 
    "ods",
    "ots", 
    "xls",
    "xlsx",
    "xlsm", 
    "xlt", 
    "xltm", 
    "xltx", 
    "fodp", 
    "odp", 
    "otp", 
    "pot", 
    "potm", 
    "potx", 
    "pps", 
    "ppsm", 
    "ppsx", 
    "ppt", 
    "pptm"
]

class DmsFile(models.Model):
    _inherit = 'dms.file'

    is_oo_relevant = fields.Boolean(compute="_compute_is_oo_relevant",store=False)

    @api.depends("extension","attachment_id")
    def _compute_is_oo_relevant(self):
        for rec in self:
            if rec.extension in extensions and rec.attachment_id:
                rec.is_oo_relevant = True
            else:
                rec.is_oo_relevant = False

    def open_onlyoffice(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        access_token = self.attachment_id._generate_access_token()
        self.attachment_id.access_token = access_token
        oo_url = f"{base_url}/onlyoffice/editor/{self.attachment_id.id}?access_token={access_token}"
        return {
            'type': 'ir.actions.act_url',
            'url': oo_url,
            'target': 'new',
        }
