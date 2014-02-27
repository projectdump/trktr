<div class = "btn-group">
    <a class = "btn btn-large btn-primary" href = "/admin/link/new">new link</a>
    <a class = "btn btn-large btn-inverse" href = "#" id = "sortLinks">save link order</a>
</div>

<table class="table">
    <thead>
        <tr>
            <th>name</th>
            <th>action</th>
        </tr>
    </thead>
    <tbody id = "sortable">
        %for link in links:
        <tr id = "{{link['id']}}">
            <td>{{link['name']}}</td>
            <td>
                <div class = "btn-group">
                <a href = "/admin/link/{{link['id']}}/edit" class = "btn btn-primary">
                    edit
                </a>
                <a href = "/admin/link/{{link['id']}}/delete" class = "btn btn-danger">
                    delete
                </a>
                </div>
        </tr>
        %end
    </tbody>
</table>
%rebase admin/index
