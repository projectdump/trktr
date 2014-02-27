<form class = "well form-horizontal" action = "/admin/picture/edit" method = "POST" enctype = "multipart/form-data">
    <fieldset>
        <legend>edit picture</legend>
        <input type = "hidden" name = "id" value = "{{picture['id']}}">
        <div class = "control-group">
            <label class = "control-label" for = "title">title</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="title" name="title" value = "{{picture['title']}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "description">description</label>
            <div class = "controls">
                <input class = "input-xlarge" type = "text" name = "description", id = "description" value = "{{picture['description']}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_id">gallery</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "category_id" id = "category_id">
                    <option value = "{{picture['category_id']}}">{{picture['category']}}</option>
                    %for category in categories:
                    <option value = "{{category['id']}}">{{category['name']}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "picture">picture</label>
            <div class = "controls">
                <input type = "file" class = "input-xlarge" id="picture" name="picture">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/picture">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
