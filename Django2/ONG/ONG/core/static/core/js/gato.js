
$(document).ready(function() {

    $.get("https://api.thecatapi.com/v1/images/search?limit=5",function(response){
        console.log("El servicio Responde")
        console.log(response);

        $.each(response,function(index,elemet){
            console.log("agregar gato #"+index+",url:"+element.url);

            registroHTML+= "<tr>";
            registroHTML+= "        <td>";
            registroHTML+= "        "+index;
            registroHTML+= "        </td>";
            registroHTML+= "        <td>";
            registroHTML+= "        <img src=\""+element.url+"\" id=\"image-"+element.id+"\"width=\"200\"height=\"auto\" />";
            registroHTML+= "        </td>";
            registroHTML+= "        <td>";
            registroHTML+= "        <button>Reemplazar imagen</button>";
            registroHTML+= "        </td>";
            registroHTML+= "</tr>";
            $("#listado-gatos").append(registroHTML);

        });
    });
});