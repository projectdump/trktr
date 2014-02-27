%import os
<div class = "btn-group">
    <button class = "btn btn-large btn-info dropdown-toggle">select category</button>
    <ul class="dropdown-menu">
        %for category in categories:
        <li>
            <a href="/admin/picture/category/{{category['id']}}">{{category['name']}}</a>
        </li>
        %end
    </ul>
    <a class = "btn btn-large btn-primary" href = "/admin/picture/new">new picture</a>
    %if sortable:
    <a class = "btn btn-large btn-inverse" href = "#" id = "sortPictures">save picture order</a>
    %end
</div>
<table class="table">
    <thead>
        <th>picture</th>
        <th>title</th>
        <th>description</th>
        <th>gallery</th>
        <th>actions</th>
    </thead>
    <tbody id = "sortable">
        %for picture in pictures:
        %fn, ext = os.path.splitext(picture['path'])
        %thumbnail = "/assets/picture"+str(picture['id'])+"thumb"+ext
        %path = "/assets/picture"+str(picture['id'])+ext
        <tr id = "{{picture['id']}}">
            <td>
                <a href = "{{path}}">
                <img height="50px" src = "{{thumbnail}}"></td>
                </a>
            <td>{{picture['title']}}</td>
            <td>{{picture['description']}}</td>
            <td>{{picture['category']}}</td>
            <td>
                <div class = "btn-group">
                    <a href = "/admin/picture/{{picture['id']}}/edit" class = "btn btn-primary">
                        edit
                    </a>
                    <a href = "/admin/picture/{{picture['id']}}/delete" class = "btn btn-danger">
                        delete
                    </a>
                </div>
            </td>
        </tr>
        %end
    </tbody>
</table>
%rebase admin/index
