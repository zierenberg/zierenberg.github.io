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

function simple_sampling_x01(ID,func_y,func_Px,xmin,xmax,ymin,ymax){
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
  axes.y0 = canvas.height/2. - 1;     // y0 pixels from top to y=0
  axes.xm = canvas.width/2. -1;       // xm pixels from left to xmax
  axes.ym = 1;                     // ym pixels from top  to ymax
  axes.scalex = (axes.xm-axes.x0)/(xmax-xmin);   // width  pixels from x=0 to x=1 for x=[xmin,xmax]
  axes.scaley = (axes.y0-axes.ym)/(ymax-ymin);   // height pixels from y=0 to y=1 for y=[ymin,ymax]
  //axes.scaleP = (axes.y0-axes.ym)/(Pmax-Pmin);   // height pixels from y=0 to y=1 for P=[Pmin,Pmax]

  //P(x) for x in [0,1]
  var array_x_dx = 0.01;
  var array_x_nb = 1/array_x_dx+1;
  array_x=[];
  for(var i=0; i<array_x_nb; i++){array_x[i] = 0;}
  var hist={};
  hist.x0 = canvas.width/2.;
  hist.xm = canvas.width-1;
  hist.dx = (hist.xm-hist.x0)*array_x_dx;
  hist.y0 = axes.y0;
  hist.ym = axes.ym;

  showAxes(ctx,axes,5);
  funGraph(ctx,axes,func_y,"rgb(11,153,11)",5,axes.x0,axes.xm); 
  funGraph(ctx,axes,func_Px,"rgb(66,44,255)",3,axes.x0,axes.xm);
  draw_histogram(ctx,axes,hist,array_x);
  draw_timetrace(ctx,axes,0,0);
 
  $("#start").click(function() {
    console.log('here');
    id = setInterval(generate_points, 100);
  });

  $("#stop").click(function() {
    clearInterval(id);
    return;
  });

  var radius=7;
  var x=0,y=0;
  var exp_y = 0;
  var N = 0;
  function generate_points(){
    //remove old dots
    if(x!=0)clear_dot(ctx,axes,func_y, func_Px, x,y,radius);
    x = Math.random();
    y = func_y(x);
    //draw
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(axes.x0+x*axes.scalex, axes.y0-y*axes.scaley, radius, 0, 2*Math.PI, true);
    ctx.fill();
    //add to array
    array_x[Math.round(x/array_x_dx)]+=1;
    draw_histogram(ctx,axes,hist,array_x);
    //add to expectation value
    N+=1;
    exp_y = (exp_y*(N-1) + y*func_Px(x))/N;
    draw_timetrace(ctx,axes,exp_y,N);
    console.log(exp_y);
  }
}

function clear_dot(ctx,axes,func_y, func_Px, x,y,radius){
  var c_x=axes.x0+x*axes.scalex-radius-1;
  var c_y=axes.y0-y*axes.scaley-radius-1;
  var c_dx=2*radius+2;
  var c_dy=2*radius+2;
  ctx.clearRect(c_x,c_y,c_dx,c_dy);
  funGraph(ctx,axes,func_y,"rgb(11,153,11)",5,c_x,c_x+c_dx); 
  funGraph(ctx,axes,func_Px,"rgb(66,44,255)",3,c_x,c_x+c_dx);
}

function draw_histogram(ctx,axes,hist,data){
  ctx.clearRect(hist.x0,hist.y0,hist.xm-hist.x0+1,hist.ym-hist.y0-1);
  ctx.beginPath();
  ctx.moveTo(hist.x0-1,hist.y0,); ctx.lineTo(hist.xm,hist.y0);  // X axis
  ctx.strokeStyle = "rgb(128,128,128)"; 
  ctx.stroke();
  //var rmax = Math.max.apply(null, data);
  norm = 0;
  for(var i=0;i<data.length;i++){norm += data[i];}
  ctx.fillStyle = "rgb(66,44,255)";
  if(norm>0){
    for(var i=0;i<data.length;i++){
      var dy = (data[i] / norm)*(hist.y0-hist.ym);
      ctx.fillRect(hist.x0+i*hist.dx, hist.y0, hist.dx, -dy*10);
    };
  }
}

function draw_timetrace(ctx,axes,exp_y,N){
  ctx.beginPath();
  ctx.moveTo(axes.x0,axes.y0-1); ctx.lineTo(axes.x0,canvas.height-1);  
  ctx.strokeStyle = "rgb(128,128,128)"; 
  ctx.stroke();
  if(N>1){
    var dx = 1;
    var iMin=(N-1-axes.x0)/dx;
    var iMax=(N-axes.x0)/dx;
    var xx, yy;
    ctx.beginPath();
    for (var i=iMin;i<=iMax;i++) {
      xx = dx*i; 
      yy = axes.scaley*exp_y
      if (i==iMin) ctx.moveTo(axes.x0+xx,canvas.height-1-yy);
      else         ctx.lineTo(axes.x0+xx,canvas.height-1-yy);
    }
    ctx.strokeStyle = "rgb(11,153,11)";
    ctx.stroke();
  }
  else{
    var true_exp_y=1.65698;
    var dx = 1;
    var iMin=0;
    var iMax=1000;
    var xx, yy;
    ctx.beginPath();
    for (var i=iMin;i<=iMax;i++) {
      xx = dx*i; 
      yy = axes.scaley*true_exp_y;
      if (i==iMin) ctx.moveTo(axes.x0+xx,canvas.height-1-yy);
      else         ctx.lineTo(axes.x0+xx,canvas.height-1-yy);
    }
    ctx.lineWidth = 1;
    ctx.strokeStyle = "rgb(128,128,128)";
    ctx.stroke();
  }
}

function showAxes(ctx,axes, thick) {
 var x0=axes.x0, xm=axes.xm;
 var y0=axes.y0, ym=axes.ym;
 ctx.lineWidth = thick;
 ctx.beginPath();
 ctx.moveTo(x0-1,y0); ctx.lineTo(xm,y0);  // X axis
 ctx.stroke();
 ctx.moveTo(x0,y0-1); ctx.lineTo(x0,ym);  // Y axis
 ctx.strokeStyle = "rgb(128,128,128)"; 
 ctx.stroke();
 ctx.beginPath();
 ctx.moveTo(xm,y0-1); ctx.lineTo(xm,ym);  // Px axis
 ctx.strokeStyle = "rgb(66,44,255)"; 
 ctx.stroke();
}

function funGraph (ctx,axes,func,color,thick,xmin,xmax) {
 var xx, yy, dx=1, x0=axes.x0, y0=axes.y0;
 //var iMax = ctx.canvas.width/dx;
 //var iMin = 0;
 var iMin=(xmin-axes.x0)/dx;
 var iMax=(xmax-axes.x0)/dx;
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

