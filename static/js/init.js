(function($){
    $(function(){

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

    }); // end of document ready
})(jQuery); // end of jQuery name space

(function(){

    const semestre = document.getElementById("semestre");
    const materia = document.getElementById("materia");
    const label = document.getElementById("label");
    const field = document.getElementById("fieldd");
    const titulo = document.getElementById("titulo");
    const x = document.getElementById("x");

    console.log('Consola en js');

    const v = semestre.value;

    console.log(v);

    const m = materia.value;
    console.log(m);

    onmousemove= function (e) {

        if (e.clientY >= 290 && e.clientY <= 400){

            const v2 = semestre.value;
            console.log(v2);
            /*
            if (v==1){
                console.log('caso 1');
                materia.value = "Algebra"
            }else if(v==2){
                console.log('caso 2');
                materia.value = "Algebra Lineal";
            }else if(v==3){
                console.log('caso 3');
                materia.value = "Electricidad y Magnetismo";
            }else if(v==4){
                console.log('caso 4');
                materia.value = "Investigacion de Operaciones y Sistemas";
            }else if(v==5){
                console.log('caso 5');
                materia.value = "Diseno y Analisis de Algoritmos";
            }else if(v==6){
                console.log('caso 6');
                materia.value = "Calidad";
            }else if(v==7){
                console.log('caso 7');
                materia.value = "Bases de Datos 1";
            }else if(v==8){
                console.log('caso 8');
                materia.value = "Microprocesadores y Microcontroladores";
            }else if(v==9){
                console.log('caso 9');
                materia.value = "Gestion de Redes de Computadoras";
            };
            */

        }
    };


    semestre.addEventListener('click', e => {

        console.log('click en semestre');
        const va = semestre.textContent;

        console.log(v);
        location.reload();
    });
    if (x.onmouseover){
        alert('x.onmouseover');
    };
    x.addEventListener('click', e => {
        /*
         if (v==1 ){
         console.log('caso 1');
         const t= materia.value = "Algebra"
         if (t=="Algebra" ||
         t=="Computadoras y Programacion" ||
         t=="Calculo Diferencial e Integral" ||
         t=="Introduccion a la ingenieria en computacion" ||
         t=="Geometria analitica" ){
         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         }
         }else if(v==2){
         console.log('caso 2');
         materia.value = "Algebra Lineal";
         if (t=="Programacion Orientada a objetos" ||
         t=="Algebra Lineal" ||
         t=="Comunicacion Oral y Escrita" ||
         t=="Calculo Vectorial" ||
         t=="Administracion Contabilidad y Costos" ){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==3){
         console.log('caso 3');
         materia.value = "Electricidad y Magnetismo";
         if (t=="Electricidad y Magnetismo" ||
         t=="Metodos Numericos" ||
         t=="Ecuaciones Diferenciales" ||
         t=="Estructura de Datos" ||
         t=="Introduccion a la Economia"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==4){
         console.log('caso 4');
         materia.value = "Investigacion de Operaciones y Sistemas";
         if (t=="Investigacion de Operaciones y Sistemas" ||
         t=="Analisis de Circuitos Electricos" ||
         t=="Estructuras Discretas" ||
         t=="Ingenieria Economica" ||
         t=="Probabilidad y Estadistica" ){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==5){
         console.log('caso 5');
         materia.value = "Diseno y Analisis de Algoritmos";
         if (t=="Diseno y Analisis de Algoritmos" ||
         t=="Dispositivos Electronicos" ||
         t=="Lenguajes Formales y Automatas" ||
         t=="Medicion e Instrumentacion" ||
         t=="Programacion de Sistemas"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==6){
         console.log('caso 6');
         materia.value = "Calidad";
         if (t=="Calidad" ||
         t=="Compiladores" ||
         t=="Diseno Logico" ||
         t=="Ingenieria de software 1" ||
         t=="Sistemas de Comunicaciones" ||
         t=="Sistemas Operativos"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==7){
         console.log('caso 7');
         materia.value = "Bases de Datos 1";
         if (t=="Bases de Datos 1" ||
         t=="Dinamica de Sistemas Fisicos" ||
         t=="Diseno de Sistemas Digitales" ||
         t=="Redes de Computadoras 1" ||
         t=="Seguridad Informatica"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==8){
         console.log('caso 8');
         materia.value = "Microprocesadores y Microcontroladores";
         if (t=="Microprocesadores y Microcontroladores" ||
         t=="Organizacion y Administracion de Centros de Computo" ||
         t=="Sistemas de Control" ||
         t=="Sistemas de Informacion"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         }else if(v==9){
         console.log('caso 9');
         materia.value = "Gestion de Redes de Computadoras";
         if (t=="Gestion de Redes de Computadoras" ||
         t=="Habilidades Directivas" ||
         t=="Inteligencia Artificial"){

         }else{
         alert("Semestre y materia no coinciden\n" +
         "Vuelve a intentar.");
         location.reload();
         };
         };
         */

    });

    console.log('Despues...');

    //onmousemove = function(e){console.log("mouse location:", e.clientX, e.clientY)}
    //375 227
    //375 310
})();

