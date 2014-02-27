<form class = "well form-horizontal" action = "/admin/link/new" method = "POST">
    <fieldset>
        <legend>new link</legend>
        <div class = "control-group">
            <label class = "control-label" for = "name">link name</label>
            <div class = "controls">
                <input type = "link" class = "input-xlarge" id="name" name="name">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "href">href</label>
            <div class = "controls">
                <input class = "input-xlarge" id="href" name="href"></input>
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
            <a class = "btn btn-large btn-danger" href = "/admin/link">cancel</a>
        </div>
    </fieldset>
</form>

%rebase admin/index
