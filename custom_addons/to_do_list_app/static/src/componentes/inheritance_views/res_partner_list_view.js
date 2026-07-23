/** @odoo-module */

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { useService } from "@web/core/utils/hooks";

class ResPartnerListController extends ListController {
    setup(){
        super.setup();
        this.action = useService("action");
    }
    getSales(){
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Customer Orders",
            res_model: "sale.order",
            views:[[false, 'list'], [false, 'form']]
        });
    }
}

export const resPartnerListViewController = {
    ...listView,
    Controller: ResPartnerListController,
    buttonTemplate : "to_do_list_app.ListViewInherit.Buttons.Inherit"
}

registry.category('views').add("res_partner_list_controller", resPartnerListViewController)