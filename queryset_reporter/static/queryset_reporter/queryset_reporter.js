/*
 * queryset_reporter.js
 *
 * Author: Ricardo Dani
 * E-mail: ricardodani@gmail.com
 * Github: github.com/ricardodani
 * Twitter: @ricardodani
 * */

(function($) {
// django jquery namespace
$(document).ready(function() {
    $('#queryset_form #id_model').change(function(event) {
        var model = $(this);
        if (model.val().length > 0) {
            var url = '/queryset_reporter/ajax/model-fields/';
            $.getJSON(url, {model: model.val()}, function(data) {
                console.log(data);
            });
        }
    }).change();
})
}(django.jQuery));
