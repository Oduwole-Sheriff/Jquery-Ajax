$(document).ready(function(){
    var $search_nav = $('.search-nav');
    
    function getAuthToken() {
        return localStorage.getItem('token');
    }

    $search_nav.on('click', '.remove', function(e){
        e.preventDefault();

        const token = getAuthToken();

        // Check if token is null or empty
        if (!token) {
            console.log('Token not available');
            return; // or handle appropriately
        }
            
        var dataId = $(this).attr('data-id');
        var $searchNavToRemove = $(this).closest('.search-nav');
    
        Swal.fire({
            title: "Are you sure?",
            text: "You won't be able to revert this!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes, delete it!"
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: 'DELETE',
                    url: '/api/post/',
                    data: { id: dataId },
                    headers: {
                        'Authorization': `Token ${getAuthToken()}` // Assuming Bearer token authentication
                    },
                    success: function(){
                        $searchNavToRemove.fadeOut(300, function(){
                            $(this).remove();
                            Swal.fire(
                                'Deleted!',
                                'Your file has been deleted.',
                                'success'
                            );
                        });
                    },
                    error: function() {
                        console.error('Error deleting post');
                    }
                });
            }
        });
    });

    
});

