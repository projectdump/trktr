<form class = "well form-horizontal" action = "/admin/video/{{video['id']}}/edit" method = "POST" enctype = "multipart/form-data">
    <fieldset>
        <input type = "hidden" name = "id" value = "{{video['id']}}">
        <legend>edit video</legend>
        <div class = "control-group">
            <label class = "control-label" for = "title">title</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="title" name="title" value = "{{video['title']}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "description">description</label>
            <div class = "controls">
                <textarea name = "description", id = "description">{{video['description']}}</textarea>
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "control_id">category</label>
            <div class = "controls">
                <select class = "input-xlarge" name = "category_id" id = "category_id">
                    <option value = "{{video['category_id']}}">{{video['category']}}</option>
                    %for category in categories:
                    <option value = "{{category['id']}}">{{category['name']}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "youtube">youtube</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="youtube" name="youtube">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "video">video</label>
            <div class = "controls">
                <input type = "file" class = "input-xlarge" id="video" name="video">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "thumbnail">thumbnail</label>
            <div class = "controls">
                <input type = "file" class = "input-xlarge" id = "thumbnail" name = "thumbnail">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/category">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
