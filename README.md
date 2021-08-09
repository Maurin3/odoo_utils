# Odoo Utils

Modules to make easier the development of Odoo modules

**NB** : **Make sure you know what you're doing when installing these modules.**

## Installation

Clone this repository and add the repository to the addons (`addons-path`) then install the modules (`-i module_name`)

## Modules list

|Name                |Version|Summary                                                                                                            |
|:------------------:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
|custom_safe_eval    |1.0.2  |Rewrites the safe_eval to let (i)pdb, print function to be used in server actions, crons, automated actions, ...   |

**NB** : 

* To remove the traceback of some missing file linked to ir.attachment model, you can add to your command line : `--log-handler odoo.addons.base.models.ir_attachment:WARNING`
