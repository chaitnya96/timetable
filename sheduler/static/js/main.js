

$('input#get').click(function(){
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/sheduler/api/semester/3/?format=json',
        dataType: 'json',
         success: $(document).ready(function () {
            $.ajax({
                type: "GET",
                contentType: "application/json",
                dataType: "json",
                url: 'http://127.0.0.1:8000/sheduler/api/semester/3/?format=json',
            })
            .done(function (response) {
            //    $.each(response, function (index, value) {

               //     console.log(response.division);
                    $('div.container').append(response.division);
                 //   console.log(JSON.stringify(response));
                 //   console.log(response.GetDataResult.id);
                  //      alert("success")

             //   })
            })
        })})})


