<form class = "well form-horizontal" action = "/admin/link/edit" method = "POST">
    <fieldset>
        <legend>edit link</legend>
        <input type = "hidden" name = "id" value = "{{link['id']}}">
        <div class = "control-group">
            <label class = "control-label" for = "name">link name</label>
            <div class = "controls">
                <input type = "link" class = "input-xlarge" id="name" name="name" value = "{{link['name']}}">
            </div>
        </div>
        <div class = "control-group">
            <div class = "controls">
                <input class = "input-xlarge" id="href" name="href" value="{{link['href']}}">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/link">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
