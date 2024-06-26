$("#id_country").change(function () {
    const url = $("#personForm").attr("data-cities-url");  // get the url of the `load_cities` view
    const countryId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
        data: {
            'country_id': countryId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
            console.log(data);
            
            $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
            

            // let html_data = '<option value="">---------</option>';
            // data.forEach(function (city) {
            //     html_data += `<option value="${city.id}">${city.name}</option>`
            // });
            // console.log(html_data);
            // $("#id_city").html(html_data);

            
        }
    });

});