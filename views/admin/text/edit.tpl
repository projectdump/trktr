<form class = "well form-horizontal" action = "/admin/text/edit" method = "POST" role="form" enctype="multipart/form-data">
    <fieldset>
        <legend>edit text</legend>
        <input type = "hidden" name = "id" value = "{{text['id']}}">
        <div class = "form-group">
            <label class = "control-label" for = "name">text menu name</label>
            <input type = "text" class = "input-xlarge" id="name" name="name" value = "{{text['name']}}">
        </div>
        <div class = "form-group">
            <label class = "control-label" for = "control_id">category</label>
            <select class = "input-xlarge" name = "category_id" id = "category_id">
                <option value = "{{text['category_id']}}">{{text['category']}}</option>
                %for category in categories:
                <option value = "{{category['id']}}">{{category['name']}}</option>
                %end
            </select>
        </div>
        <div class = "form-group">
            <label>Size</label>
            <select class = "input-xlarge" name = "size">
                <option value = "{{text['size']}}">{{textinfo['sizestring']}}</option>
                <option value = "1">small</option>
                <option value = "2">mid</option>
                <option value = "3">big</option>
            </select>
        </div>
        <div class = "form-group">
            <label>Format</label>
            <select class = "input-xlarge" name = "format">
                <option value = "{{text['format']}}">{{textinfo['formatstring']}}</option>
                <option value = "0">landscape</option>
                <option value = "1">portrait</option>
            </select>
        </div>
        <div class = "form-group">
            <label>Position</label>
            <select class = "input-xlarge" name = "alignment">
                <option value = "{{text['alignment']}}">{{textinfo['alignmentstring']}}</option>
                <option value = "-1">left</option>
                <option value = "0">center</option>
                <option value = "1">right</option>
            </select>
        </div>
        <div class = "form-group">
            <label>Overlap</label>
            <select class = "input-xlarge" name = "overlap">
                <option value = "{{text['overlap']}}">{{textinfo['overlapstring']}}</option>
                <option value = "1">light</option>
                <option value = "2">mid</option>
                <option value = "3">strong</option>
            </select>
        </div>
        <div class = "form-group">
            <label class = "control-label" for = "picture">Cover Picture</label>
            <input type = "file" class = "" id="coverpic" name="coverpic">
        </div>
        <div class = "form-group">
            <label class = "control-label" for = "content">abstract</label>
            <textarea class = "input-xlarge wysiwyg" id="abstract" name="abstract">{{text['abstract']}}</textarea>
        </div>
        <div class = "form-group">
            <label class = "control-label" for = "content">content</label>
            <textarea class = "input-xlarge wysiwyg" id="content" name="content" rows = "25">{{text['content']}}</textarea>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/text">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
