function
setup(){
  createCanvas(500,500);
}
function draw(){
if(mouseIsPressed) {
  rect(mouseX,mouseY,80,80);
  ellipse(mouseX,mouseY,-80,-180);
  fill(255,255,255,0)
  strokeWeight(3);
fill(268,118,200,200,);
} else{
  fill(0,255,0 -0);
} 
rect(mouseX,mouseY,-80,-80);
translate(width /2, height /2);
rotate(PI / 3.0);

}