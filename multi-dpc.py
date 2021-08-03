#!/usr/bin/python3

import os
import sys
import time

# banner
banner = """\033[1;32;49m ┌─────────────────────────────────────────────────────────┐
 │                 _  _    _         _                     │
 │     _____  _ _ | || |_ |_| ___  _| | ___  ___  {v.1}    │
 │    |     || | || ||  _|| ||___|| . || . ||  _|          │
 │    |_|_|_||___||_||_|  |_|     |___||  _||___|          │
 │                                     |_|                 │
 │                                                         │
 │              [Multi Deface Page Creator]                │
 │                                                         │
 │   Github   : https://github.com/mkdirlove/multi-dpc     │
 │   Facebook : https://free.facebook.com/mkdirlove.git    │
 │                                                         │
 └─────────────────────────────────────────────────────────┘
 
 »     CREDITS TO THE FOLOWING OWNERS OF DEFACE PAGES      « 
 \033[1;32;49m"""

options = """\033[1;32;49m [01] » Mr.D347H                           [05] » CLOWNSEC 
 [02] » GR1MR34P3R                         [06] » Mr.GrinXz   
 [03] » Chaos Cyber Hood                   [07] » MR TOM
 [04] » Anonymouse                         [00] » Exit"""

# slowprint function
def slowprint(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

# Mr.D347H deface page
def MrD347H():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input("» ")
  print(" ")
  time.sleep(0.1)
  print(" Enter your message for the website")
  message = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
</head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Hacked By Mr.D347H">
    <meta name="author" content="T3rr8us">

    <!-- Le styles -->
	<link rel="SHORTCUT ICON" href="http://winhacker.do.am/favicon.ico" />
	<link href="https://fonts.googleapis.com/css2?family=Iceland&display=swap" rel="stylesheet">
<style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      background: #000;
      padding-bottom: 40px;
      color: #000;
      
      -webkit-transform: rotateX(90deg);
      -moz-transform: rotateX(90deg);
      -ms-transform: rotateX(90deg);
      -o-transform: rotateX(90deg);
      transform: rotateX(90deg);
      -webkit-transform: translateZ(-100px);
      -moz-transform: translateZ(-100px);
      -ms-transform: translateZ(-100px);
      -o-transform: translateZ(-100px);
      transform: translateZ(-100px);
      -webkit-animation: rain 3s infinite linear;
      -moz-animation: rain 3s infinite linear;
      -ms-animation: rain 3s infinite linear;
      -o-animation: rain 3s infinite linear;
      animation: rain 3s infinite linear;
    }

    @-webkit-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-moz-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-ms-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-o-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 0px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
	  
	  font-family: Verdana, Arial, Helvetica, sans-serif; 
	  color : black;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    @media (max-width: 979px) {

      .featurette {
        height: auto;
        padding: 0;
      }
	  
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    @media (max-width: 767px) {

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 15px;
        line-height: 1.5;
      }

    }
    </style>	
    <body>
<!--
 * Do not Copy 
 * @author Winhacker
 * @copyright 2016 Winhacker
------------------------------------------------------- 
-->
	<br><br><div class="featurette">"""
	
  code4 = """<img src="""

  code5 = img

  code6 = """ width =99% height=200px>
		<center><h2 class="featurette-heading"><b>
		<script> 
		farbbibliothek = new Array(); 
		farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100"); 
		farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00"); 
		farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00"); 
		farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040"); 
		farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000"); 
		farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF"); 
		farbbibliothek[6] = new Array("#0000FF","#FFFF00"); 
		farben = farbbibliothek[4];
		function farbschrift() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.all["a"+i].style.color=farben[i]; 
			} 
			farbverlauf(); 
		} 
		function string2array(text) 
		{ 
			Buchstabe = new Array(); 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 
			k=0; 
			while(k<=text.length) 
			{ 
				Buchstabe[k] = text.charAt(k); 
				k++; 
			} 
		} 
		function divserzeugen() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>"); 
			} 
			farbschrift(); 
		} 
		var a=1; 
		function farbverlauf() 
		{ 
			for(var i=0 ; i<farben.length; i++) 
			{ 
				farben[i-1]=farben[i]; 
			} 
			farben[farben.length-1]=farben[-1]; 
 
			setTimeout("farbschrift()",30); 
		} 
		// Zu Demonstrationszwecken***************** 
		var farbsatz=1; 
		function farbtauscher() 
		{ 
			farben = farbbibliothek[farbsatz]; 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 	
			farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001)); 
		} 
		setInterval("farbtauscher()",4500); 
		text=" You Have Been Hacked ";
