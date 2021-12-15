// console.log('funcionando');

var formulario = document.getElementById('formulario');
var respuesta = document.getElementById('respuesta');

formulario.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('me diste un click')

    var datos = new FormData(formulario);

    console.log(datos)
    console.log(datos.get('nombre_producto'))
    console.log(datos.get('descripcion_producto'))
    console.log(datos.get('stock'))
    console.log(datos.get('precio'))

    fetch('http://127.0.0.1:8000/producto/',{
        method: 'POST',
        body: datos
    })
        .then( res => res.json())
        .then( data => {
            console.log(data)
            
        } )
})