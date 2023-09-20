(function () {
    const $formularioPacientes = document.getElementById('formularioPacientes')
    const $txtCedula = document.getElementById('txtCedula')
    const $txtNombre = document.getElementById('txtNombre')
    const $txtApellido = document.getElementById('txtApellido')
    const $txtEdad = document.getElementById('txtEdad')
    const $txtDireccion = document.getElementById('txtDireccion')
    const $txtLugarNac = document.getElementById('txtLugarNac')

        $formularioPacientes.addEventListener('submit', function (e) {
            let cedula = String($txtCedula.value).trim()
            let nombre = String($txtNombre.value).trim()
            let apellido = String($txtApellido.value).trim()
            let edad = String($txtEdad.value).trim()
            let direccion = String($txtDireccion.value).trim()
            let lugarnac = String($txtLugarNac.value).trim()

                if(cedula.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }
                if(nombre.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(apellido.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(edad.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(direccion.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(lugarnac.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }
        })
    
    }) ()