//h 
		string2array(text);
		divserzeugen(); 
//document.write(text);   
//
/*function expand() {
for(x = 0; x < 50; x++) {
window.moveTo(screen.availWidth * -(x - 50) / 100, screen.availHeight * -(x - 50) / 100);
window.resizeTo(screen.availWidth * x / 50, screen.availHeight * x / 50);
}
window.moveTo(0,0);
window.resizeTo(screen.availWidth, screen.availHeight);
}
expand();*/
	</script>"""

  code7 = """</b></h2></center>
		<hr width="80%" style="color:black" />

		<div style="background : black; padding : 10px;">
<b><center>
<font face="Tahoma" size="5" color=red>"""




  code8 = """[<marquee style="width:200px;height:24px;"><font face="Iceland" color=white>Hacked By : <font face="Iceland" color=red>"""

  code9 = codename

  code10 = """<font color=red></font></font></marquee>]</font></center></b>
		</div>"""

  code11 = """
<p style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size : 16px;" align="center"><font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : red; font-size : 16px;" align="center">Hello <font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : white; font-size : 16px;" align="center">"""

  code12 = message 

  code13 = """</p>
    </div>
	<br/><br/>

  </body>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)
  fo.write(code10)
  fo.write(code11)
  fo.write(code12)
  fo.write(code13)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# GR1MR34P3R deface page
def gr1mr34p3r():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter your message for the website")
  message = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
<head>
    <meta content="width=devic­e-width, initial-scale=1" name="viewport" />
    <meta property="og:title" content="[ Mr.GR1MR34P3R ]">
    <meta name="description" content="Hello Admin , Im Mr.GR1MR34P3R , Let's Honk the Planet.">
    <link rel="preconnect" href="https://­fonts.gstatic.com/">
    <link href="https://­fonts.googleapis.com/­css2?family=Righteous­&display=swap" rel="stylesheet">
    <link href="https://­fonts.googleapis.com/­css2?family=Montserra­t%3Awght%40100&displ­ay=swap" rel="stylesheet">
    <link rel="icon" href="https://i.imgur.com/­8lCDBye.png" type="image/­icon type">
    <title>Mr.GR1MR34P3R</title>
    <style>
      * {
        user-select: none;
      }

      body {
        background: black;
      }

      body::after {
        content: "";
        background: url('https://­images.unsplash.com/­photo-1502905704466-2­690947baeee?ixid=MXw­xMjA3fDB8MHxzZWFyY2h­8MXx8Y2l0eSUyMHNreWx­pbmV8ZW58MHx8MHw%3D&­ixlib=rb-1.2.1&w=100­0&q=80');
        background-position: ­ center;
        background-repeat: no-repeat;
        background-size: cover;
        opacity: 0.3;
        filter: blur(3px);
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        position: absolute;
        
        z-index: -1;
        overflow: hidden;
      }

      .logo img {
        float: right;
        width: 40%;
        margin: 5% 5% 0 0;
      }

      #pwnd {
        position: absolute;
        color: white;
        font-family: 'Righteous', cursive;
        font-size: 6em;
        margin: 12% 0 0 5%;
      }

      #pwnd span {
        color: #c2252a;
      }

      #pwnd .GR1MR34P3R {
        font-size: 20%;
        font-family: 'Montserrat', sans-serif;
      }

      @media screen and (max-width: 1024px) {
        * {
          margin: 0;
        }

        #pwnd {
          font-size: 250%;
          text-align: center;
          width: 100%;
          margin: 0 0 0 0;
          position: absolute;
          top: 35%;
          transform: translate(0, -50%);
        }

        .logo img {
          margin: 0;
          float: none;
          text-align: center;
          display: block;
          margin-left: auto;
          margin-right: auto;
          width: 200px;
        }

        .logo {
          width: 100%;
          margin-top: 45vh;
        }
      }
    </style>
    </­head>
<body onkeydown='return false' ; oncontextmenu='alert`ho­nk`;return false;'>
"""
  code4 = """ width =99% height=200px>
<div id="pwnd">Honked By <br>"""
  code5 = codename 
  code6 = """<div class="clownsec"> 
  <br>"""
  code7 = message
  code8 = """
        </div>
    </div>"""
  code9 = """<div class="logo">"""
  code10 = """<img src=" """
  code11 = img
  code12 = """">"""
  code13 = """
    </div>
  </body>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)
  fo.write(code10)
  fo.write(code11)
  fo.write(code12)
  fo.write(code13)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# Chaos Cyber Hood deface page
def cch():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
<style>
*{

padding,margin:0;
}
body{
max-height:100%;
max-width:100%;
overflow-x:hidden;
background-color:bla­ck;
}

img{
position:relative;
left:230px;
height:700px;
width:700px;
}
.content{
width: 100%;
font-family: 'Press Start 2P';
height: 30%;
display: flex;
justify-content: center;
align-items: center;
}
.content .text{
position: relative;
color: #fff;

font-weight: 700;
font-size: 35px;
transform: scale(2);
padding: 30px;
left:10%;
letter-spacing: 2px;
text-transform: uppercase;
}
.content .text:before,
.content .text:after {
padding: 30px;
color: white;
content: attr(data-text);
position: absolute;
width: 100%;
height: 100%;
background: black;
overflow: hidden;
top: 0;
}
.content .text:before{
left: 3px;
position:absolute;
top:10px;
left:5px;
text-shadow: 5px 0 0 blue;
animation: glitch-1 3s linear infinite reverse;
}
.content .text:after{
left: 2px;
position:absolute;
top:5px;
right:5px;
text-shadow: 5px 0 red;
animation: glitch-2 3s linear infinite reverse;
}

@keyframes glitch-1 {
0% {
clip: rect(132px, auto, 101px, 30px);
}
5% {
clip: rect(17px, auto, 94px, 30px);
}
10% {
clip: rect(40px, auto, 66px, 30px);
}
15% {
clip: rect(87px, auto, 82px, 30px);
}
20% {
clip: rect(137px, auto, 61px, 30px);
}
25% {
clip: rect(34px, auto, 14px, 30px);
}
30% {
clip: rect(133px, auto, 74px, 30px);
}
35% {
clip: rect(76px, auto, 107px, 30px);
}
40% {
clip: rect(59px, auto, 130px, 30px);
}
45% {
clip: rect(29px, auto, 84px, 30px);
}
50% {
clip: rect(22px, auto, 67px, 30px);
}
55% {
clip: rect(67px, auto, 62px, 30px);
}
60% {
clip: rect(10px, auto, 105px, 30px);
}
65% {
clip: rect(78px, auto, 115px, 30px);
}
70% {
clip: rect(105px, auto, 13px, 30px);
}
75% {
clip: rect(15px, auto, 75px, 30px);
}
80% {
clip: rect(66px, auto, 39px, 30px);
}
85% {
clip: rect(133px, auto, 73px, 30px);
}
90% {
clip: rect(36px, auto, 128px, 30px);
}
95% {
clip: rect(68px, auto, 103px, 30px);
}
100% {
clip: rect(14px, auto, 100px, 30px);
}
}

@keyframes glitch-2 {
0% {
clip: rect(129px, auto, 36px, 30px);
}
5% {
clip: rect(36px, auto, 4px, 30px);
}
10% {
clip: rect(85px, auto, 66px, 30px);
}
15% {
clip: rect(91px, auto, 91px, 30px);
}
20% {
clip: rect(148px, auto, 138px, 30px);
}
25% {
clip: rect(38px, auto, 122px, 30px);
}
30% {
clip: rect(69px, auto, 54px, 30px);
}
35% {
clip: rect(98px, auto, 71px, 30px);
}
40% {
clip: rect(146px, auto, 34px, 30px);
}
45% {
clip: rect(134px, auto, 43px, 30px);
}
50% {
clip: rect(102px, auto, 80px, 30px);
}
55% {
clip: rect(119px, auto, 44px, 30px);
}
60% {
clip: rect(106px, auto, 99px, 30px);
}
65% {
clip: rect(141px, auto, 74px, 30px);
}
70% {
clip: rect(20px, auto, 78px, 30px);
}
75% {
clip: rect(133px, auto, 79px, 30px);
}
80% {
clip: rect(78px, auto, 52px, 30px);
}
85% {
clip: rect(35px, auto, 39px, 30px);
}
90% {
clip: rect(67px, auto, 70px, 30px);
}
95% {
clip: rect(71px, auto, 103px, 30px);
}
100% {
clip: rect(83px, auto, 40px, 30px);
}
}


#typewriter{
font-family: 'Creepster';
font-size:50px;
position:relative;
color:green;
top:150px;
left:25%;
}
b{
color:white;
}
.handler{
position:absolute;
}
#typehandler{

position:relative;
background-color:bla­ck;
width:1000px;
height:170px;
left:10%;
top:100px;
border: none;
border:2px solid #A9A9A9;
}
#cn{

color:red;
}
#music {
display:none;
}
</style>
<link href="https://­fonts.googleapis.com/­css2?family=Creepster­&display=swap" rel="stylesheet"> <link href="https://­fonts.googleapis.com/­css2?family=Press+Sta­rt+2P&display=swap" rel="stylesheet">
</head>

<body>
<div id="music">
<audio autoplay>
<source src="https://­i.top4top.io/­m_2036r0x210.mp3" type="audio/mpeg">
<p>If you can read this, your browser does not support the audio element.</p> </audio>
</div>
"""
	
  code4 = """<img src=" """

  code5 = img

  code6 = """ ">"""

  code7 = """</b></h2></center>
		<hr width="80%" style="color:black" />

		<div style="background : black; padding : 10px;">
<b><center>
<font face="Tahoma" size="5" color=red>"""




  code8 = """<div class="content">
<h2 class="text" data-text="PWNED BY CCH">
PWNED BY """
  code9 = codename

  code10 = """
</div>
<div class="handler">
<div id="typehandler"></­div>
</div>
<div id="typewriter"></­div>

<script>


alert("WEAK SECURITY LOL")

</script>
<script>


alert("special message from me: POGI PO AKOxD")

</script>

<script src="https://unpkg.com/­typewriter-effect@lat­est/dist/core.js"></script> <script type='text/­javascript'>
const typewriter = new Typewriter('#typewri­ter', {
loop: false,
});

typewriter.typeStrin­g('Hello Admin')
.changeCursor('<b><~­</b>')
.pauseFor(2000)
.deleteAll()
.typeString('you got a little problem here LOL')
.pauseFor(2000)
.deleteAll()

.typeString(' Greet to <span id="cn">MrXmile</­span>')
.pauseFor(2000)
.deleteChars(7)
.typeString("<span id='cn'>maestro</­span>")
.pauseFor(2000)
.deleteChars(7)
.typeString("<span id='cn'>TrinityLulz<­/span>")
.pauseFor(2000)
.deleteChars(11)
.typeString("<span id='cn'>Hack-Ninja</­span>")
.pauseFor(2000)
.deleteChars(10)

.typeString("<span id='cn'>Haxcoder</­span>")
.pauseFor(2000)
.deleteChars(7)
.typeString("<span id='cn'>CYCL0P5</­span>")
.pauseFor(2000)
.deleteChars(7)
.typeString("<span id='cn'>Mr.$cript</­span>")
.pauseFor(2500)
.deleteChars(9)
.typeString("<span id='cn'>R|E'xp3ct.Me­</span>")
.pauseFor(2500)
.deleteChars(12)
.typeString("<span id='cn'>S4SHZ-X</­span>")
.pauseFor(2500)
.deleteChars(7)
.typeString("<span id='cn'>Ph.Kawayan</­span>")
.pauseFor(2500)
.deleteChars(10)
.deleteAll()
.typeString("HAVE A GREAT DAY, GOOD BYE")
.start()
</script>
</body>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  print(banner)
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)
  fo.write(code10)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# Anonymouse deface page
def anonymouse():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input("» ")
  print(" ")
  time.sleep(0.1)
  print(" Enter your message for the website")
  message = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
</head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Hacked By Mr.D347H">
    <meta name="author" content="T3rr8us">

    <!-- Le styles -->
	<link rel="SHORTCUT ICON" href="http://winhacker.do.am/favicon.ico" />
	<link href="https://fonts.googleapis.com/css2?family=Iceland&display=swap" rel="stylesheet">
<style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      background: #000;
      padding-bottom: 40px;
      color: #000;
      
      -webkit-transform: rotateX(90deg);
      -moz-transform: rotateX(90deg);
      -ms-transform: rotateX(90deg);
      -o-transform: rotateX(90deg);
      transform: rotateX(90deg);
      -webkit-transform: translateZ(-100px);
      -moz-transform: translateZ(-100px);
      -ms-transform: translateZ(-100px);
      -o-transform: translateZ(-100px);
      transform: translateZ(-100px);
      -webkit-animation: rain 3s infinite linear;
      -moz-animation: rain 3s infinite linear;
      -ms-animation: rain 3s infinite linear;
      -o-animation: rain 3s infinite linear;
      animation: rain 3s infinite linear;
    }

    @-webkit-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-moz-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-ms-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-o-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 0px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
	  
	  font-family: Verdana, Arial, Helvetica, sans-serif; 
	  color : black;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    @media (max-width: 979px) {

      .featurette {
        height: auto;
        padding: 0;
      }
	  
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    @media (max-width: 767px) {

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 15px;
        line-height: 1.5;
      }

    }
    </style>	
    <body>
<!--
 * Do not Copy 
 * @author Winhacker
 * @copyright 2016 Winhacker
------------------------------------------------------- 
-->
	<br><br><div class="featurette">"""
	
  code4 = """<img src="""

  code5 = img

  code6 = """ width =99% height=200px>
		<center><h2 class="featurette-heading"><b>
		<script> 
		farbbibliothek = new Array(); 
		farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100"); 
		farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00"); 
		farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00"); 
		farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040"); 
		farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000"); 
		farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF"); 
		farbbibliothek[6] = new Array("#0000FF","#FFFF00"); 
		farben = farbbibliothek[4];
		function farbschrift() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.all["a"+i].style.color=farben[i]; 
			} 
			farbverlauf(); 
		} 
		function string2array(text) 
		{ 
			Buchstabe = new Array(); 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 
			k=0; 
			while(k<=text.length) 
			{ 
				Buchstabe[k] = text.charAt(k); 
				k++; 
			} 
		} 
		function divserzeugen() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>"); 
			} 
			farbschrift(); 
		} 
		var a=1; 
		function farbverlauf() 
		{ 
			for(var i=0 ; i<farben.length; i++) 
			{ 
				farben[i-1]=farben[i]; 
			} 
			farben[farben.length-1]=farben[-1]; 
 
			setTimeout("farbschrift()",30); 
		} 
		// Zu Demonstrationszwecken***************** 
		var farbsatz=1; 
		function farbtauscher() 
		{ 
			farben = farbbibliothek[farbsatz]; 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 	
			farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001)); 
		} 
		setInterval("farbtauscher()",4500); 
		text=" You Have Been Hacked ";
//h 
		string2array(text);
		divserzeugen(); 
//document.write(text);   
//
/*function expand() {
for(x = 0; x < 50; x++) {
window.moveTo(screen.availWidth * -(x - 50) / 100, screen.availHeight * -(x - 50) / 100);
window.resizeTo(screen.availWidth * x / 50, screen.availHeight * x / 50);
}
window.moveTo(0,0);
window.resizeTo(screen.availWidth, screen.availHeight);
}
expand();*/
	</script>"""

  code7 = """</b></h2></center>
		<hr width="80%" style="color:black" />

		<div style="background : black; padding : 10px;">
<b><center>
<font face="Tahoma" size="5" color=red>"""




  code8 = """[<marquee style="width:200px;height:24px;"><font face="Iceland" color=white>Hacked By : <font face="Iceland" color=red>"""

  code9 = codename

  code10 = """<font color=red></font></font></marquee>]</font></center></b>
		</div>"""

  code11 = """
<p style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size : 16px;" align="center"><font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : red; font-size : 16px;" align="center">Hello <font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : white; font-size : 16px;" align="center">"""

  code12 = message 

  code13 = """</p>
    </div>
	<br/><br/>

  </body>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)
  fo.write(code10)
  fo.write(code11)
  fo.write(code12)
  fo.write(code13)

  print("")
  print(banner)

  fo.close()

# CLOWNSEC deface page
def clownsec():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter your message for the website")
  message = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
<meta name="Author" content="PINOY Clown-Sec TRiG3R-X"/>
<meta name="copyright" content="PINOY Clown-Sec 2018"/>
<meta name="keywords" content="Greetings Admin, I'm TRiG3R-X of PINOY CLOWN-SEC "/>
<style type="text/css">body{background-image:url('type="text/css">body{background-image:url('https://1366x768wallpaper.com/2015/07/26/14565-world-map-1920x1080-wallpaper-4360-dark-world.jpg');background-color:#000000;background-repeat:no-repeat;background-position:right');background-color:#000000;background-repeat:no-repeat;background-position:right top;color:#ffffff;margin:0px;}</style>
<style type="text/css">
        @import url(http://fonts.googleapis.com/css?family=Anonymous+Pro:700);
</style>"""
	
  code4 = """<div>
<center>
<img src=" """

  code5 = img

  code6 = """ " width="300"/>
<div align="center">
<body background="https://i.imgur.com/jXqHUkB.gif">
<script>alert('Honk Honk BITCH');</script>
<script>alert('Stamped By Pinoy Clown Sec');</script>
<script src="http://e-mete.com/js/kdsnow.js"></script>

<div align="center">
<pre style="font: 30px/10px courier;"><b><script language="JavaScript1.2">
var message=" """ 
  code7 = codename 
  code8 =""" "
var neonbasecolor="gray"
var neontextcolor="white"
var neontextcolor2="#FFFFA8"
var flashspeed=100                                             
var flashingletters=3  
var flashingletters2=1 
var flashpause=0       
 
var n=0
if (document.all||document.getElementById){
document.write('<font color="'+neonbasecolor+'">')
for (m=0;m<message.length;m++)
document.write('<span id="neonlight'+m+'">'+message.charAt(m)+'</span>')
document.write('</font>')
}
else
document.write(message)
 
function crossref(number){
var crossobj=document.all? eval("document.all.neonlight"+number) : document.getElementById("neonlight"+number)
return crossobj
}
 
function neon(){
 
//Change all letters to base color
if (n==0){
for (m=0;m<message.length;m++)
crossref(m).style.color=neonbasecolor
}
 
//cycle through and change individual letters to neon color
crossref(n).style.color=neontextcolor
 
if (n>flashingletters-1) crossref(n-flashingletters).style.color=neontextcolor2
if (n>(flashingletters+flashingletters2)-1) crossref(n-flashingletters-flashingletters2).style.color=neonbasecolor
 
 
if (n<message.length-1)
n++
else{
n=0
clearInterval(flashing)
setTimeout("beginneon()",flashpause)
return
}
}
 
function beginneon(){
if (document.all||document.getElementById)
flashing=setInterval("neon()",flashspeed)
}
beginneon()
 
</script></b></pre>
</div>"""




  code9 = """
  </font>	
</font><br>

PinoyClownSec Â© Alright Reserved 2018
</pre>

<iframe width="1" height="1" src="https://www.youtube.com/embed/5lLclBfKj48?rel=0&t=0m5s&autoplay=1&loop=1&playlist=Q4C5S4pAfAQ" frameborder="0" allowfullscreen=""></iframe>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  print(banner)
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# Mr.GrinXz deface page
def mrgrinxz():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet codename")
  codename = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter your message for the website")
  message = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<title>"""

  code2 = title

  code3 = """</title>
<meta property="og:title" content="Hacked by the GrinXz" />
<meta property="og:descrip­tion" content="Website pawned by a Gh0st. You can run but you cant hide😈" />
<meta property="og:image" content="https://­encrypted-tbn0.gstati­c.com/­images?q=tbn%3AANd9Gc­S1IgPVN-n0t3HT5PZYHt­_FPBoxl1T9zTSBaA&usq­p=CAU" />
<link href='https://­fonts.googleapis.com/­css?family=Nosifer' rel='stylesheet' type='text/css'>
<link href='https://­fonts.googleapis.com/­css?family=Iceland' rel='stylesheet' type='text/css'>
<link href="https://­fonts.googleapis.com/­css?family=Sarpanch%3­A700" rel="stylesheet">
<link href="https://­fonts.googleapis.com/­css?family=play" rel="stylesheet">

</head>
<style>
body {
color: white;
background-color: black;
}
.logo {
width:30%;
}
a {
text-decoration:none­;
color:silver;
}
h1 {
text-transform: uppercase;
font-family: Nosifer;
color: white;
text-shadow: 0 0 0.5em red, 0 0 0.5em red;
}
h2 {
font-family:courier new;
}
h3 {
font-family:courier new;
}
p {
font-family:courier new;
color:white;
}
a {
color:red;
}
.grinxz {
font-family: iceland;
}
</style>
<body ONCONTEXTMENU='retur­n false;' ONKEYDOWN='return false;' ONMOUSEDOWN='return false;'>
<div align="center">
"""
  code4 = """<img class="logo" src=" """
  code5 = img
  code6 = """ "></br></br>
<h1> <script language="JavaScript­1.2">
var message=" You have been hacked!!!"
var neonbasecolor="silve­r"
var neontextcolor="blue"
var neontextcolor2="red"
var flashspeed=100 // speed of flashing in milliseconds
var flashingletters=3 // number of letters flashing in neontextcolor
var flashingletters2=1 // number of letters flashing in neontextcolor2 (0 to disable)
var flashpause=0 // the pause between flash-cycles in milliseconds
///No need to edit below this line/////
var n=0
if (document.all||docum­ent.getElementById){
document.write('<fon­t color="'+neonbasecol­or+'">')
for (m=0;m<message.lengt­h;m++)
document.write('<spa­n id="neonlight'+m+'">­'+message.charAt(m)+­'</span>')
document.write('</­font>')
}
else
document.write(messa­ge)
function crossref(number){
var crossobj=document.al­l? eval("document.all.n­eonlight"+number) : document.getElementB­yId("neonlight"+numb­er)
return crossobj
}
function neon(){
//Change all letters to base color
if (n==0){
for (m=0;m<message.lengt­h;m++)
crossref(m).style.co­lor=neonbasecolor
}
//cycle through and change individual letters to neon color
crossref(n).style.co­lor=neontextcolor
if (n>flashingletters-1­) crossref(n-flashingl­etters).style.color=­neontextcolor2
if (n>(flashingletters+­flashingletters2)-1)­ crossref(n-flashingl­etters-flashinglette­rs2).style.color=neo­nbasecolor
if (n<message.length-1)
n++
else{
n=0
clearInterval(flashi­ng)
setTimeout("beginneo­n()",flashpause)
return
}
}
function beginneon(){
if (document.all||docum­ent.getElementById)
flashing=setInterval­("neon()",flashspeed­)
}
beginneon()
</script></h1>"""
  code7 = """<h2>Hacked By <font color="red">"""
  code8 = codename
  code9 = """</­h2>
<center> <br>"""

  code10 = """<p>"""
  code11 = message
  code12 = """</p>"""
  code13 = """ 
  <br>Follow Me On:<br><a href="" >Facebook</a> | <a href="https://­m.youtube.com/­channel/GrinXz" >Twitter</a></p>
</center><br>
<center>
<iframe width="0" height="0" src="https://­www.youtube.com/­embed/­8B-sFGfA3lM?&autoplay­=1" frameborder="0" allow="accelerometer­; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></­iframe>
</center>
</body>
<script src="https://­cdn.rawgit.com/­bungfrangki/­efeksalju/2a7805c7/­efek-salju.js" type="text/­javascript"></script>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)
  fo.write(code9)
  fo.write(code10)
  fo.write(code11)
  fo.write(code12)
  fo.write(code13)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# MR TOM deface page
def mrtom():
  os.system("clear")
  slowprint(banner)
  print("\033[1;32;49m")
  print(" Enter deface page title")
  title = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter banner image url")
  img = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Enter you leet message and codename")
  codename = input(" » ")
  print(" ")
  time.sleep(0.1)
  print(" Generate deface page (y/n)")
  choice = input(" » ")

# html code snippets
  code1 = """<html>
