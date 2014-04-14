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
    if(!$(this).hasClass("active")) {
        $(this).css("z-index", "100");
    }
}, function () {
    if(!$(this).hasClass("active")) {
        $(this).css("z-index", "0");
    }
});
$(".blacklayer").hover( function () {
}, function () {
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
    $(".active .x").click();
    var padding = $(this).parent().find(".boxcontent").css(".margin-bottom");
    var x = $(this).parent().find(".x");
    var entry = $(this).parent();
    var cover = $(this).parent().find('.cover');
    var boxcontent = $(this).parent().find('.boxcontent');
    var margin = parseInt(entry.css('margin-bottom'))*-1;
    var blacklayer = $(this).find(".blacklayer");
    entry.addClass("active");
    entry.css("overflow","visible");
    x.css("display","block");
    x.css("opacity","1");
    cover.hide();
    boxcontent.show();
    boxcontent.css("opacity", 1);
    boxcontent.css('padding-bottom', margin);
    if(entry.hasClass("center")) {
        entry.css("float", "left");                
        entry.css("left", "0");                
        entry.css("margin-left", "0px");                
        entry.css("margin-right", "0px");
    }

    blacklayer.hide();
    entry.css("max-width", "100%");
    entry.css("width", "100%");
    $('body').animate({
        scrollTop: entry[0].offsetTop - 50
    }, 500, function(e) {
        entry.css("max-height", entry.find(".boxcontent").innerHeight());
        entry.css("height", entry.find(".boxcontent").innerHeight());
        return false;
    });
    return false;
});

$(".x").click( function (e) {
    var blacklayer = $(this).parent().parent().find(".blacklayer");
    var under = $(this).parent().parent().find(".under"); 
    var entry = $(this).parent().parent();
    entry.css('overflow', "hidden");
    var cover= $(this).parent().parent().find("cover");
    var margin = parseInt($(this).parent().parent().find(".boxcontent").css("padding-bottom"));
    entry.css('margin-bottom', entry.find("under").css("margin-bottom"));
    
    $(this).parent().css("opacity", "0");
    $(this).hide();
    $(this).css("opacity", "0");

    if(under.css("margin-bottom") > 0 ) {
        margin = -under.css("margin-bottom");
    } else {
        margin=0;
    }

    blacklayer.css("width", under.width());
    blacklayer.css("height", under.height());

    $(this).parent().parent().css("max-width", under.width());
    $(this).parent().parent().css("max-height", under.height());

    entry.css("width", under.width()+margin);
    entry.css("height", under.height()+margin);
    cover.show()
    $(this).parent().parent().find(".cover").show();
    cover.css('height', under.height())+margin;
    cover.css('width', under.width())+margin;
    cover.css("opacity", 1);
    if($(this).parent().parent().hasClass("center")) {
        entry.css("float", "");
        entry.css("left", "");
        entry.css("margin-left", "auto");
        entry.css("margin-right", "auto");
        
    }
    blacklayer.show();
    entry.removeClass("active");
    entry.css("overflow", "hidden");

    return false;
});

function updateUnderDivs() {
        $(".under").each( function(x) {
            var blacklayer = $(this).parent().find(".blacklayer");
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
});
$(window).load(function() {
    if(document.location['pathname'] != "/") {
        document.body.scrollTop = $(".header").height();
    }
    else {
    }
    $("#loading").hide();
    $("html, body").css({
        "overflow-y": "visible",
        "height": "auto"
    });
});

$(window).resize( function() {
    updateUnderDivs();
    return false;
});

Shadowbox.init();
