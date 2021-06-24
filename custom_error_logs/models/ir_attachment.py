# -*- coding: utf-8 -*-
from odoo import api, models

from odoo.tools.parse_version import parse_version


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def _file_read(self, fname, bin_size=False):
        self.env.cr.execute("""
            SELECT latest_version 
            FROM ir_module_module 
            WHERE name = 'base';
        """)
        version = parse_version(self.env.cr.fetchone()[0])
        if int(version[0]) < 14:
            res = ''
            try:
                return super()._file_read(fname, bin_size)
            except (IOError, OSError):
                pass
            return res
        else:
            try:
                return super()._file_read(fname)
            except (IOError, OSError):
                pass
            return b''
