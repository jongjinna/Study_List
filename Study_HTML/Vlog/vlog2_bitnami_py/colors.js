var Links = {
  setColor:function(color){
    var alist = document.querySelectorAll('a');
    var i = 0;
    while(i < alist.length){
      alist[i].style.color = color;
      i = i + 1;
    }
  }
}
var Body = {
  setColor:function (color){
    document.querySelector('body').style.color = color;
  },
  setBackgroundColor:function (color){
    document.querySelector('body').style.backgroundColor = color;
  }
}
function NightDayHandler(Self){
  var target=document.querySelector('body')
  if(Self.value === 'night'){
    Body.setBackgroundColor('black')
    Body.setColor('white')
    Self.value = 'day';

    Links.SetColor('powderblue');
  } else {
    Body.setBackgroundColor('white')
    Body.setColor('black')
    Self.value = 'night';

    Links.SetColor('blue');
  }
}
