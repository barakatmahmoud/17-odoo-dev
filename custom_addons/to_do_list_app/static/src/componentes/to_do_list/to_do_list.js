/** @odoo-module */

import { registry } from "@web/core/registry";
const { Component , useState , onWillStart, useRef} = owl;
import { useService } from "@web/core/utils/hooks";

export class ToDoList extends Component{

    setup() {
        this.state = useState({
            task : {name: "", color: '#FF00000', completed: false},
            taskList: [],
            isEdit : false,
            activeId : false
        })

        this.orm = useService("orm");
        this.model = "to.do.list";
        this.searchInput = useRef('search-input');

        onWillStart(async () => {
            await this.getAllTasks();
        })
        }
        async getAllTasks(){
             this.state.taskList = await this.orm.searchRead(this.model, [], [
                "name", "color", "completed"
            ])
        }

        addTask(){
            this.clearTask();
            this.state.activeId = false;
            this.state.isEdit = false;

        }

        editTask(task){
            this.state.activeId = task.id;
            this.state.isEdit = true;
            this.state.task = {...task}
        }

        async saveTask(){
        if (this.state.isEdit){
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        else{
             await this.orm.create(this.model,[{
                name : this.state.task.name,
                color : this.state.task.color,
                completed : this.state.task.completed,
            }]);
        }
        await this.getAllTasks();
        }

        clearTask(){
            this.state.task = {name: "", color: '#FF00000', completed: false}
        }

        async deleteTask(task){
            await this.orm.unlink(this.model, [task.id]);
            await this.getAllTasks();
            this.clearTask();
        }

        async searchTask(){
            const text = this.searchInput.el.value;
            this.state.taskList = await this.orm.searchRead(this.model, [
                ['name', 'ilike', text]
            ],
            ["name", "color", "completed"])
        }

        async uncheckedTask(e, task){
            await this.orm.write(this.model, [task.id], {completed : e.target.checked})
            await this.getAllTasks();
        }

        async updateColorTask(e, task){
            await this.orm.write(this.model, [task.id], {color : e.target.value})
            await this.getAllTasks();
        }
}

ToDoList.template = 'to_do_list_template';
registry.category('actions').add('to_do_list_owl_action', ToDoList)