<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- WHATEVER A SHORTCUT ICON IS
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">
    -->
    <title>Traktor</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet">
    <link href="/js/shadowbox/shadowbox.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="//f.fontdeck.com/s/css/uH5+KWQnibDTJRYggGJ9XZLTAgw/DOMAIN_NAME/40726.css" type="text/css" />
    <script type="text/javascript">
        WebFontConfig = { fontdeck: { id: '40726' } };

        (function() {
            var wf = document.createElement('script');
            wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
            '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
            wf.type = 'text/javascript';
            wf.async = 'true';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(wf, s);
        })();
    </script>
    <link href="/css/traktor.css" rel="stylesheet">
  </head>
  <body>

  %include

    <script src="/js/jquery-2.0.3.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/holder.js"></script>
    <script src="/js/shadowbox/shadowbox.js"></script>
    <script src="/js/application.js"></script>
    <script>

$('#navigate').click( function(e) {
    targetId = $(this).attr('href');
    currentId = "";
    closeId = "";
    var i = 0
    var tmp = $(this).parent()
    while(true) {
        var str = tmp.find('.x').attr('id');
        console.log(str);
        if(str != undefined) {
            if(str.indexOf('close') >= 0) {
                closeId = str;
                navigate(closeId, targetId);
                break;
            }
        }
        if(i > 10) {
            break;
        }
        tmp = tmp.parent();
        i = i + 1;
    }
    return false; 
});
function navigate(current, target) {
    simulate(document.getElementById(closeId), 'click');
    setTimeout(function() {
        simulate(document.getElementById(targetId.replace('#', "")), 'click')
    }, 1000);
    return false;
}

    </script>


 
  </body>

</html>
