/** @odoo-module */

import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { useService } from "@web/core/utils/hooks";

class ResPartnerKanbanController extends KanbanController {
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

export const resPartnerKanbanViewController = {
    ...kanbanView,
    Controller: ResPartnerKanbanController,
    buttonTemplate : "to_do_list_app.kanbanViewInherit.Buttons.Inherit"
}

registry.category('views').add("res_partner_kanban_controller", resPartnerKanbanViewController)