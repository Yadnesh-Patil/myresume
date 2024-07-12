from django.test import TestCase

# Create your tests here.


'''

            <div class="card">
                <!-- <img src="/static/Images/dot.png" alt=""> -->
                <div class="card-content">
                    <h3>API CRUD operations</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad nulla maxime laborum laboriosam
                        blanditiis! Sint fuga ullam tempora ut quibusdam.</p>
                    <button class="collapsible">Read More</button>
                    <a href="" class="btn">Read More</a>
                </div>
            </div>
'''




# APP Password 
# APP NAME resumeWeb
# APP PASSWORD gefkgumeplovqddn 



    <!-- <style> -->
        <!-- /* * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;

        } */ -->



        
    <!-- </style> -->


* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
            scroll-padding-top: 70px;

        }


        body {
            background: #000;
            min-height: 100vh;
        }





        nav {
            display: flex;
            justify-content: space-around;
            align-items: center;
            height: 60px;
            background-color: rgb(247, 244, 244);
        }

        nav ul {
            margin-left: 300px;
            display: flex;
            justify-content: center;
        }

        nav ul li {
            display: flex;
            margin: 0 23px;
        }

        nav ul li a {
            /* font-family: cursive; */
            font-family: "Gill Sans Extrabold", sans-serif;
            text-decoration: none;
            font-weight: 900;
            color: rgb(33, 32, 32);
            font-size: 1.4rem;

        }


        nav ul li a:hover {
            color: #ff8000;
            /* font-size: 1.02rem; */
        }

        .left {
            font-family: "Gill Sans Extrabold", sans-serif;
            font-size: 1.4rem;
            font-weight: 900;
            font-size: 1.9rem;
            color: rgb(74, 36, 170);
            padding: 0%;
            margin: -5%;
        }


        /* Main Body */

        .firstsection {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin: 150px 0;
            padding-top: 150px;
            margin-top: 100px;
        }

        .firstsection>div {
            /* background-color: red; */
            width: 30%;
        }

        .leftsection {
            /* background-color: red; */
            font-size: 3.5rem;
            /* width: 50%; */
        }


        .leftsection .buttons {
            padding: 52px 0;
            text-decoration: none;
        }


        .leftsection .buttons a {
            /* padding: 52px 0; */
            text-decoration: none;
            color: rgb(247, 244, 244);


        }

        .leftsection .btn {
            padding: 12px;
            /* font-family: "Gill Sans Extrabold", sans-serif; */
            font-family: "fantasy";

            color: rgb(247, 244, 244);
            border: 2px solid #8e43e7;
            background-color: #8e43e7;
            border-radius: 6px;
            font-size: 20px;
            cursor: pointer;
        }


        .rightsection img {
            width: 50%;
            border-radius: 40%;
        }

        .purple {
            color: #8e43e7;
        }

        .gray {
            color: gray;
        }

        #element {
            color: #8e43e7;
        }


        /* about section */

        .about {
            background-color: rgb(247, 244, 244);
            max-width: 100vw;
            margin: auto;
            /* height: 80vh; */
            display: flex;
        }


        .imgdiv {
            margin-right: -55%;
        }

        .aboutimg {
            border-radius: 20%;
            width: 20%;
            padding: 5% 0%;
            margin-left: 8%;

        }




        .aboutme {
            margin-top: 7%;
            padding-right: 10%;
            /* position: relative; */

        }



        .abouthead h5 {
            color: #8c89a2;
            font-weight: 600;
            font-size: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
            padding-bottom: 1vw;
        }


        .short h1 {
            padding-bottom: 1vw;
            text-align: justify;

        }

        .mypara p {
            letter-spacing: 1px;
            text-align: justify;
            font-size: 20px;
            font-size: larger;
        }

        .socialmedia {
            display: flex;
        }

        .socialmedia a img {
            width: 3vw;
            margin-top: 2vw;
            margin-right: 1vw;
        }


        .resume {
            max-width: 100vw;
            border: 1px solid #fff ;

            
        }

        .resume button {
            width: 100vm;
        }

        .resume button a {
            text-decoration: none;
            color: rgb(74, 36, 170);
        }






        /* RESUME PAGE */

        .resumepage {
            background-color: rgb(247, 244, 244);
            max-width: 100vw;

        }

        .resumepage h2 {

            border-bottom: 5px solid #ff8000;
            position: absolute;
            right: 45%;
            margin-top: 3vw;
            padding-bottom: 15px;
            letter-spacing: 1px;
            font-weight: 900;
            font-family: "Lucida Console", Courier, monospace;
        }

        .objective {
            text-align: center;
            position: absolute;
            padding: 0 20%;
            margin-top: 5vw;
            letter-spacing: 1px;
        }

        .objective p {
            margin-bottom: 15px;
            padding: 30px;
            font-weight: 400;
            font-family: "Gill Sans Extrabold", sans-serif;

        }


        .details {
            display: flex;
            max-width: 100vw;
            margin-top: 250px;
            letter-spacing: 1px;
            text-align: left;
            padding-left: 8vw;
        }


        .details .work {
            border-left: 5px solid #ff8000;
            width: 45%;
            padding: 0 15px;
        }

        .details .work h3 {
            margin-top: 3vw;
            padding-bottom: 15px;


        }


        .details .work p {
            padding: 10px 0;
            text-align: justify;
        }


        .details .education {
            width: 45%;
            border-left: 5px solid #ff8000;
            padding-left: 15px;
        }


        .details .education h3 {
            font-size: large;
            margin-top: 3vw;
            padding-bottom: 15px;

        }








        /* Projects */



        .projectspage {
            background-color: rgb(247, 244, 244);
            max-width: 100vw;
        }

        .projectspage h2 {
            border-bottom: 5px solid #ff8000;
            position: absolute;
            right: 45%;
            margin-top: 3vw;
            padding-bottom: 15px;
            letter-spacing: 1px;
            font-weight: 900;
            font-family: "Lucida Console", Courier, monospace;
        }



        .projects {
            margin: 50px 0;

        }



        .card-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 100px;

        }

        .card {
            width: 450px;
            background-color: #f0f0f0;
            border-radius: 8px;
            /* overflow: hidden; */
            /* overflow-y: scroll; */
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
            margin: 40px 20px;
            height: 200px;
        }


        .card img {
            width: 100%;
            height: auto;
        }

        .card-content {
            padding: 16px;

        }

        .card-content h3 {
            font-size: 28px;
            margin-bottom: 8px;
        }

        .card-content p {
            color: #666;
            font-size: 15px;
            line-height: 1.3;
            height: 4vw;

        }


        .card-content .btn {
            display: inline-block;
            padding: 8px 16px;
            /* background-color: #8e43e7; */
            text-decoration: none;
            border-radius: 8px;
            margin-top: 16px;
            color: #8e43e7;
            border: 1px solid #8e43e7;
        }


        .card-content .btn:hover {
            background-color: #8e43e7;
            color: #fff;
        }


        .contact {
            background-color: rgb(247, 244, 244);
            max-width: 100vw;
        }


        .contact h2 {
            border-bottom: 5px solid #ff8000;
            position: absolute;
            right: 45%;
            margin-top: 3vw;
            padding-bottom: 15px;
            letter-spacing: 1px;
            font-weight: 900;
            font-family: "Lucida Console", Courier, monospace;

        }



        .card-contact {
            width: 400px;
            background-color: #f0f0f0;
            border-radius: 8px;
            /* overflow: hidden; */
            /* overflow-y: scroll; */
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
            margin: 150px 10px;
            height: 250px;
        }

        .card-contact:hover {
            border: 1px solid #ff8000;
            color: #ff8000;
        }

        .card-content-contact {
            padding: 10px 0;
            text-align: center;
        }

        .card-content-contact h3 {
            padding-bottom: 10px;
            letter-spacing: 1px;
            font-size: x-large;
        }




        .card-content-contact h5 {
            font-size: large;
            color: #666;
        }



        /* .contactimg {
            border: 5px solid #ff8000;
            border-radius: 20%;
            width: 20%;
            padding: 15% 40%;
        } */

        .contactimg {
            margin-left: 40%;
            margin-top: 10%;
            border-radius: 20%;
            width: 60px;
            height: 25%;
        }

        .collapsible {
            margin: 20px 0;
            padding: 12px;
            /* font-family: "Gill Sans Extrabold", sans-serif; */
            font-family: "fantasy";
            /* width: 10vw; */
            color: #8e43e7;
            border: 1px solid #8e43e7;
            background-color: rgb(247, 244, 244);
            border-radius: 6px;
            font-size: 15px;
            height: 40px;
            cursor: pointer;
        }


        .collapsible:hover {
            color: rgb(247, 244, 244);
            background-color: #8e43e7;

        }


        .contentc {
            padding: 0 18px;
            display: none;
            overflow: hidden;
            background-color: #f1f1f1;
            border: outset;
        }

        .emmap {
            padding: 30px 12%;
            margin-top: -100px;
            display: flex;
        }

        .emmap iframe {
            border: 5px solid #fff;
            box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
            border-radius: 25px;
        }

        .emmap iframe:hover {
            border: 5px solid #f0f0f0;

        }






        .contactform {
            /* border: 1px solid #aaa; */
            margin: 0 20px;
            border-radius: 25px;
            box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        }





        form .form-element {
            margin: 15px 20px;

        }


        .form-content {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
        }



        .form-element input[type="text"] {
            margin-top: 5px;
            display: block;
            /* width: 100%; */
            width: 270px;
            padding: 10px;
            outline: none;
            border: 1px solid #aaa;
            border-radius: 5px;
        }

        .form-element textarea {
            margin-top: 5px;
            display: block;
            /* width: 94%; */
            padding: 10px;
            outline: none;
            border: 1px solid #aaa;
            border-radius: 5px;
        }


        .form-element button {
            width: 100%;
            height: 40px;
            border: none;
            outline: none;
            font-size: 16px;
            font-weight: 900;
            background: #8e43e7;
            color: #fff;
            border-radius: 10px;
            cursor: pointer;
        }




        .form-element button:hover {
            background-color: #fff;
            color: #8e43e7;
            border: 1px solid #8e43e7;
        }






        /* StICKY NAVBAR */


        header {
            position: fixed;
            background-color: rgb(247, 244, 244);
            top: 0;
            left: 0;
            width: 100%;
            height: 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.6s;
            padding: 40px 100px;
            z-index: 100000;
        }

        header.sticky {
            padding: 50px 100px;
            background: #fff;
        }

        header .logo {
            position: relative;
            text-decoration: none;
            letter-spacing: 2px;
            transition: 0.4s;
            font-family: cursive;
            font-weight: 900;
            font-size: 1.9rem;
            color: rgb(74, 36, 170);

        }

        header ul {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        header ul li {
            position: relative;
            list-style: none;


        }

        header ul li a {
            position: relative;
            margin: 0 25px;
            letter-spacing: 2px;
            font-size: large;
            transition: 0.5s;
            font-family: "Gill Sans Extrabold", sans-serif;
            text-decoration: none;
            font-weight: 900;
            color: rgb(33, 32, 32);
            font-size: 1.0rem;

        }


        /* .banner{
            position: relative;
            width: 100%;
            height: 100vh;
            background-size: cover;
        } */


        header.sticky .logo {
            color: #000;
        }



        header.sticky ul li a {
            color: #000;
        }


        header ul li a:hover {
            color: #ff8000;
        }





        /* servicePage */

        .serv {
            /* width: 100vw; */
            width: 100%;

            /* background-color: rgb(247, 244, 244); */
        }

        .serv h2 {
            border-bottom: 5px solid #ff8000;
            position: absolute;
            right: 45%;
            margin-top: 1vw;
            padding-bottom: 15px;
            letter-spacing: 1px;
            font-weight: 900;
            font-family: "Lucida Console", Courier, monospace;
        }


        .servcard-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 100px;

        }

        .servcard {
            width: 500px;
            background-color: #f0f0f0;
            border-radius: 8px;
            /* overflow: hidden; */
            /* overflow-y: scroll; */
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
            margin: 120px 10px;
            height: 300px;
        }


        .servcard:hover {
            border: 1px solid #ff8000;
            color: #ff8000;
        }



        .card-content-serv {
            padding: 16px;
        }


        .card-content-serv h3 {
            font-family: cursive;
            text-align: left;
            font-weight: 900;
            font-size: x-large;
            margin: 20px 0;
        }


        .card-content-serv p {

            font-size: larger;
            color: #666;
            font-family: cursive;
        }


        .card-content-serv img {
            width: 50px;
        }