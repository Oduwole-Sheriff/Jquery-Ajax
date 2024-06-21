// $(document).ready(function(){

//     var $search_nav = $('.search-nav')

//     $search_nav.on('click', '.remove', function(){
//         var dataId = $(this).attr('data-id');
//         var $search_nav = $(this).closest('.search-nav');

//         const confirmDelete = confirm('Are you sure you want to delete this item?')

//         if(confirmDelete === true){
//             $.ajax({
//                 type: 'DELETE',
//                 url: '/api/post/',
//                 data: { id: dataId },
//                 success: function(){
//                     $search_nav.fadeOut(300, function(){
//                         $(this).remove();
//                         console.log('Data deleted successfully');
//                     });
//                 },
//                 error: function() {
//                     console.error('Error deleting data');
//                 },
//             });
//         }
//     })

// });

$(document).ready(function(){
    var $search_nav = $('.search-nav');

    $search_nav.on('click', '.remove', function(e){
        e.preventDefault();
        
        var dataId = $(this).attr('data-id');
        var $searchNavToRemove = $(this).closest('.search-nav');

        const confirmDelete = confirm('Are you sure you want to delete this item?');

        if (confirmDelete) {
            $.ajax({
                type: 'DELETE',
                url: '/api/post/',
                data: { id: dataId },
                success: function(){
                    $searchNavToRemove.fadeOut(300, function(){
                        $(this).remove();
                        console.log('Post deleted successfully');
                    });
                },
                error: function() {
                    console.error('Error deleting post');
                }
            });
        }
    });
});