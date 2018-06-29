var formAjaxSubmit = function(form, modal) {
  $(form).submit(function (e) {
         e.preventDefault();
         $.ajax({
             type: $(this).attr('method'),
             url: $(this).attr('action'),
             data: $(this).serialize(),
             success: function (xhr, ajaxOptions, thrownError) {
                 if ( $(xhr).find('.has-error').length > 0 ) {
                     $(modal).find('.modal-body').html(xhr);
                     formAjaxSubmit(form, modal);
                 } else {
                     $(modal).modal('toggle');
                 }
             },
             error: function (xhr, ajaxOptions, thrownError) {
                 // handle response errors here
             }
         });
  });
}
$('#comment-button').click(function() {
  /*$('.modal-body').load('/create/', function () {
    $('#form-modal').modal('toggle');
      formAjaxSubmit('#form-modal-body form', '#form-modal');
  });*/
  $.ajax({
    url: 'create/',
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#form-modal").modal("show");
    },
    success: function (data) {
      $("#form-modal-body .modal-content").html(data.html_form);
    }
  });
});

/*
$(function () {

  $(".js-create").click(function () {
    $.ajax({
      url: 'create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-form").modal("show");
      },
      success: function (data) {
        $("#modal-form .modal-content").html(data.html_form);
      }
    });
  });

});
$("#modal-form").on("submit", ".js-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("Book created!");  // <-- This is just a placeholder for now for testing
        }
        else {
          $("#modal-form .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
  $("#modal-form").on("submit", ".js-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);  // <-- Replace the table body
          $("#modal-form").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-form .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
*/
