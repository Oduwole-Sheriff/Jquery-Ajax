$(document).ready(function(){
    $('#addOrderBtn').click(function(){
        $('#addOrderModal').modal('show');
    });

    $('#add_order_form').submit(function(e){
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type: 'POST',
            url: '/api/post/',
            data: formData,
            contentType: false,
            processData: false,
            beforeSend: function() {
                // Show preloader if needed
            },
            success: function(data) {
                $('#add_order_form').trigger('reset'); // Reset the form

                // Close the modal
                $('#addOrderModal').modal('hide');
                
                alert('Order added successfully!');

                // Add code to populate the order list immediately
                addNewPost(data); // Assuming this function adds a new post

                // Reload the page
                location.reload();

            },
            error: function(xhr, status, error) {
                alert('A post with that name already exist');
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