$(document).ready(function(){

      $('.update').click(function(e) {
        e.preventDefault();

        var postName = $('#modalName').text().trim();
        var postDrink = $('#modalDrink').text().trim();

        $('#updateName').val(postName);
        $('#updateDrink').val(postDrink);

        var modal = new bootstrap.Modal(document.getElementById('updateOrderModal'));
        modal.show();
    });

    $('#update_order_form').submit(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        var name = $('#updateName').val().trim();
        var drink = $('#updateDrink').val().trim();

        if (!name || !drink) {
            console.log('Name and Drink fields are required.');
            return;
        }

        formData.set('name', name);
        formData.set('drink', drink);

        $.ajax({
            type: 'POST',
            url: '/api/post/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {

                $('#updateOrderModal').modal('hide'); 

                $('#modalName').text(name); 
                $('#modalDrink').text(drink); 

                $('#modalName').text(name);
                $('#modalDrink').text(drink); 
            },
            error: function(xhr, status, error) {
                var responseJSON = xhr.responseJSON;
                if (responseJSON && responseJSON.errors) {
                    console.log('Validation Errors:', responseJSON.errors);
                } else {
                    console.log('Error:', error);
                }
            }
        });
    });

});