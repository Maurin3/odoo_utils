# Odoo Utils

Modules to make easier the development of Odoo modules

**NB** : **Make sure you know what you're doing when installing these modules.**

## Installation

Clone this repository and add the repository to the addons (`addons-path`) then install the modules (`-i module_name`)

## Modules list

|Name                |Version|Summary                                                                                                            |
|:------------------:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
|custom_safe_eval    |1.0.2  |Rewrites the safe_eval to let (i)pdb, print function to be used in server actions, crons, automated actions, ...   |
|custom_error_logs   |1.0.2  |Rewrites _file_read method of ir.attachment model to avoid the display of the traceback                            |
