$(document).ready(function() {

    var load = $('#lazyLoadLink')
    load.onclick = function() {
    $.ajax({
      type: 'post',
      url: 'get_more',
      data: {
        'type': 'same',
        'filter': 'FGHJ',
        'offset': 5
      },
      success: function(data) {
        // if there are still more pages to load,
        // add 1 to the "Load More Posts" link's page data attribute
        // else hide the link
        if (data.has_next) {
            link.data('page', page+1);
        } else {
          link.hide();
        }
        // append html to the posts div
        $('#div').append(data.posts_html);
      },
      error: function(xhr, status, error) {
        // shit happens friends!
      }
    });
  };

});