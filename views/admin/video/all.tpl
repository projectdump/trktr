<div class = "btn-group">
    <button class = "btn btn-large btn-info dropdown-toggle">select category</button>
    <ul class="dropdown-menu">
        %for category in categories:
        <li>
            <a href="/admin/video/category/{{category['id']}}">{{category['name']}}</a>
        </li>
        %end
    </ul>
    <a class = "btn btn-large btn-primary" href = "/admin/video/new">new video</a>
    %if sortable:
    <a class = "btn btn-large btn-inverse" href = "#" id = "sortVideos">save video order</a>
    %end
</div>
<table class="table">
    <thead>
        <th>thumbnail</th>
        <th>title</th>
        <th>description</th>
        <th>category</th>
        <th>actions</th>
    </thead>
    <tbody id = "sortable">
        %for video in videos:
        <tr id = "{{video['id']}}">
        %   if "youtu" in video['thumbnail']:
            <td><img width="100px" src = "{{video['thumbnail']}}"></td>
        %   else:
            <td><img width="100px" src = "/{{video['thumbnail']}}"></td>
        %   end
            <td>{{video['title']}}</td>
            <td>{{video['description']}}</td>
            <td>{{video['category']}}</td>
            <td>
                <div class = "btn-group">
                    <a href = "/admin/video/{{video['id']}}/edit" class = "btn btn-primary">
                        edit
                    </a>
                    <a href = "/admin/video/{{video['id']}}/delete" class = "btn btn-danger">
                        delete
                    </a>
                </div>
            </td>
        </tr>
        %end
    </tbody>
</table>
%rebase admin/index
