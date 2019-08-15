//Utility functions
function MetropolisHastings(probability, state, generateAState) {
    var aPossibleState = generateAState(state);
    var transitionOdds = probability(aPossibleState) / probability(state);
    var newState
    if (Math.random() <= transitionOdds) {
        newState = aPossibleState;
    } else {
        newState = state;
    }
    return newState;
}

function stdNormal(X) {
    var v = (1/Math.sqrt(Math.PI * 2)) * Math.exp( -X * X / 2)
    return v
}

function createNewStateFrom(X){
    var newState
    if (Math.random() <= .5) {
        newState = X + .1
    } else {
        newState = X - .1
    }
    return newState
}

function fun1(x) {return Math.sin(x);  }
function fun2(x) {return Math.cos(3*x);}


function draw(ID){
 var canvas = document.getElementById(ID);
 if (null==canvas || !canvas.getContext) return;

 var axes={}, ctx=canvas.getContext("2d");
 axes.x0 = .5 + .5*canvas.width;  // x0 pixels from left to x=0
 axes.y0 = .5 + .5*canvas.height; // y0 pixels from top to y=0
 axes.scale = 40;                 // 40 pixels from x=0 to x=1
 axes.doNegativeX = true;

 showAxes(ctx,axes);
 funGraph(ctx,axes,fun1,"rgb(11,153,11)",1); 
 funGraph(ctx,axes,fun2,"rgb(66,44,255)",2);
}

function my_fun1(x) {return Math.exp(x);  }
function my_fun2(x) {return fun2_A*Math.exp(-Math.pow(x-fun2_x0,2)/(2.*fun2_s2));}

function test_canvas(ID){
 var canvas = document.getElementById(ID);
 if (null==canvas || !canvas.getContext) return;
 canvas.width  = canvas.clientWidth;
 canvas.height = canvas.clientHeight;

 //reset canvas
 canvas.width=canvas.width

 var axes={}, ctx=canvas.getContext("2d");
 //ctx.clearRect(0, 0, canvas.width, canvas.height);
 //simplify by plotting explicitely from 0 to 1 and from 0 to 3 in y
 axes.x0 = 1;                     // x0 pixels from left to x=0
 axes.y0 = canvas.height - 1;     // y0 pixels from top to y=0
 axes.xm = canvas.width -1;       // xm pixels from left to xmax
 axes.ym = 1;                     // ym pixels from top  to ymax
 axes.scalex = (axes.xm-axes.x0)/1.;   // width  pixels from x=0 to x=1 for x=[0:1]
 axes.scaley = (axes.y0-axes.ym)/3.;   // height pixels from y=0 to y=1 for y=[0:3]


 fun2_x0=0.5;
 fun2_s2=Math.pow(0.1,2);
 fun2_A=3;
 showAxes(ctx,axes);
 funGraph(ctx,axes,my_fun1,"rgb(11,153,11)",1); 
 funGraph(ctx,axes,my_fun2,"rgb(66,44,255)",2);
}

function funGraph (ctx,axes,func,color,thick) {
 var xx, yy, dx=1, x0=axes.x0, y0=axes.y0;
 //var iMax = ctx.canvas.width/dx;
 //var iMin = 0;
 var iMin=0;
 var iMax=axes.xm;
 ctx.beginPath();
 ctx.lineWidth = thick;
 ctx.strokeStyle = color;

 for (var i=iMin;i<=iMax;i++) {
  xx = dx*i; 
  yy = axes.scaley*func(xx/axes.scalex);
  if (i==iMin) ctx.moveTo(x0+xx,y0-yy);
  else         ctx.lineTo(x0+xx,y0-yy);
 }
 ctx.stroke();
}

function showAxes(ctx,axes) {
 var x0=axes.x0, xm=axes.xm;
 var y0=axes.y0, ym=axes.ym;
 ctx.beginPath();
 ctx.moveTo(x0-1,y0); ctx.lineTo(xm,y0);  // X axis
 ctx.moveTo(x0,y0-1); ctx.lineTo(x0,ym);  // Y axis
 ctx.strokeStyle = "rgb(128,128,128)"; 
 ctx.stroke();
}

