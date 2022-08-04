$(document).ready(function () {

    var ShowForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#modalJS').modal('show');
            },
            success: function (data) {
                $('#modalJS .modal-content').html(data.html_form);
            }
        });
    };

    var SaveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#scr-vtr-dynamic-print tbody').html(data.table_list);
                     $('#scr-vtr-dynamic tbody').html(data.table_list);

                    $('#modalJS').modal('hide');
                } else {
                    $('#modalJS .modal-content').html(data.html_form)
                }
            }
        });
        return false;
    };


// create 
    $(".show-form").click(ShowForm);
    $("#modalJS").on("submit", ".create-form", SaveForm);

//update
    $('#book-table').on("click", ".show-form-update", ShowForm);
    $('#scr-vtr-dynamic').on("click", ".show-form-update", ShowForm);
    $('#scr-vtr-dynamic-print').on("click", ".show-form-update", ShowForm);
    $('#modalJS').on("submit", ".update-form", SaveForm);

//delete
    $('#book-table').on("click", ".show-form-delete", ShowForm);
    $('#scr-vtr-dynamic-print').on("click", ".show-form-delete", ShowForm);
    $('#modalJS').on("submit", ".delete-form", SaveForm);
    $('#card-remove').on("click", ".show-form-delete", ShowForm);


});