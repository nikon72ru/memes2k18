$(document).ready(function() {
    var first_lazy = true;
    var load = $('#lazyLoadLink');
    $("#lazyLoadLink").click(function(e){
        console.log($('.post'));
    $.ajax({
      type: 'post',
      url: 'get_more',
      data: {
        'type': window.location.pathname,
        'filter': findGetParameter('filter'),
        'offset': $('.post').length
      },
      success: function(data) {
           $(".posts").append(data);
      },
      error: function(xhr, status, error) {
        // shit happens friends!
      }
    });
  });

});

function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}