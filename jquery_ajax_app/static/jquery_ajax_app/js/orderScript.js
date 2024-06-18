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
    $('#addOrderBtn').click(function(){
        $('#addOrderModal').modal('show');
    });

    $('#add_order_form').submit(function(e){
        e.preventDefault();

        var formData = new FormData(this);
        var progressBar = $('.progress-bar');

        $.ajax({
            type: 'POST',
            url: '/api/post/',
            data: formData,
            contentType: false,
            processData: false,
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                // Upload progress event listener
                xhr.upload.addEventListener("progress", function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = Math.round((evt.loaded / evt.total) * 100);

                        console.log('Upload Progress:', percentComplete + '%');

                        // Update progress bar attributes and style
                        progressBar.attr('aria-valuenow', percentComplete);
                        progressBar.css('width', percentComplete + '%');
                        progressBar.text(percentComplete + '%');
                    }
                }, false);
                return xhr;
            },
            beforeSend: function() {
                // Show progress bar and initialize
                $('.progress').removeClass('d-none');
                progressBar.attr('aria-valuenow', '0');
                progressBar.css('width', '0%');
                progressBar.text('0%');
            },
            success: function(data) {
                // Handle success
                progressBar.text('Order added successfully!');
                setTimeout(function() {
                    $('.progress').addClass('d-none'); // Hide progress bar after a short delay
                    progressBar.attr('aria-valuenow', '0');
                    progressBar.css('width', '0%');
                    progressBar.text('0%'); // Reset progress text
                }, 1000);

                $('#add_order_form').trigger('reset'); // Reset the form

                // Optionally, update UI or perform other actions with 'data'
                // getAllOrders();

                // close the modal
                $('#addOrderModal').modal('hide');
            },
            error: function(xhr, status, error) {
                // Handle error
                $('.progress').addClass('d-none'); // Hide progress bar on error
                progressBar.text('Error adding order: ' + error);
            }
        });
    });
});



// var formData = {
        //     'field1': $('#field1').val(),
        //     'field2': $('#field2').val(),
        //     'image': $('#image')[0].files[0]
        // };