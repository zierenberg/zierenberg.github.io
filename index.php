<!doctype html>
<html lang="en">
<head>
	<!-- Required meta tags -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<link rel="stylesheet" href="./css/main.css">
	<title>Johannes Zierenberg</title>
</head>

<body>
	<?php include_once("navigation.php"); ?>

	<div class="container">
		<div class="row flex-xl-nowrap">
			<!-- sidecolumn is col-3 col-xl-2 -->
			<?php include_once("sidecolumn.php"); ?>

			<main class="col-12 col-md-9 col-xl-10 content" role="main">
			  <div class="row mb-2 ">
        </div>
				<div class="row pd-2">
          <!--show this when sidebar is active-->
					<div class="col-4 col-sm-4 d-block d-md-none">
		          <img src="img/2018_johannes_small.jpg" name="johannes" class="content-img">
          </div>
					<div class="col-8 col-sm-8 d-block d-md-none">
						You can find me on<br>
            <ul class="list-unstyled">
	        	<li class="nav-item">
	        		<a class="nav-link" href="https://www.researchgate.net/profile/Johannes_Zierenberg">
					      <img class="svg feather" src="./img/academicons/ResearchGate.svg"></img>
	        			Research Gate
	        		</a>
	        	</li>
	        	<li class="nav-item">
	        		<a class="nav-link" href="https://github.com/zierenberg">
	        			<span data-feather="github"></span>
	        			Github
	        		</a>
	        	</li>
	        	<li class="nav-item">
	        		<a class="nav-link" href="https://twitter.com/jozierenberg">
	        			<span data-feather="twitter"></span>
	        			Twitter
	        		</a>
	        	</li>
	        	<li class="nav-item">
	        		<a class="nav-link" href="https://www.linkedin.com/in/johannes-zierenberg-8ab0971a/">
	        			<span data-feather="linkedin"></span>
	        			LinkedIn
	        		</a>
            </li>
            </ul>
					</div>
					<div class="col-md-12 pt-2">
            I am a theoretical physicist now in Neuroscience. Amongs others, I am interested in
            <ul>
            <li>phase transitions and critical phenomena,</li>
            <li>criticality in neural networks,</li>
            <li>effect of disorder and correlations,</li>
            <li>the analogy between particle condensation and polymer aggregation,</li>
            <li>and what comes along the way</li>
            </ul>
          </div>
					<div class="col-md-12 pt-2">
            <b>E-mail:</b><br>
            <div class="pl-2 pb-1">
            johannes.zierenberg@ds.mpg.de.
            </div>
            <b>Address:</b><br>
            <div class="pl-2 pb-1">
            Dr. Johannes Zierenberg<br>
            Max Planck Institute for Dynamics and Self-Organization<br>
            Am Fassberg 17<br>
            37077 Göttingen
            </div>
            <b>Short course of scientific life:</b><br>
            <div class="pl-2 pb-1">
            I studied physics in Leipzig and Zürich before doing a phd in Prof. Wolfhard Janke’s group in Leipzig. Now I am a postdoctoral researcher in Viola Priesemann’s group in Göttingen.
            </div>
            <b>Institute pages:</b></br>
            <div class="pl-2 pb-1">
            <a href="http://www.chaos.gwdg.de/people/zierenberg">[Göttingen]</a><br>
            <a href="http://www.physik.uni-leipzig.de/~zierenberg">[Leipzig]</a><br>
            </div>
          </div>
					<div class="col-md-12 col-lg-6 pt-2">
					</div>
				</div>
	  	</main>
		</div>
	</div>


	<!-- Icons -->
	<script>
		document.getElementById('navbar_home').classList.add("active");
	</script>
	<script src="./js/feather.min.js"></script>
  <script src="./js/replacesvg.js"></script>
	<script>feather.replace()</script>
	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
