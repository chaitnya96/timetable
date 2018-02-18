var container = $('div.container')

$('input#get').click(function(){
    $.ajax({
        type: 'GET'
        url: 'http://127.0.0.1:8080/sheduler/api/semester/3/'
        dataType: 'json'
        success: function(data){
            $.each(data,function(index, item){
                $.each(item,function(key , value){
                    container.append(key +' : '+ value +'</br>')
                });
                container.append('</br> </br>')
            });
        }
    });

})