/*
 * queryset_reporter.js
 *
 * Author: Ricardo Dani
 * E-mail: ricardodani@gmail.com
 * Github: github.com/ricardodani
 * Twitter: @ricardodani
 * */

(function($) {
    $(document).ready(function() {
        $('#queryset_form #id_model').change(function(event) {
            var model = $(this);
            if (model.val().length > 0) {
                $.getJSON('/admin/')
            }
        }).change();
    })
}(django.jQuery));
