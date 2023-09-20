(function () {
    const $formularioProveedores = document.getElementById('formularioProveedores')
    const $txtCedulaProv = document.getElementById('txtCedulaProv')
    const $txtRifProv = document.getElementById('txtRifProv')
    const $txtNombreProv = document.getElementById('txtNombreProv')
    const $txtApellidoProv = document.getElementById('txtApellidoProv')
    const $txtDireccionProv = document.getElementById('txtDireccionProv')
    const $txtTelefonoProv = document.getElementById('txtTelefonoProv')

        $formularioProveedores.addEventListener('submit', function (e) {
            let cedula_prov = String($txtCedulaProv.value).trim()
            let rif = String($txtRifProv.value).trim()
            let nombre_prov = String($txtNombreProv.value).trim()
            let apellido_prov = String($txtApellidoProv.value).trim()
            let direccion_prov = String($txtDireccionProv.value).trim()
            let telefono_prov = String($txtTelefonoProv.value).trim()

                if(cedula_prov.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }
                if(rif.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(nombre_prov.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(apellido_prov.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(direccion_prov.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }

                if(telefono_prov.length === 0 ){
                    alert('No se pueden enviar campos con espacios en blanco')
                    e.preventDefault()
                }
        })
    
    }) ()