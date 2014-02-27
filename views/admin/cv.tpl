<form class = "well form-horizontal" action = "/admin/cv" method = "POST">
    <fieldset>
        <legend>edit CV</legend>
        <div class = "control-group">
            <label class = "control-label" for = "cv">content</label>
            <div class = "controls">
                <textarea class = "input-xlarge wysiwyg" id="cv" name="cv">{{cv}}</textarea>
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
        </div>
    </fieldset>
</form>

%rebase admin/index
