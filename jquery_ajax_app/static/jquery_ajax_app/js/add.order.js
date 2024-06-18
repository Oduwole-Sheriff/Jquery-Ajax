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
                // Show preloader
            },
            success: function(data) {
                // Handle success 

                $('#add_order_form').trigger('reset'); // Reset the form

                // close the modal
                $('#addOrderModal').modal('hide');
                
                alert('Order added successfully!');

                // add code to populate the orderlist

            },
            error: function(xhr, status, error) {
                // Handle error
                alert('Error adding order: ' + error);
            }
        });
    });
});
