# -*- coding: utf-8 -*-

from odoo import models, fields

class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    DEFAULT_PYTHON_CODE = """
# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - Warning: Warning Exception to use with raise
# To return an action, assign: action = {...}
# 
# Additional custom variables (!! don't save Odoo's logs inside a file and check your terminal !!):
#  - print: printing a message in Odoo's logs
#  - (i)pdb: adding a breakpoint inside the action (mostly used as '(i)pdb.set_trace()')
\n\n\n\n
"""

    code = fields.Text(string='Python Code', groups='base.group_system',
                       default=DEFAULT_PYTHON_CODE,
                       help="Write Python code that the action will execute. Some variables are "
                            "available for use; help about python expression is given in the help tab.")