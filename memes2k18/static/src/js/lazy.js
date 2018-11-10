$(document).ready(function() {

    var load = $('#lazyLoadLink')
    load.onclick = function() {
    $.ajax({
      type: 'post',
      url: 'get_more',
      data: {
        'type': window.location.pathname,
        'filter': 'FGHJ',
        'offset': 5
      },
      success: function(data) {
        window.location.pathname
      },
      error: function(xhr, status, error) {
        // shit happens friends!
      }
    });
  };

});