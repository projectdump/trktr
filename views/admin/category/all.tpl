<div class = "btn-group">
    <a class = "btn btn-large btn-primary" href = "/admin/category/new">new category</a>
    %if sortable:
    <a class = "btn btn-large btn-inverse" href = "#" id = "sortCategories">save category order</a>
    %end
</div>

<table class="table">
    <thead>
        <tr>
            <th>name</th>
            <th>type</th>
            <th>parent</th>
            <th>template</th>
            <th>action</th>
        </tr>
    </thead>
    <tbody id = "sortable">
        %for category in categories:
        <tr id = "{{category['id']}}">
            <td>{{category['name']}}</td>
            <td>{{category['type']}}</td>
            <td>{{category['parent_name']}}</td>
            <td>{{category['template']}}</td>
            <td>
                <div class = "btn-group">
                <a href = "/admin/category/{{category['id']}}/edit" class = "btn btn-primary">
                    edit
                </a>
                <a href = "/admin/category/{{category['id']}}/delete" class = "btn btn-danger">
                    delete
                </a>
                </div>
        </tr>
        %end
    </tbody>
</table>

%rebase admin/index
