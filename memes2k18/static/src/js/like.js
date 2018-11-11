$(document).ready(function() {
    $(".like").click(function(e){
    console.log(123);
            var cluster_id = $(this).parent().parent().parent().parent().data('source')

        if ($(this).hasClass("far")) {
            $(this).removeClass("far");
            $(this).addClass("fas");
            var val = sessionStorage.getItem('cluster_'+cluster_id);
            sessionStorage.setItem('cluster_'+cluster_id, val+1);
            return
        } else if($(this).hasClass("fas")) {
            $(this).removeClass("fas");
            $(this).addClass("far");
            var val = sessionStorage.getItem('cluster_'+cluster_id);
            sessionStorage.setItem('cluster_'+cluster_id, val-1);
        }
    })
});

