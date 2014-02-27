<form class = "well form-horizontal" action = "/admin/password" method = "POST">
    <fieldset>
        <legend>set password</legend>
        <div class = "control-group">
            <label class = "control-label" for = "password">old password</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="oldpassword" name="oldpassword" >
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "password">new password</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="newpassword" name="newpassword">
            </div>
        </div>
        <div class = "control-group">
            <label class = "control-label" for = "password">type new password again</label>
            <div class = "controls">
                <input type = "text" class = "input-xlarge" id="newpassword3" name="newpassword2">
            </div>
        </div>
        <div class = "form-actions">
            <input type = "submit" name = "save" class = "btn btn-large btn-primary">
        </div>
    </fieldset>
</form>

%rebase admin/index
