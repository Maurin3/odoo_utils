# -*- coding: utf-8 -*-

from odoo.tools.safe_eval import _BUILTINS
import pdb
import ipdb

_BUILTINS['print'] = print
_BUILTINS['pdb'] = pdb
_BUILTINS['ipdb'] = ipdb
