function viewDetails(post_id){
    $.ajax({
        url: '/get-post-details/',
        type: 'GET',
        data: {
            'post_id': post_id
        },
        success: function(response) {
            $('#modalBody').html(response);
            $('#myModal').modal('show');
        },
        error: function(error) {
            console.log(error);
        }
    });
    
    // Update modal title with post_id
    $('#myModal').find('.modal-title').text('Post Details: #' + post_id);

    // Show the modal
    $('#myModal').modal('show');
}


$(document).ready(function(){
    // $.ajax({
    //     type: 'GET',
    //     url: '/api/post/',
    //     success: function(orders){
    //         $.each(orders, function(i, order){
    //             addOrder(order);
    //         });
    //     },
    //     error: function(xhr, status, error) {
    //         alert('Error loading orders');
    //     }
    // });
}); 

