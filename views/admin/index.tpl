<link rel = "stylesheet" href = "/css/bootstrap.css" type="text/css">
<link rel = "stylesheet" href = "/css/cms.css" type = "text/css">
<script src = "/js/jquery-1.10.2.min.js"></script>
<script src="/js/ui/jquery.ui.core.js"></script>
<script src="/js/ui/jquery.ui.widget.js"></script>
<script src="/js/ui/jquery.ui.mouse.js"></script>
<script src="/js/ui/jquery.ui.sortable.js"></script>
<script src = "/js/jquery.browser.min.js"></script>
<script src = "/js/bootstrap.js"></script>
<script src = "/js/tiny_mce/tiny_mce.js"></script>
<br>
<div class = "container" style = "font-weight:bold; font-size:18px;">
    <ul class = "nav nav-pills">
        <li>
            <a href = "/admin/category">
                Categories
            </a>
        </li>
        <li>
            <a href = "/admin/text">
                Texts
            </a>
        </li>
        <li>
            <a href = "/admin/picture">
                Pictures
            </a>
        </li>
        <li>
            <a href = "/admin/video">
                Videos
            </a>
        </li>
        <li>
            <a href = "/admin/stuff">
                Impressum/Footer/Meta
            </a>
        </li>

        <!---
        <li>
            <a href = "/admin/startpage">
                Landing Page
            </a>
        </li>

        <li>
            <a href = "/admin/meta">
                Meta Description
            </a>
        </li>
        -->
        <li>
            <a href = "/admin/password">
                Password
            </a>
        </li>
        <li>
            <a href = "/logout">
                LOGOUT
            </a>
        </li>

    </ul>
</div>
<br>
<div class = "container left">
        %include
</div>
<div class = "container left">
    <p class = "text-info">
        Kind Sir, if you encounter problems, need support, have questions 
        or want to recommend me, feel free to visit 
        <a href="http://fullcab.in">my website</a>.
    </p>
</div>
<script>
    $(document).ready( function () {
        $(".dropdown-toggle").dropdown();
    });
    $(function() {
        $("#sortable").sortable();
        $("#sortable").disableSelection();
    });
    $("#sortVideos").click( function() {
        json = JSON.stringify($('#sortable').sortable('toArray'));
        $.get("/admin/video/sort/"+json, json);
    });
    $("#sortPictures").click( function() {
        json = JSON.stringify($('#sortable').sortable('toArray'));
        $.get("/admin/picture/sort/"+json, json);
    });
    $("#sortTexts").click( function() {
        json = JSON.stringify($('#sortable').sortable('toArray'));
        $.get("/admin/text/sort/"+json, json);
    });
    $("#sortCategories").click( function() {
        json = JSON.stringify($('#sortable').sortable('toArray'));
        $.get("/admin/category/sort/"+json, json);
    });
    $("#sortLinks").click( function() {
        json = JSON.stringify($('#sortable').sortable('toArray'));
        $.get("/admin/link/sort/"+json, json);
    });
    $('.menu-uncheck-btn').click( function() {
        $('input:radio').attr('checked', false);
    });
    tinyMCE.init({
        selector: "textarea.wysiwyg",
        width: "100%",
        theme : "advanced",
        mode : "textareas",
        plugins : "table",
        theme_advanced_buttons3_add : "tablecontrols",
        table_styles : "Header 1=header1;Header 2=header2;Header 3=header3",
        table_cell_styles : "Header 1=header1;Header 2=header2;Header 3=header3;Table Cell=tableCel1",
        table_row_styles : "Header 1=header1;Header 2=header2;Header 3=header3;Table Row=tableRow1",
        table_cell_limit : 100,
        table_row_limit : 5,
        table_col_limit : 5
    });
</script>
