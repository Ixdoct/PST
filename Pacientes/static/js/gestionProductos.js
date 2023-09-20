(function () {

const $formularioProductos = document.getElementById('formularioProductos')
const $txtCodigo = document.getElementById('txtCodigo')
const $txtNombre = document.getElementById('txtNombre')
const $txtCantidad = document.getElementById('txtCantidad')

    $formularioProductos.addEventListener('submit', function (e) {
        let codigo = String($txtCodigo.value).trim()
        let nombre = String($txtNombre.value).trim()
        let cantidad = String($txtCantidad.value).trim()
            if(codigo.length === 0 ){
                alert('No se pueden enviar campos con espacios en blanco')
                e.preventDefault()
            }

            if( nombre.length === 0 ){
                alert('No se pueden enviar campos con espacios en blanco')
                e.preventDefault()
            }

            if(cantidad.length === 0 ){
                alert('No se pueden enviar campos con espacios en blanco')
                e.preventDefault()
            }
    })

}) ()