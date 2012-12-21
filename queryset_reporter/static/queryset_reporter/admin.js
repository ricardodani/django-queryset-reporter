/*
 * admin.js
 *
 * Author: Ricardo Dani
 * E-mail: ricardodani@gmail.com
 * Github: github.com/ricardodani
 * Twitter: @ricardodani
 * */

(function($) {
// django jquery namespace

function option(val, verbose, type, selected) {
    /*
     * Return a <option> with value, verbose and selected bool.
     * */
    var selected = selected || false;
    var $opt = $('<option>');
    $opt.val(val);
    $opt.text(verbose);
    if (selected == true) {
        $opt.attr('selected', 'selected');
    }
    if (type != null) {
        $opt.attr('data-type', type)
    }
    // returns a <option> jQuery object with the give `val` and `verbose`.
    return $opt;
}

function populate_clean($inline_item) {
    var model_field = $inline_item.find('.introspect-model_field');
    $(model_field).empty(); 
    model_field.append(option('', '-------', null));
}

function populate_model_data($inline_item) {
    /*
     * populate_model_data($inline_item)
     * with a given $inline_item (jQuery object of a inline item)
     * populate the <select> `model_field` with the metadata located in
     * windows.queryset_reporter.model_data
     * */
    var model_field = $inline_item.find('.introspect-model_field');
    var data = window.queryset_reporter.model_data;
    console.log(data);
    if (data.success) {
        $.each(data.fields, function (i, field) {
            model_field.append(option(field.name, field.verbose, field.type));
            if (typeof field.lookup_fields != 'undefined') {
                $.each(field.lookup_fields, function (j, lfield) {
                    //model_field.append(option(field.name, field.verbose));
                    var lf_name = field.name + '__'  + lfield.name;
                    var lf_verbose = field.verbose + ' -> ' + lfield.verbose;
                    model_field.append(option(lf_name, lf_verbose, lfield.type));
                });
            }
        });
    }
}

function populate_model_defaults($inline_item) {

    // hidden with field name
    var field = $inline_item.find('.introspect-field');
    // hidden with verbose
    var verbose = $inline_item.find('.introspect-field_verbose');
    // select
    var model_field = $inline_item.find('.introspect-model_field');

    // if the hidden field `field` has data
    if (field.val().length > 0) {
        if (verbose.val().length == 0) {
            verbose = field;
        }
        var $opt = model_field.children('option[value=' + field.val() + ']');
        if ($opt.length > 0) {
            $opt.attr('selected', 'selected');
        }
    }
}

function model_field_populate_by_inline(index, value) {
    /*
     * model_field_default_by_inline()
     * for each form in the inline formset, makes the default values
     * for the model_field <select>, selecting what are equal to the hidden
     * `field`.
     */
    var inline_itens = $('#'+value+'_set-group div[id^='+value+'_set]');

    // iterate through each form
    inline_itens.each(function(index, inline_item) {
        populate_clean($(inline_item));
        populate_model_data($(inline_item));
        populate_model_defaults($(inline_item));
    });
}

function model_field_populate() {
    /*
     * model_field_populate()
     * with an array of inline`s names, for each of them, execute the 
     * function `model_field_defaults_by_inline`, responsable for 
     * */
    var inlines = $(['displayfield', 'filter', 'exclude']);
    inlines.each(model_field_populate_by_inline);
}

$(document).ready(function() {
   
    /*
     * for every change in the Model <select> execute the funcion to
     * retrieve a JSON via ajax to get the field metadata of the selected
     * model.
     * */
    $('#queryset_form #id_model').change(function(event) {
        var model = $(this);
        if (model.val().length > 0) {
            var url = '/queryset_reporter/ajax/model-fields/';
            $.getJSON(url, {model: model.val()}, function(data) {
                // first, sets the model_data in a global object
                window.queryset_reporter = {model_data: data}
                // then call a method to populate 
                model_field_populate();
            });
        }
    }).change();

    /*
     * For every change in the `model_field` of the inlines.
     * Copies the <select> information to `field`, `field_verbose` and `field_type`.
     * */
    $('#queryset_form .introspect-model_field').change(function(event) {
        var $model_field = $(this);
        var $option = $model_field.find('option:selected');
        var $div_parent = $model_field.parent().parent();
        var $name = $div_parent.find('.introspect-field');
        var $verb = $div_parent.find('.introspect-field_verbose');
        var $type = $div_parent.find('.introspect-field_type');
        $verb.val($option.text());
        $name.val($option.val());
        $type.val($option.attr('data-type'));
    });
});

}(django.jQuery));
