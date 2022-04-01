
document.location.href = a;

function prendido(prendido) {
    console.log(a)
    let param = 'encendido='+ prendido;
    
    send_request(param);
  }



// Esta parte toma la solicitud GET y devuelve en funcion del parametro  param la informacion
//la informacion es result y a su vez es dirigida a la funcion update_table(result)
function send_request(param) {  
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/list2?' + param,
        beforeSend: function() {
            console.log('before send');
        },
        success: function(result) {
            update_table(result);
            console.log('after send')
        },
        error: function(){
            console.log('sucedio un error')
        }

    });
}

//La funcion data toma automaticamente el resultado y va creando 
//linea por lne los resultados. update_table(result) result es data. tema de nombres y resconstruye la tabla.


function update_table(data) {
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
      elem = data[key];
      row = '<tr> <td>' + elem['Luz'] + '</td>' + '<td>' + elem['encendido'] + '</td>' + '<td>' + elem['Ip'] + '</td>' + '<td>' + elem['descripcion'] + '</td>' + '</tr>';
      all_rows = all_rows + row;
    });

    $('#latabla tbody').html(all_rows);
  }
