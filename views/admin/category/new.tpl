<form class = "well form-horizontal">
    <fieldset>
        <legend>new category</legend>
        <div class = "control-group">
            <label class = "control-label" for = "name">name</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="name" name="name">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_type_id">type</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "category_type_id" id = "category_type_id">
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
                    <input type="radio" name="template" value = "contentlist" checked>striped list</input>
                </div>
                <div>
                    <input type="radio" name="template" value = "contentboxes">box style</input>
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
                    <option value = "NULL"></option>
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
