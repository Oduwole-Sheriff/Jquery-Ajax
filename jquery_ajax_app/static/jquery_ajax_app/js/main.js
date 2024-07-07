
var $orders = $('#orders');

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


export function getAuthToken() {
    return localStorage.getItem('token');
}


export function getAllOrders(){

    const token = getAuthToken();

    // Check if token is null or empty
    if (!token) {
        console.log('Token not available');
        return; // or handle appropriately
    }

    $.ajax({
        type: 'GET',
        url: '/api/post/',
        headers: {
            'Authorization': `Token ${getAuthToken()}` // Assuming Bearer token authentication
        },
        success: function(orders){
            $.each(orders, function(i, order){
                addOrder(order);
            });
        },
        error: function(xhr, status, error) {
            alert('Error loading orders');
        }
    });
}

// console.log('Token:', getAuthToken());
// getAllOrders();



$(document).ready(function(){
    var $orders = $('#orders');
    var $name = $('#name');
    var $drink = $('#drink');
    var $image = $('#image');
    var $date = $('#date');

    
    

    getAllOrders();


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

let hamburger = document.querySelector(".hamburger");
let toggleMenu = document.querySelector(".background");
let toggleLogo = document.querySelector(".logo-display");
let toggleNav = document.querySelector("nav");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    toggleMenu.classList.toggle("active");
    toggleLogo.classList.toggle("active");
    toggleNav.classList.toggle("active");
})
