<form class = "well form-horizontal">
    <fieldset>
        <input type="hidden" name = "id" value = "{{category['id']}}">
        <legend>edit category</legend>
        <div class = "control-group">
            <label class = "control-label" for = "name">name</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="name" name="name" value = "{{category['name']}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_type_id">type</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "category_type_id" id = "category_type_id">
                    <option value = "{{category['category_type_id']}}">{{category['type']}}</option>
                    %for type in types:
                    <option value = "{{type['id']}}">{{type['name']}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "template">template</label>
            <div class = "controls">
                <div>
                    %if category['template'] == "contentlist":
                        <input type="radio" name="template" value = "contentlist" checked>striped list</input>
                    %else:
                        <input type="radio" name="template" value = "contentlist">striped list</input>
                    %end
                </div>
                <div>
                    %if category['template'] == "contentboxes":
                        <input type="radio" name="template" value = "contentboxes" checked>box style</input>
                    %else:
                        <input type="radio" name="template" value = "contentboxes">box style</input>
                    %end
                </div>
                <!--
                <div>
                    <a class="btn btn-small menu-uncheck-btn">uncheck</a>
                </div>
                -->
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_type_id">parent</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "parent" id = "parent">
                    <option value = "{{"" if category['parent'] == None else category['parent']}}">{{category['parent_name']}}</option>
                    <option value = ""></option>
                    %for parent in parents:
                    <option value = "{{parent['id']}}">{{parent['name']}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/category">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
