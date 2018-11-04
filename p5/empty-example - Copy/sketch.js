
// for red, green, and blue color values
var r, g, b;

function setup() {
  createCanvas(720, 400);
  // Pick colors randomly
  r = random(255);
  g = random(255);
  b = random(255);
}

function draw() {
  background(127);
  // Draw a circle
  strokeWeight(2);
  stroke(r, g, b);
  fill(0);
  triangle(50, 50, 50, 80, 150, 80); 
  fill(r, g, b, 127);
  ellipse(mouseX, mouseY, 50, 50);
  
}

// When the user clicks the mouse
function mousePressed() {
  // Check if mouse is inside the circle
  var d = dist(mouseX, mouseY, 200, 200);
{
    
    // Pick new random color values
    r = random(255);
    g = random(255);
    b = random(255);
  }

}