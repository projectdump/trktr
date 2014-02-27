<form class = "well form-horizontal" action = "/admin/contact" method = "POST">
    <fieldset>
        <legend>edit Contact</legend>
        <div class = "control-group">
            <label class = "control-label" for = "contact">content</label>
            <div class = "controls">
                <textarea class = "input-xlarge wysiwyg" id="contact" name="contact">{{contact}}</textarea>
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
        </div>
    </fieldset>
</form>

%rebase admin/index
