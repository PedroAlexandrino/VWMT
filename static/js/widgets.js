$(function () {
    'use strict';



});

$(document).ready(function () {

    $('#datepickerwidget').datetimepicker({
        inline: true,
        format: 'yyyy-mm-dd',
        onSelect: function (dateText, inst) {
            alert("Working");
        }
    });

    $('#datepickerReposicao').datetimepicker({
        inline: true,
        formatDate: 'yyyy-mm-dd',
        onSelect: function (dateText, inst) {
            alert("Working");
        }
    });





});