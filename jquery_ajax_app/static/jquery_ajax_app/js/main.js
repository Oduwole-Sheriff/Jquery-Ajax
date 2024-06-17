$(document).ready(function(){

    var $orders = $('#orders');
    var $name = $('#name');
    var $drink = $('#drink');
    var $image = $('#image');
    var $date = $('#date');
    var $search_nav = $('.search-nav')

    var orderTemplate = "" +
    "<li data-id='{{id}}'>" +
    "<p><strong>Name:</strong> <span class='noEdit name'>{{name}}</span><input class='edit name' /></p>" +
    "<p><strong>Drink:</strong> <span class='noEdit drink'>{{drink}}</span><input class='edit drink' /></p>" +
    "<img src='{{image}}'></img>" +
    "<p><strong>Date:</strong> <span class='noEdit date'>{{date}}</span><input class='edit date' /></p>" +
    "<button data-id='{{id}}' class='remove'>X</button>" +
    "<button class='editOrder noEdit'>Edit</button>"+
    "<button data-id='{{id}}' class='saveEdit edit'>Save</button>"+
    "<button class='cancelEdit edit'>Cancel</button>"+
    "</li>";

    function addOrder(order){
        $orders.append(Mustache.render(orderTemplate, order));
    }

    $.ajax({
        type: 'GET',
        url: '/api/post/',
        success: function(orders){
            $.each(orders, function(i, order){
                addOrder(order);
            });
        },
        error: function(xhr, status, error) {
            alert('Error loading orders');
        }
    });

    $('#add-order').click(function(event){
        
        event.preventDefault();

        var formData = new FormData();
        formData.append('name', $name.val());
        formData.append('drink', $drink.val());
        formData.append('image', $image[0].files[0]);
        formData.append('date', $date.val());

        $.ajax({
            type: 'POST',
            url: '/api/post/',
            data: formData,
            contentType: false,
            processData: false,
            success: function(newOrder){
                addOrder(newOrder);
            },
            error: function(xhr, status, error){
                alert('Error saving order');
            },
            error: function(xhr, status, error) {
                var jsonResponse = JSON.parse(xhr.responseText);
                if (jsonResponse.errors) {
                    var errorMessage = "";
                    $.each(jsonResponse.errors, function(key, value) {
                        errorMessage += value.join(", ") + "\n";
                    });
                    alert(errorMessage);
                }
            }
        });
    });

    // Rest of your event handlers...

    // $orders.on('click', '.remove', function(){
    //     var dataId = $(this).attr('data-id');
    //     var $li = $(this).closest('li');
    //     $.ajax({
    //         type: 'DELETE',
    //         url: '/api/post/',
    //         data: { id: dataId },
    //         success: function() {
    //             $li.fadeOut(300, function(){
    //                 $(this).remove();
    //                 console.log('Data deleted successfully');
    //             });
    //         },
    //         error: function() {
    //             console.error('Error deleting data');
    //         }
    //     });
    // });

    $search_nav.on('click', '.remove', function(){
        var dataId = $(this).attr('data-id');
        var $search_nav = $(this).closest('.search-nav');

        const confirmDelete = confirm('Are you sure you want to delete this item?')

        if(confirmDelete === true){
            $.ajax({
                type: 'DELETE',
                url: '/api/post/',
                data: { id: dataId },
                success: function(){
                    $search_nav.fadeOut(300, function(){
                        $(this).remove();
                        console.log('Data deleted successfully');
                    });
                },
                error: function() {
                    console.error('Error deleting data');
                },
            });
        }
    })



    $orders.on('click', '.editOrder', function(){
        var $li = $(this).closest('li');
        $li.find('input.name').val( $li.find('span.name').html() );
        $li.find('input.drink').val( $li.find('span.drink').html() );
        $li.addClass('edit');
    });

    $orders.on('click', '.cancelEdit', function(){
        $(this).closest('li').removeClass('edit');
    });

    $orders.on('click', '.saveEdit', function(){
        var $li = $(this).closest('li');
        var dataId = $(this).attr('data-id');
        var order = {
            id: dataId,
            name: $li.find('input.name').val(),
            drink: $li.find('input.drink').val(),
            image: $li.find('input.image').val(),
            date: $li.find('input.date').val()
        };
        $.ajax({
            type: 'PUT',
            url: '/api/post/',
            data: order,
            success: function(newOrder) {
                $li.find('span.name').html(order.name);
                $li.find('span.drink').html(order.drink);
                $li.removeClass('edit');
            },
            error: function(xhr, status, error) {
                alert('Error updating data: ' + error);
            }
        });
    });
});