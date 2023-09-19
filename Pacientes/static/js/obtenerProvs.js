const listarProveedores = async() => {
  try {
  const response = await fetch("./proveedor")
  const data = await response.json()
  if(data.message=="Success"){
  let opciones=``
  data.proveedor.forEach((Proveedores) => {
  opciones+=`<option value='${Proveedores.cedula_prov}'>${Proveedores.nombre_prov} ${Proveedores.apellido_prov}</option>`
  })
  cboProveedores.innerHTML=opciones
  }else{
    alert("Proveedores no encontrados...")
  }
  }catch(err){
    console.log(err)
  }
}

const cargaInicial = async() => {
  await listarProveedores()
}

window.addEventListener("load", async () => {
    await cargaInicial()
})