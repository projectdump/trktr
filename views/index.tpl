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
    <script>
        $(".entry").hover( function () {
            $(this).css("z-index", "100");
        }, function () {
            $(this).css("z-index", "0");
        });
        $(".up").click( function() {
            $("html, body").animate({scrollTop: $(".header").height()});
        });
        $(".navbar-wrapper").affix({
            offset: {
                top: function() {
                    return $(".header").height();
                }
            }
        });
        $(".box").click( function (e) {
            $(this).parent().find(".cover").animate({
                "opacity": 0}, 250, function(e) {
                    $(this).parent().find('.boxcontent').show();
                    $(this).parent().find('.cover').hide();
                    return false;
                });
            var margin = parseInt($(this).parent().css('margin-bottom'))*-1
            $(this).parent().find('.boxcontent').css('padding-bottom', margin);
            $(this).parent().css('margin-bottom', "0px");
            //$(this).find(".blacklayer").css("background-color", "white");
            //$(this).find(".blacklayer").css("opacity", "1");
            if($(this).parent().hasClass("center")) {
                $(this).parent().css("right", "auto");                
                $(this).parent().css("float", "left");                
                $(this).parent().animate({
                    "left": "0px",
                    "margin-left": "0px" 
                });
            }
            $(this).find(".blacklayer").hide();
            $(this).parent().css("max-width", "100%");
            $(this).parent().css("max-height", $(this).parent().find(".boxcontent").height());
            $(this).parent().animate({
                "width": "100%",
                "height": $(this).parent().find(".boxcontent").height()
                });
            return false;
        });
        $(".x").click( function (e) {
            var blacklayer = $(this).parent().parent().find(".blacklayer")
            var margin = parseInt($(this).parent().parent().find(".boxcontent").css("padding-bottom"));
            //$(this).parent().parent().find(".boxcontent").css("padding-bottom"));
            $(this).parent().parent().css('margin-bottom', margin*-1);
            $(this).parent().animate({
                "opacity": 0
            }, 250, function(e) {
                $(this).hide();
                $(this).css("opacity", "1");
            });
            //alert($(this).parent().parent().attr("class"));
            $(this).parent().parent().css("max-width", "auto");
            $(this).parent().parent().css("max-height", "auto");
            //alert($(this).parent().parent().find(".under").width());
            $(this).parent().parent().animate({
                "width" : $(this).parent().parent().find(".under").width(),
                "height": $(this).parent().parent().find(".under").height()
            }, 500, function() {
                blacklayer.show();
            });
            $(this).parent().parent().find(".cover").show();
            //$(this).parent().parent().find(".blacklayer").show();
            $(this).parent().parent().find(".cover").animate({
                "opacity": "1"
            },250);
            if($(this).parent().parent().hasClass("center")) {
                $(this).parent().parent().css("right", "50%");                
                $(this).parent().parent().css("float", "none");                
                $(this).parent().parent().animate({
                    "left": "50%",
                    "margin-left": "-300px" 
                });
            }

            //alert($(this).parent().parent().css("display"));
            return false;
        });

        function updateUnderDivs() {
                $(".under").each( function(x) {
                    //alert($(this).parent().find(".cover").css("height"));
                    var blacklayer = $(this).parent().find(".blacklayer");
                    //alert(blacklayer.css("height"));
                    blacklayer.css("height", $(this).parent().find(".cover").css("height"));
                    $(this).css("width", $(this).parent().css("max-width"));
                    $(this).css("height", $(this).parent().find(".cover").css("height"));
                    $(this).css("display", "none");
                });
        }

        $(document).ready(function () {
            var readyStateCheckInterval = setInterval(function() {
                if(document.readyState === "complete") {
                    updateUnderDivs()
                    clearInterval(readyStateCheckInterval)
                }
            },
            10
            );
        }
            /*function() {
                $(".under").each( function(x) {
                    alert($(this).parent().find(".cover").css("height"));
                    $(this).css("width", $(this).parent().css("max-width"));
                    $(this).css("height", $(this).parent().find(".cover").css("height"));
                    $(this).css("display", "none");
                });
            }*/
        );

                

    </script>


 
  </body>

</html>
