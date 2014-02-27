<form class = "well form-horizontal" action = "/admin/meta" method = "POST">
    <fieldset>
        <legend>define page keywords</legend>
        <div class = "control-group">
            <label class = "control-label" for = "description">description</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="description" name="description" value="{{description}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "keywords">keywords</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="keywords" name="keywords" value="{{keywords}}">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "author">author</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="author" name="author" value="{{author}}">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
        </div>
    </fieldset>
</form>

%rebase admin/index
