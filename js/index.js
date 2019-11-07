
var canvas =document.querySelector(".canvas");
var w,h;
(function setSize(){
	window.onresize=arguments.callee;
	w=window.innerWidth;
	h=window.innerHight;
	canvas.width=w;
	canvas.height=h;
})();
var y=233;
var canCon=cancas.getContext("2d");
setInterval(function(){
	canCon.beginPath();
	canCon.clearRect(0,0,w,h);
	canCon.fillStyle="red";
	canCon.rect(233,y++,66,66);
	canCon.fill();
},1000/60);