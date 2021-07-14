// se crea el objeto  del formulario

const datos = {
    nombre: '',
    apellido:'',
    telefono:'',
    mail:'',
    Region:'',
    mensaje:''
}



//evento de los input y textarea

const nombre = document.querySelector('#nombre');
const apellido = document.querySelector('#apellido');
const telefono = document.querySelector('#telefono');
const mail = document.querySelector('#mail');
const Region = document.querySelector('#Region');
const mensaje = document.querySelector('#mensaje');


nombre.addEventListener     ('input',validaTexto);
apellido.addEventListener   ('input',validaTexto);
telefono.addEventListener   ('input',validaTexto);
mail.addEventListener       ('input',validaTexto);
Region.addEventListener     ('input',validaTexto);
mensaje.addEventListener    ('input',validaTexto);
   

// evento de submit

const formulario = document.querySelector('.formulario');
formulario.addEventListener ('submit',function(evento) {
    evento.preventDefault();

    //valdia el formulario

     const { nombre , appellido,telefono,mail,region,mensaje} = datos;
         if (nombre ==='' ||apellido === '' || telefono === '' || mail ==='' ||Region === '' || mensaje === ''){
             mostrarError('Todos los campos son obligatorios');
             
             return; // corta la linea de ejecucion del codigo
         }

         //crear la alerta de envio

         mostrarMensaje('Formulario enviado correctamente')

     // envia el formulario    
    //console.log('Enviando Formulario'); solo para validar funcion por consola
})

function validaTexto (evento){
    //console.log(evento.target.value); funcion para validiar sin crear objeto
    datos[evento.target.id] = evento.target.value;
    //console.log(datos); 
}

//muestra mensaje de envio correcto

function mostrarMensaje(mensaje){
    const alerta = document.createElement('P');
    alerta.textContent = mensaje;
    alerta.classList.add ('correcto');
    formulario.appendChild(alerta);

//mensaje desaparece despues de 3 segundos
setTimeout(()=>{
    alerta.remove();
},3000);
    
}

// muestra el error en pantalla

function mostrarError(mensaje){
    const error =document.createElement('P');
    error.textContent= mensaje;
    error.classList.add ('error');

  formulario.appendChild(error);

  //mensaje desaparece despues de algunos segundos 

  setTimeout(() => {
      error.remove();
  },3000);
}

// crear objeto inicio sesion---------------//

/*
const sesion = {
    rut:'',
    pasaporte:''
}

//evento de los input
const rut = document.querySelector('#rut');
const pasaporte = document.querySelector('#pasaporte');

rut.addEventListener     ('input',validaTexto);
pasaporte.addEventListener ('input',validaTexto);

//evento submit


var usuarioAutenticado = new Promise (function(resolve,reject){
    var auth = true;

    if(auth){
    //esto es una funcion resolve('usuario autenticado');// el promise se cumple

    }else{
    //esto es una funcion reject('no se pudo iniciar sesion');// el promise no se cumple

    }
});

usuarioAutenticado
    .then (function(resultado){
        //console.log(resultado)
    })
    .catch(function(error){
        //console.log(error)

    })

const iniciosesion = document.querySelector('usuario');
usuario.addEventListener('click',function(evento){
    evento.preventDefault();

    //valida el inicio de sesion

     const { rut , pasaporte = sesion};

        if (rut ==='' ||pasaporte === ''){
             mostrarError('Todos los campos son obligatorios');
             
             return; // corta la linea de ejecucion del codigo
         }

         //crear la alerta de envio

         mostrarMensaje('inicio correcto')

     // envia el formulario    
    //console.log('Enviando Formulario'); solo para validar funcion por consola
    })
    function validaTexto (evento){
    sesion[evento.target.id] = evento.target.value;
    }
    //muestra mensaje de envio correcto

    function mostrarMensaje(mensaje){
        const alerta = document.createElement('P');
        alerta.textContent = mensaje;
        alerta.classList.add ('sesionon');
        formulario.appendChild(alerta);

    //mensaje desaparece despues de 3 segundos
    setTimeout(()=>{
        alerta.remove();
    },3000);
        
    }
    // muestra el error en pantalla

    function mostrarError(mensaje){
        const error =document.createElement('P');
        error.textContent= mensaje;
        error.classList.add ('sesionoff');

    formulario.appendChild(error);

    //mensaje desaparece despues de algunos segundos 

    setTimeout(() => {
        error.remove();
    },3000);
    }

*/