function test_run(ID){
  var canvas = document.getElementById(ID);
  console.log(canvas.height)
  console.log(canvas.width)
  var axes={}, ctx=canvas.getContext("2d");
  //ctx.clearRect(0, 0, canvas.width, canvas.height);
  //simplify by plotting explicitely from 0 to 1 and from 0 to 3 in y
  axes.x0 = 1;                     // x0 pixels from left to x=0
  axes.y0 = canvas.height - 1;     // y0 pixels from top to y=0
  axes.xm = canvas.width -1;       // xm pixels from left to xmax
  axes.ym = 1;                     // ym pixels from top  to ymax
  axes.scalex = (axes.xm-axes.x0)/1.;   // width  pixels from x=0 to x=1 for x=[0:1]
  axes.scaley = (axes.y0-axes.ym)/3.;   // height pixels from y=0 to y=1 for y=[0:3]

  var buttonX = 70;
  var buttonY = 80;
  var buttonW = 60;
  var buttonH = 30;

  ctx.fillStyle = 'red';
  ctx.fillRect(buttonX, buttonY, buttonW, buttonH);

  // Add event listener to canvas element
  var active=false;
  var id=null;
  canvas.addEventListener('click', function(event) {
    // Control that click event occurred within position of button
    // NOTE: This assumes canvas is positioned at top left corner 
    const rect = canvas.getBoundingClientRect();
    var scale = canvas.width / parseFloat(rect.width);
    const x = (event.clientX - rect.left)*scale;
    const y = (event.clientY - rect.top)*scale;
    if (
      x > buttonX && 
      x < buttonX + buttonW &&
      y > buttonY && 
      y < buttonY + buttonH
    ) {
      // Executes if button was clicked!
      if(active){
        clearInterval(id);
        active=false;
        ctx.strokeStyle = 'black';
        ctx.clearRect(buttonX, buttonY, buttonW, buttonH);
        ctx.rect(buttonX, buttonY, buttonW, buttonH);
        ctx.stroke();
        ctx.font = "30px Arial";
        ctx.fillText("Start", buttonX, buttonY); 
      }
      else{
        id=setInterval(generate_points,100);
        active=true;
        ctx.strokeStyle = 'black';
        ctx.clearRect(buttonX, buttonY, buttonW, buttonH);
        ctx.rect(buttonX, buttonY, buttonW, buttonH);
        ctx.stroke();
      }
    }
  });
 
  $("#start").click(function() {
    id = setInterval(generate_points, 100);
  });

  $("#stop").click(function() {
    clearInterval(id);
  });

  ///???
  //var id=setInterval(generate_points,100);
  function generate_points(){

    //remove old dot?
    var x = Math.random();
    var y = my_fun1(x);
  
    //ctx.fillRect(x-2,y-2,4,4);
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(axes.x0+x*axes.scalex, axes.y0-y*axes.scaley, 3, 0, 2*Math.PI, true);
    ctx.fill()
  }
}

function test(ID){
            var width = 300,
                height = 400,
                padding = 50;


            var x = d3.scale.linear()
                .domain([-4, 4])
                .range([padding, width-padding]);
            var svg = d3.select(ID)
                .append("svg")
                .attr("height", height)
                .attr("width", width)

            // Taking 1 million simulations of the standard normal
            var values = []
            
            var state = 0
            for (var i = 0; i < 1000000; i++) {
              state = MetropolisHastings(stdNormal, state, createNewStateFrom);
              values.push(state)
              if(i%100000==0){
                svg.selectAll("*").remove()
                var data = d3.layout.histogram()(values);
                var y = d3.scale.linear()
                    .domain([0, d3.max(data, function(d) { return d.y; })])
                    .range([height, 0]);
                var bar = svg.selectAll("rect")
                    .data(data)
                  .enter().append("rect")
                    .classed("bar", true)
                    .attr("x", function(d){
                        return x(d.x)
                    })
                    .attr("y", function(d) {
                        return y(d.y)
                    })
                    .attr("width", (x(data[0].dx) - x(0)) * .95 )
                    .attr("height", function(d) {
                        return height - y(d.y) - padding;
                    });
                var xAxis = d3.svg.axis()
                .scale(x)
                .orient("bottom");
                svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + (height - padding) + ")")
                .call(xAxis);
              }
            }


            
            
}