<head>
<meta name="viewport" content="width=devic­e-width, initial-scale=1.0">
<TITLE>"""

  code2 = title

  code3 = """</TITLE>
<style type="text/css" media="all">
*{
margin: 1;
padding:0;
}
img{
position: center;
width: 470px;
height: 450px;
</style>
</head>
<body bgCOLOR="WHITE"TEXT­="BLACK">
<MARQUEE><H1>
"""
  code4 = codename
  code5 = """</H1></MARQUEE>"""
  code6 = """<center><img src=" """
  code7 = img
  code8 = """ "/></center>
</body>
</html>"""

  if choice == "y":
	  time.sleep(3)
	  os.system("clear")
	  slowprint("\033[1;32;40m[!] Generating deface page...")
	  fo = open("deface.html","w")
	  time.sleep(5)
  elif choice == "n":
    os.system("clear")
    quit()
    exit()

  fo.write(code1)
  fo.write(code2)
  fo.write(code3)
  fo.write(code4)
  fo.write(code5)
  fo.write(code6)
  fo.write(code7)
  fo.write(code8)

  print("")
  os.system("clear")
  print(banner)
  print(" Your deface page is generated as: deface.html")
  print(" Thank you for using my simple tool.")
  fo.close()

# main function
def main():
  os.system("clear")
  slowprint(banner)
  slowprint(options)
  print("\n Choose deface page template")
  option = input(" » ")

  if option == "1" or option == "01":
    MrD347H()
  elif option == "2" or option == "02":
    gr1mr34p3r()
  elif option == "3" or option == "03":
    cch()
  elif option == "4" or option == "04":
    anonymouse()
  elif option == "5" or option == "05":
    clownsec()
  elif option == "6" or option == "06":
    mrgrinxz()
  elif option == "7" or option == "07":
    mrtom()
  elif option == "0" or option == "00":
    os.system("clear")
    quit()
    exit()

# Execute main function
if __name__ == "__main__":    
  main()
