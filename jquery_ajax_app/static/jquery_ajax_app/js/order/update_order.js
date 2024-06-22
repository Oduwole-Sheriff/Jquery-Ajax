$(document).ready(function () {
    // Function to open modal and set initial values
    function openModal(name, drink, postId) {
        $('#modalName').text(name);
        $('#modalDrink').text(drink);
        $('#modalId').text(postId);
        
        var modal = new bootstrap.Modal(document.getElementById('showOrderModal'));
        modal.show();
        
        // Hide edit.name and edit.drink input fields initially
        $('.edit.name, .edit.drink').hide();
    }

    // Click event for clicking on a post
    $('.post-text h4 a').on('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        
        var postId = $(this).closest('.search-nav').data('id');
        var postName = $(this).text().split(' - ')[0].trim(); // Extract post name
        var postDrink = $(this).text().split(' - ')[1].trim(); // Extract post drink
        
        // Open modal and set initial values
        openModal(postName, postDrink, postId);

        $('.save-changes').hide();

    });
    
    // Function to update input fields with modal values and show them
    $('.update').on('click', function () {
        var nameValue = $('#modalName').text().trim();
        var drinkValue = $('#modalDrink').text().trim();
        
        $('.edit.name').val(nameValue);
        $('.edit.drink').val(drinkValue);
        
        // Show edit.name and edit.drink input fields
        $('.edit.name, .edit.drink').show();
        
        // Hide modalName and modalDrink spans
        $('#modalName, #modalDrink').hide();

        $('.save-changes').show();

        $('.update').hide();
    });
    
    // Function to save changes back to modal values and post
    $('.save-changes').on('click', function () {
        var newNameValue = $('.edit.name').val().trim();
        var newDrinkValue = $('.edit.drink').val().trim();
        var postId = $('#modalId').text().trim();
        
        // Update modalName and modalDrink spans in modal
        $('#modalName').text(newNameValue);
        $('#modalDrink').text(newDrinkValue);
        
        // Update post in the only-post section
        var postToUpdate = $('.search-nav[data-id="' + postId + '"]');
        postToUpdate.find('.post-text h4 a').text(newNameValue + ' - ' + newDrinkValue);
        
        // Send AJAX request to update the post on the server
        $.ajax({
            url: '/api/post/',  // Replace with your Django update post URL
            type: 'PUT',
            data: {
                name: newNameValue,
                drink: newDrinkValue,
                id: postId,
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is included
            },
            dataType: 'json',
            success: function (data) {
                console.log('Post updated successfully:', data);
                // Optionally handle success message or further actions
                location.reload();
            },
            error: function (xhr, status, error) {
                console.error('Error updating post:', error);
                // Optionally handle errors
            }
        });
    });

    $('.btn-danger').on('click', function () {
        // Reload the page
        location.reload();
    });
});
