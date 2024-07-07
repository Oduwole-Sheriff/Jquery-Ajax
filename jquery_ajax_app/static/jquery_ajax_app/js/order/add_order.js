import {getAllOrders} from '../main.js'


$(document).ready(function(){

    function fetchOrderFromBackend(){
        getAllOrders();
    }
    
    
    $('#addOrderBtn').click(function(){
        $('#addOrderModal').modal('show');
    });

    function getAuthToken() {
        return localStorage.getItem('token');
    }

    $('#add_order_form').submit(function(e){
        e.preventDefault();
        var formData = new FormData(this);

        const token = getAuthToken();
        console.log('Token:', token);
    
        Swal.fire({
            icon: 'success',
            title: 'Success',
            text: 'Order Has Been Added Successfully?',
            confirmButtonText: 'Okay',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: 'POST',
                    url: '/api/post/',
                    data: formData,
                    headers: {
                        'Authorization': `Token ${getAuthToken()}` // Assuming Bearer token authentication
                    },
                    contentType: false,
                    processData: false,
                    beforeSend: function() {
                        // Show preloader if needed
                    },
                    success: function(data) {
                        $('#add_order_form').trigger('reset'); // Reset the form
                        $('#addOrderModal').modal('hide');
    
                        // Add code to populate the order list immediately
                        addNewPost(data); // Assuming this function adds a new post
    
                        // Reload the page
                        location.reload();
                    },
                    error: function(xhr, status, error) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Error',
                            text: 'A post with that name already exists',
                        });
                    }
                });
            }
        });
    });

    
    // Function to add a new post dynamically
    function addNewPost(postData) {
        // Example: Assuming posts are rendered in a certain format
        var newPost = `
            <div class="search-nav">
                <div class="post">
                    <img src="${postData.image}" alt="post">
                    <div class="post-text">
                        <h4> <a href="#"> ${postData.name} - Ordered (${postData.drink}) </a></h4>
                        <p class="text-muted">${postData.date_posted}</p>
                    </div>
                </div>
                <div class="post-btn">
                    <a href="#" data-id='${postData.id}' class="remove"> Delete </a>
                </div>
            </div>
        `;
        
        $('.only-post').prepend(newPost); // Assuming posts are within .main-background
    }
});