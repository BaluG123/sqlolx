function randomcolor(){
  letters='0123456789ABCDEF'
  color="#"
  for (var i=0;i<6;i++){
    var r=Math.floor(Math.random()*16)
    color=color+letters[r]
  }
  return color
}
function change(){
//var god=document.querySelector('.xxx');
//god.style.background=randomcolor()
var brand=document.querySelector('#brand');
brand.style.color=randomcolor()

//var brand=document.querySelector('#thebrand')
//brand.style.background=randomcolor()
}
setInterval(change,1000)
