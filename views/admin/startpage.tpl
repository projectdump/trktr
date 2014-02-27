<form class = "well form-horizontal" action = "/admin/startpage" method = "POST">
    <fieldset>
        <legend>set start page url</legend>
        <div class = "control-group">
            <label class = "control-label" for = "name">start url</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="url" name="url" value="{{url}}">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
        </div>
    </fieldset>
</form>

%rebase admin/index
