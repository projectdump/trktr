<form class = "well form-horizontal" action = "/admin/picture/new" method = "POST" enctype = "multipart/form-data">
    <fieldset>
        <legend>new picture</legend>
        <div class = "control-group">
            <label class = "control-label" for = "title">title</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="title" name="title">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "description">description</label>
            <div class = "controls">
                <input name = "description", id = "description" name="title" class = "input-xlarge" type = "text">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_id">gallery</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "category_id" id = "category_id">
                    %for category in categories:
                    <option value = "{{category['id']}}">{{category['name']}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "picture">picture</label>
            <div class = "controls">
                <input type = "file" class = "" id="picture" name="picture">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/picture">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
