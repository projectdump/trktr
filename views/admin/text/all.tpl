<div class = "btn-group">
    <button class = "btn btn-large btn-info dropdown-toggle">select category</button>
    <ul class="dropdown-menu">
        %for category in categories:
        %   linkname = category['name']
        %   if category['parent'] != None:
        %       linkname += " ("+category['parent']+")"
        %   end
        <li>
            <a href="/admin/text/category/{{category['id']}}">{{linkname}}</a>
        </li>
        %end
    </ul>
    <a class = "btn btn-large btn-primary" href = "/admin/text/new">new text</a>
    <a class = "btn btn-large btn-inverse" href = "#" id = "sortTexts">save text order</a>
</div>

<table class="table">
    <thead>
        <tr>
            <th>title</th>
            <th>category</th>
            <th>action</th>
        </tr>
    </thead>
    <tbody id = "sortable">
        %for text in texts:
        <tr id = "{{text['id']}}">
            <td>{{text['name']}}</td>
            <td>{{text['category']}}</td>
            <td>
                <div class = "btn-group">
                <a href = "/admin/text/{{text['id']}}/edit" class = "btn btn-primary">
                    edit
                </a>
                <a href = "/admin/text/{{text['id']}}/delete" class = "btn btn-danger">
                    delete
                </a>
                </div>
        </tr>
        %end
    </tbody>
</table>
%rebase admin/index
