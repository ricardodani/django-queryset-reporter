/*
 * reporter.js
 *
 * Author: Ricardo Dani
 * E-mail: ricardodani@gmail.com
 * */

$(document).ready(function() {
    $('#querysets-form select[name=queryset]').change(function(event) {
        if ($(this).val() != '') {
            $('#querysets-form').submit();
        }
    });

    $('.datetime-field').datepicker({
        format: 'dd/mm/yyyy hh:ii',
    });
   
    $('.filter-checkbox').change(function() {
        var $check = $(this);
        var $parent = $check.parent();
        var $input_filters = $parent.find('.inputs');
        if ($check.attr('checked') == 'checked') {
            $input_filters.show('fast');
            $input_filters.find('.filter-field').removeAttr('disabled');
            $parent.addClass('filter-selected');
        } else {
            $input_filters.hide('fast');
            $input_filters.find('.filter-field').attr('disabled', 'disabled');
            $parent.removeClass('filter-selected');
        }
    }).change();

});

