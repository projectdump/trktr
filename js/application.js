function simulate(element, eventName)
{
    var options = extend(defaultOptions, arguments[2] || {});
    var oEvent, eventType = null;

    for (var name in eventMatchers)
    {
        if (eventMatchers[name].test(eventName)) { eventType = name; break; }
    }

    if (!eventType)
        throw new SyntaxError('Only HTMLEvents and MouseEvents interfaces are supported');

    if (document.createEvent)
    {
        oEvent = document.createEvent(eventType);
        if (eventType == 'HTMLEvents')
        {
            oEvent.initEvent(eventName, options.bubbles, options.cancelable);
        }
        else
        {
            oEvent.initMouseEvent(eventName, options.bubbles, options.cancelable, document.defaultView,
            options.button, options.pointerX, options.pointerY, options.pointerX, options.pointerY,
            options.ctrlKey, options.altKey, options.shiftKey, options.metaKey, options.button, element);
        }
        element.dispatchEvent(oEvent);
    }
    else
    {
        options.clientX = options.pointerX;
        options.clientY = options.pointerY;
        var evt = document.createEventObject();
        oEvent = extend(evt, options);
        element.fireEvent('on' + eventName, oEvent);
    }
    return element;
}

function extend(destination, source) {
    for (var property in source)
      destination[property] = source[property];
    return destination;
}

var eventMatchers = {
    'HTMLEvents': /^(?:load|unload|abort|error|select|change|submit|reset|focus|blur|resize|scroll)$/,
    'MouseEvents': /^(?:click|dblclick|mouse(?:down|up|over|move|out))$/
}
var defaultOptions = {
    pointerX: 0,
    pointerY: 0,
    button: 0,
    ctrlKey: false,
    altKey: false,
    shiftKey: false,
    metaKey: false,
    bubbles: true,
    cancelable: true
}

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
    $(this).parent().css('margin-bottom', "100px");
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
    $('body').animate({
        scrollTop: $(this).parent().offset().top - 40
    })
    //alert($(this).parent().attr('class'));
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
    $('.header').css('height', $(window).height() - $('.nav').height());
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
$(window).load(function() {
    /*
    if(document.location['pathname'] != "/") {
        document.body.scrollTop = $(".header").height();
    }
    else {
    }
    */
    if(document.location['pathname'] != "/") {
        $('body').animate( {
            scrollTop: $(".header").height()
        });
    }
    else {
    }
});

Shadowbox.init();
                

