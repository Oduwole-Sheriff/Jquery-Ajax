$(document).ready(function(){

    var $orders = $('#orders');
    var $name = $('#name');
    var $drink = $('#drink');

    var orderTemplate = $('#order-template').html();

    var orderTemplate = "" +
    "<li data-id='{{id}}'>" +
    "<p><strong>Name:</strong> <span class='noEdit name'>{{name}}</span><input class='edit name' /></p>" +
    "<p><strong>Drink:</strong> <span class='noEdit drink'>{{drink}}</span><input class='edit drink' /></p>" +
    "<button data-id='{{id}}' class='remove'>X</button>" +
    "<button class='editOrder noEdit'>Edit</button>"+
    "<button class='saveEdit edit'>Save</button>"+
    "<button class='cancelEdit edit'>Cancel</button>"+
    "</li>";

    function addOrder(order){
        $orders.append(Mustache.render(orderTemplate, order)) ;
        // $orders.append('<li>Name: '+order.name+', Drink: '+ order.drink +'</li>') 
    }


    $.ajax({
        type: 'GET',
        url: '/api/post/',
        success: function(orders){
            $.each(orders, function(i, order){
                addOrder(order)
                // console.log(order)
            })
        },
        error: function() {
            alert('error loading orders');
        }
    });

    $('#add-order').click(function(){
        var order = {
            name: $name.val(),
            drink: $drink.val(),
        };

        $.ajax({
            type: 'POST',
            url: '/api/post/',
            data: order,
            success: function(newOrder){
                addOrder(newOrder)
            },
            error: function(){
                alert('error saving order')
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
        })
    });

    $orders.delegate('.remove', 'click', function(){

        var dataId = $(this).attr('data-id')
        var $li = $(this).closest('li');
        $.ajax({
            type: 'DELETE',
            url: '/api/post/',
            data: { id: dataId },
            success: function() {
                $li.fadeOut(300, function(){
                    $('this').remove();
                    console.log('Data deleted successfully');
                })
            },
            error: function() {
                console.error('Error deleting data:');
            }

        });
    });

    $orders.delegate('.editOrder', 'click', function(){
        var $li = $(this).closest('li');
        $li.find('input.name').val( $li.find('span.name').html() );
        $li.find('input.drink').val( $li.find('span.drink').html() );
        $li.addClass('edit');
    })

    $orders.delegate('.cancelEdit', 'click', function(){
        $(this).closest('li').removeClass('edit');
    })

    $orders.delegate('.saveEdit', 'click', function(){
        var $li = $(this).closest('li');
        var dataId = $(this).attr('data-id')
        var order = {
            id: dataId,
            name: $li.find('input.name').val(),
            drink: $li.find('input.drink').val()
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
            error: function() {
                alert('Error updating data:', error);
            }

        });
    })
    
});