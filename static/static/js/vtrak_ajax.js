function getStuff(elem) {
  const id = $(elem).attr('id');
  
  $.ajax({
    url:            window.location.pathname + id,
    type:           'GET',
    contentType:    'application/json; charset=utf-8',
    dataType:       'json',
    success:        function (result) {
      $('#something').prepend(
        "<p>" + result.item + "</p>"
      );
    }
  });
}

function postStuff(elem) {
  const id = $(elem).attr('id');
  const csrftoken = window.CSRF_TOKEN;

  $.ajax({
    url:            window.location.pathname + id,
    type:           'POST',
    beforeSend:     function (request) {
      request.setRequestHeader("X-CSRFToken", csrftoken);
    },
    data:           {
      csrfmiddlewaretoken: csrftoken
    },
    contentType:    'application/json; charset=utf-8',
    dataType:       'json',
    success:        function (result) {
      $('#something').prepend(
        "<p>" + result.item + "</p>"
      );
    }
  });
}