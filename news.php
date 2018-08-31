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

  <!-- todo: einruecken-->

	<div class="container">
		<div class="row flex-xl-nowrap">
			<!-- sidecolumn is col-sm-12 col-md-2 -->
			<?php include_once("sidecolumn.php"); ?>

			<main class="col-12 col-md-9 col-xl-10 content pub" role="main">
			  <div class="row mb-2 ">
          <!--hide this when sidebar is active-->
          <div class="col-12 d-md-none d-lg-block">
          </div>
          
          <div class="col-12">
          <h4> News </h4>
          <dl>
            <dt>01. 08. 2018: </dt>
              <dd> 
              We are happy to pre-announce the Focus session on "Collective dynamics in neural networks" at the next DPG Spring meeting in Regensburg, March 31 - April 5, 2019.  Invited speakers are Prof. Mortiz Helias (Jülich) and Prof. Anna Levina (Tübingen). We are looking forward to further interesting contributions!
              </dd> 
            <dt>29. 03. 2017: </dt>
              <dd> <a href=https://www.uni-leipzig.de/en/service/communication/medienredaktion/press-releases.html?ifab_modus=detail&ifab_uid=fb2606a50620170621080228&ifab_id=6975">Press release</a>
                   of "Canonical free-energy barrier of particle and polymer cluster formation" (publication Nr. 10). 
              <br>
              Media Coverage: 
              <a href="https://www.analytik-news.de/Presse/2017/134.html">ANALYTIK NEWS</a>,
              <a href="http://www.laborpraxis.vogel.de/wissenschaft-forschung/articles/585672/">LaborPraxis</a>,
              <a href="http://www.innovations-report.de/html/berichte/physik-astronomie/auf-den-spuren-der-entstehung-von-kondensationstropfen.html">Innovations Report</a>
              </dd>
            <dt>13. 03. 2017: </dt>
              <dd>Upcoming EPJ - Special Topics on Recent advances in phase transitions and critical phenomena! 
              We collected contributions by leading experts of the field on
              phase transitions and critical phenomena to provide a current perspective on
              the topics of interest. Currently all articles are in the final proof stage and
              will shortly be available on <a href="https://link.springer.com/journal/11734/226/4/page/1">European Physics Journal - Special Topics</a>.
              <br>
              Thank you to all contributers and enjoy reading.
              </dd>

            <dt>20. 08. 2016: </dt>
              <dd>First-order phase transitions in the real microcanonical ensemble (publication Nr. 11) was selected <a href="https://journals.aps.org/pre/abstract/10.1103/PhysRevE.94.021301">Editor's Suggestion</a>. 
              </dd>
            <dt>01. 02. 2016: </dt>
              <dd> Conference on recent advances in <a href="http://ptcp16.complexity-coventry.org/">Phase Transitions and Critical Phenomena</a> in Coventry, April 6-8, 2016 
              </dd>
          </dl>
          </div>
        </div>
		  </main>
		</div>
	</div>


	<!-- Icons -->
	<script>
		document.getElementById('navbar_news').classList.add("active");
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
