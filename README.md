

-----BEGIN PGP MESSAGE-----

jA0ECQMCcid9ug1cDbDq0sCbAe9a8IdvUF6aJ3M8JFfLO+n5poWCv5sM2929fJmd
I/YeX+H+QNFTOMKS1gjBYZpfDNY0AhslMl9w5qPJIqr6pF+E0zU4fMGTG9yR3QFG
8P/RwMcLS5BylInPbQGYwdsRoiiwwpaB9fCmcbYq6kne+++3OvaJQzoTyUXAfnvX
qU+JZEPjWLnQnTZOjEbTSvEgyCgiegluHXJ1AWPPPF/SPFDX9+Blg9Se4r2n2gk/
OGjeGiFkNynbiWP6ipnhQzA3xLraCTTDUiWE1iLoHRmLaRtz3fBqPb9zT1Zn0wb4
PbcS+sKfxl09V4HchmW8QSH974372JoHCin2UmpeeFa0elMTK7VH/vb6UeX6QLH4
+nYOAAbKCFwfLVf5CKTCuWUOwR0cafDkIXCcs3d8XIMaEQJBv6PR9Y13WZ1sVtPt
dGgCUZhJzim1QBDHE+m6cz/ppLyexoyxEyqRI6M=
=k01E
-----END PGP MESSAGE-----

passphrase jopa






function loadScript(url, callback)
{
    var head = document.head;
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    script.onreadystatechange = callback;
    script.onload = callback;
    head.appendChild(script);
}

var alert1 = function() {
console.log("ready");
};
loadScript("https://html2canvas.hertzen.com/dist/html2canvas.js", alert1);



var writer = [];
window.removeEventListener('scroll', scrollFunction);
var active = false;
var a = document.createElement("a");
document.body.appendChild(a);
a.style = "display: none";
var time1;
var writerSize = [];
function scrollFunction() {
  clearTimeout(time1);
  time1  = setTimeout(() => {
    console.log("Delayed for 1 second.");

    if (!active) {
      active = true;
      for (let i = 146; i < 500; i++) { 
        if(writer.includes(i)) {continue;}
        var canvas = document.getElementById("page_"+i );
        if(canvas){
          var dataURL = canvas.toDataURL("image/png");
          var newTab = window.open('about:blank','image from canvas');
          newTab.document.write("<img src='" + dataURL + "' alt='from canvas'/>");

          canvas.toBlob((blob) => {
            let file = new Blob([blob], {type:"application/octet-stream"})
            console.log(i);
            if(blob.size>17000)
            {
              writer.push(i);
              console.log(blob.size);
              console.log(blob.type);

              let blobURL = URL.createObjectURL(file)
              a.href = blobURL;
              a.download = "page_"+i+'.png';
              a.click();

            }
          })
        }}


        canvasClass = document.getElementsByClassName('element task_materials')
        for (let i4 = 0; i4 < canvasClass.length; i4++) {
         
          
          if(canvasClass[i4]){
            let contents = canvasClass[i4].innerText;
            if(contents.length<10)continue;
              //console.log('canvasClass[i4] contents',contents);
              console.log('canvasClass[i4] contents.length',contents.length);
          }
           div = canvasClass[i4];
          //console.log('div',div);
          html2canvas(div).then(canvas => {
                  // var myImage = canvas.toDataURL();
                  // downloadURI(myImage, "task_materials_"+blob.size+'.png';);

                  if(canvas){
                   

                    canvas.toBlob((blob) => {
                      if(writerSize.includes(blob.size)) {return;}
                      if(blob.size>17000)
                      {
                          var dataURL = canvas.toDataURL("image/png");
                          var newTab = window.open('about:blank','image from canvas');
                          newTab.document.write("<img src='" + dataURL + "' alt='from canvas'/>");
                        writerSize.push(blob.size);
                        console.log(blob.size);
                        console.log(blob.type);
                        let file = new Blob([blob], {type:"application/octet-stream"})
                        let blobURL = URL.createObjectURL(file)
                        a.href = blobURL;
                        a.download = "task_materials_"+blob.size+'.png';
                        a.click();

                      }
                    });
                  }

                });
        }



        active = false;
      }

    }, "1000")



}

window.onscroll = scrollFunction;


let timerId = setInterval(window.scrollTo(window.scrollX+100, window.scrollY),2000);




