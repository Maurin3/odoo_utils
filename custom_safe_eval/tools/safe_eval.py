# -*- coding: utf-8 -*-

from odoo.tools.safe_eval import _BUILTINS
from pprint import pprint

import pdb
import ipdb

_BUILTINS['print'] = print
_BUILTINS['pprint'] = pprint
_BUILTINS['pdb'] = pdb
_BUILTINS['ipdb'] = ipdb
