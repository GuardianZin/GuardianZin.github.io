function
setup(){
  createCanvas(720,480);
}
function draw(){
if(mouseIsPressed) {
  rect(mouseX,mouseY,80,80);
  strokeWeight(3);
fill(0,255,0,100,-100);
} else{
  fill(255,255,0 -1000000);
} 
rect(mouseX,mouseY,-80,-80);
translate(width /2, height /2);
rotate(PI / 3.0);

}