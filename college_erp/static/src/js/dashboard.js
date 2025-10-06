/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class CollegeDashboard extends Component {
    setup() {
        this.rpc = useService("rpc");
        this.state = {
            data: {},
            isLoading: true
        };
        this.loadDashboardData();
    }

    async loadDashboardData() {
        try {
            const data = await this.rpc("/web/dataset/call_kw/college.dashboard/get_dashboard_data", {
                model: "college.dashboard",
                method: "get_dashboard_data",
                args: [[]],
                kwargs: {}
            });
            this.state.data = data;
            this.state.isLoading = false;
            this.render();
        } catch (error) {
            console.error("Error loading dashboard data:", error);
            this.state.isLoading = false;
        }
    }
}

CollegeDashboard.template = "college_erp.DashboardTemplate";

registry.category("actions").add("college_dashboard", CollegeDashboard);
