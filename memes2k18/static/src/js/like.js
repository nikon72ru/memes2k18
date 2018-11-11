$(document).ready(function() {
    $(".like").click(function(e){
    console.log(123);
            var cluster_id = $(this).parent().parent().parent().parent().data('source')

        if ($(this).hasClass("far")) {
            $(this).removeClass("far");
            $(this).addClass("fas");
            var val = sessionStorage.getItem('cluster_'+cluster_id);
            sessionStorage.setItem('cluster_'+cluster_id, parseInt(val)+1);
            return
        } else if($(this).hasClass("fas")) {
            $(this).removeClass("fas");
            $(this).addClass("far");
            var val = sessionStorage.getItem('cluster_'+cluster_id);
            sessionStorage.setItem('cluster_'+cluster_id, parseInt(val)-1);
        }
    });
    console.log(12423523);
    $("#relevant").click(function(e){
    console.log(312);
        var clusters = {};
        Object.keys(sessionStorage).forEach(function (obj) {
           if (obj.indexOf('cluster') != -1){
               clusters[obj] = parseInt(sessionStorage.getItem(obj));
           }
        });
        console.log(clusters);



        var sortable=[];
        var obj = clusters;
	for(var key in obj)
		if(obj.hasOwnProperty(key) && key.indexOf('cluster') != -1)
			sortable.push([key, obj[key]]); // each item is an array in format [key, value]

	// sort items by value
	sortable.sort(function(a, b)
	{
	  return a[1]-b[1]; // compare numbers
	});
//	console.log(sortable);
     window.location.href = "relevant?filter=" + sortable[sortable.length-1][0].replace('cluster_', '');
    });

});

