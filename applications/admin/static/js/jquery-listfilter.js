// Case-insensitive contains selector
//jQuery.expr[':'].icontains = function (obj, index, meta, stack) {
//    return (obj.TextContents || obj.InnerText || "").toUpperCase().indexOf(meta[3].toUpperCase()) >= 0;
//}

$.expr[':'].icontains = function(obj, index, meta, stack){
return (obj.textContent || obj.innerText || jQuery(obj).text() || '').toLowerCase().indexOf(meta[3].toLowerCase()) >= 0;
};

// .listFilter(textbox_id, [i], [p])
//
// * textbox_id : selector that will be used to retrieve the filter value
// * i          : element inside the container that will contain the text to
//                filter
// * p          : parent element to collapse
//
( function ( $ ) {

    $.fn.listFilter = function(textbox_id, i, p) {
        var list = this;

        $(textbox_id).change(function () {
            var filter = $(this).val();
            if (filter) {
                $(list).find((i || 'strong') + ':not(:icontains(' + filter + '))').parents(p || 'li').slideUp();
                $(list).find((i || 'strong') + ':icontains(' + filter + ')').parents(p || 'li').slideDown();
            } else {
                $(list).find('li').slideDown();
            }
        }).keyup(function () {
            $(this).change();
        });
    }

})( jQuery );
