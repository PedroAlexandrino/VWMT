(function($) {
    'use strict';
    $(function() {
    $('.file-upload-browse').on('click', function() {
        var file = $(this).parent().parent().parent().find('.file-upload-default');
        file.trigger('click');
      });
      $('.file-upload-default').on('change', function() {
        $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
      });
    });
    $(document).ready(function() {
        var listDelete = $('.list-delete');
        listDelete.on('click', function() {
            swal({
                title: "Delete item?",
                text: "Do you really want to delete this item?",
                icon: "error",
                buttons: ["Cancel", "Delete Now"],
                dangerMode: true,
            })
            .then((willDelete) => {
                if (willDelete) {
                    swal({
                        title: "Deleted",
                        text: "The list item has been deleted!",
                        icon: "success",
                    });
                } else {
                    swal("The item is not deleted!");
                }
            });
        });
        $('.html-editor').summernote({
          height: 300,
          tabsize: 2
        });
    })

    $(document).ready(function() {
        var listConfirm = $('.list-confirm');
        listConfirm.on('click', function() {
            swal({
                title: "Confirm Changes?",
                text: "Are you sure you want to save changes?",
                icon: "warning",
                buttons: ["Cancel", "Confirm"],
                dangerMode: false,
            })
            .then((willDelete) => {
                if (willDelete) {
                    swal({
                        title: "Added",
                        text: "Your changes have been saved!",
                        icon: "success",
                    });
                } else {
                    swal("The item is not added!");
                }
            });
        });
        $('.html-editor').summernote({
          height: 300,
          tabsize: 2
        });
    })


    $(document).on("click", ".editSchedule", function () {
        //$(".modal-body #date_to_prod").val( $(this).data('date_to_prod') );
        $(".modal-body #date_to_prod").val($(this).data('date_to_prod'))
        $(".modal-body #order").val($(this).data('order'));

        $(".modal-header #partNumber").text($(this).data('part_number'));
        $(".modal-header #scheduleId").val($(this).data('id'));
        console.log($(this).data('id'));


    });

    $(document).on("click", ".deleteSchedule", function () {

        //$(".modal-body #date_to_prod").val( $(this).data('date_to_prod') );
        $(".modal-body #date_to_prod").val($(this).data('date_to_prod'))
        $(".modal-body #order").val($(this).data('order'));

        $(".modal-header #partNumber").text($(this).data('part_number'));
        $(".modal-header #scheduleId").val($(this).data('id'));
        console.log($(this).data('id'));


    });

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



    $(document).on('submit', '#schedulePost-form',function(e){
       var csrftoken = getCookie('csrftoken');

    $.ajax({
        type:'POST',
        headers: {'X-CSRFToken': csrftoken},
        data:{
            scheduling_id: $('.modal-header #scheduleId').val(),
            linha : $('.modal-body #linha').val(),
            date_to_prod :$('.modal-body #date_to_prod').val(),
            order: $('.modal-body #order').val(),
            action : "update",

            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

        },

        dataType: "json",
        success:function(json){
           console.log("SUCCESS"+json.status)

        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});


    $(document).on('submit', '#schedulePostDelete-form',function(e){
       var csrftoken = getCookie('csrftoken');

    $.ajax({
        type:'POST',
        headers: {'X-CSRFToken': csrftoken},
        dataType: "json",
        data:{
            scheduling_id: $('.modal-header #scheduleId').val(),
            scheduling_state : 0,
            action : "delete",

            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

        },

        success:function(json){
           console.log("SUCCESS"+json.status)

        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});

     $(document).on('submit', '#schedulePostConfirm-form',function(e){
       var csrftoken = getCookie('csrftoken');
    $.ajax({
        type:'POST',
        headers: {'X-CSRFToken': csrftoken},
        dataType: "json",
        data:{
            scheduling_id: $('.modal-header #scheduleId').val(),
            action : "confirm",

            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

        },

        success:function(json){
           console.log("SUCCESS"+json.status)

        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});


})(jQuery);