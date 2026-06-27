/** @odoo-module */

import { registry } from '@web/core/registry';
const { Component , useState } = owl;

export class owlMenu extends Component{
    setup(){
        this.state = useState({value:1})
    }
}
owlMenu.template = 'owl_menu_template';
registry.category('actions').add('owl_menu_action', owlMenu)