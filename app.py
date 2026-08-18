from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="google-site-verification" content="9HG5rcIRSxJskYZZRRlFvEvZhaUK770t-eZ_vq7XsoQ" />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>LOVE ROMAN ♥ PINK</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Georgia, "Times New Roman", serif;
            background:
                radial-gradient(circle at top, #4b1734 0%, #1b0914 45%, #080308 100%);
            color: white;
            min-height: 100vh;
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;

            background:
                radial-gradient(
                    circle at 20% 20%,
                    rgba(255, 80, 150, 0.10),
                    transparent 25%
                ),
                radial-gradient(
                    circle at 80% 80%,
                    rgba(255, 120, 180, 0.08),
                    transparent 25%
                );

            z-index: -1;
        }

        /* =========================
           NAVIGATION
        ========================= */

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 20px 7%;

            background: rgba(12, 4, 10, 0.82);
            backdrop-filter: blur(15px);

            border-bottom: 1px solid rgba(255, 130, 180, 0.15);
        }

        .logo {
            font-size: 23px;
            font-weight: bold;
            letter-spacing: 2px;

            color: #ff76ad;

            text-shadow:
                0 0 12px rgba(255, 80, 150, 0.7),
                0 0 30px rgba(255, 80, 150, 0.25);
        }

        nav a {
            color: #e7bfd0;
            text-decoration: none;
            margin-left: 24px;

            transition: 0.3s;
        }

        nav a:hover {
            color: #ff76ad;
        }

        /* =========================
           HERO
        ========================= */

        .hero {
            min-height: 90vh;

            display: flex;
            justify-content: center;
            align-items: center;

            text-align: center;

            padding: 70px 20px;
        }

        .hero-content {
            max-width: 900px;
        }

        .mini-title {
            color: #ff96c1;

            text-transform: uppercase;

            letter-spacing: 5px;

            font-size: 13px;

            margin-bottom: 25px;
        }

        .hero h1 {
            font-size: clamp(58px, 10vw, 120px);

            line-height: 0.9;

            margin-bottom: 30px;

            color: #fff1f7;

            text-shadow:
                0 0 20px rgba(255, 100, 170, 0.45),
                0 0 60px rgba(255, 80, 150, 0.15);
        }

        .hero h1 span {
            color: #ff63a5;
        }

        .hero p {
            max-width: 720px;
            margin: auto;

            color: #d9afbf;

            font-size: 19px;

            line-height: 1.9;
        }

        .buttons {
            margin-top: 35px;

            display: flex;

            justify-content: center;

            gap: 15px;

            flex-wrap: wrap;
        }

        button {
            border: none;

            cursor: pointer;

            padding: 15px 25px;

            border-radius: 30px;

            font-size: 15px;

            font-weight: bold;

            transition: 0.25s;
        }

        .primary {
            color: white;

            background:
                linear-gradient(
                    135deg,
                    #ff4d96,
                    #ff78b4
                );

            box-shadow:
                0 0 30px rgba(255, 70, 145, 0.35);
        }

        .primary:hover {
            transform: translateY(-4px) scale(1.03);

            box-shadow:
                0 0 45px rgba(255, 70, 145, 0.55);
        }

        .secondary {
            color: #ffe0ec;

            background: rgba(255, 255, 255, 0.05);

            border: 1px solid rgba(255, 160, 200, 0.25);
        }

        .secondary:hover {
            transform: translateY(-4px);

            border-color: #ff76ad;
        }

        #heroMessage {
            min-height: 30px;

            margin-top: 25px;

            color: #ff91bd;

            font-size: 18px;

            transition: 0.3s;
        }

        /* =========================
           SECTIONS
        ========================= */

        .section {
            padding: 100px 7%;
        }

        .title {
            text-align: center;

            margin-bottom: 55px;
        }

        .title span {
            color: #ff76ad;

            text-transform: uppercase;

            letter-spacing: 4px;

            font-size: 12px;
        }

        .title h2 {
            color: #fff1f7;

            font-size: 44px;

            margin-top: 12px;
        }

        /* =========================
           LOVE CARDS
        ========================= */

        .cards {
            display: grid;

            grid-template-columns:
                repeat(auto-fit, minmax(220px, 1fr));

            gap: 20px;
        }

        .card {
            padding: 32px;

            text-align: center;

            background:
                rgba(255, 255, 255, 0.04);

            border:
                1px solid rgba(255, 150, 190, 0.12);

            border-radius: 20px;

            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);

            border-color:
                rgba(255, 100, 165, 0.45);

            box-shadow:
                0 20px 60px rgba(255, 50, 130, 0.10);
        }

        .emoji {
            font-size: 42px;

            margin-bottom: 18px;
        }

        .card h3 {
            color: #ff86b8;

            margin-bottom: 12px;
        }

        .card p {
            color: #cdaaba;

            line-height: 1.7;
        }

        /* =========================
           LETTER
        ========================= */

        .letter {
            max-width: 820px;

            margin: auto;

            padding: 45px;

            background:
                rgba(255, 255, 255, 0.045);

            border:
                1px solid rgba(255, 150, 190, 0.15);

            border-radius: 25px;

            box-shadow:
                0 25px 70px rgba(0, 0, 0, 0.30);
        }

        .letter h3 {
            color: #ff78ad;

            font-size: 30px;

            margin-bottom: 25px;
        }

        .letter p {
            color: #dfbac9;

            font-size: 17px;

            line-height: 2;

            margin-bottom: 18px;
        }

        .signature {
            text-align: right;

            color: #ff78ad !important;

            font-weight: bold;
        }

        /* =========================
           MEMORY / INFINITY
        ========================= */

        .counter {
            text-align: center;
        }

        .counter-box {
            display: inline-block;

            min-width: 310px;

            padding: 35px 45px;

            background:
                rgba(255, 255, 255, 0.04);

            border:
                1px solid rgba(255, 150, 190, 0.15);

            border-radius: 25px;

            box-shadow:
                0 20px 50px rgba(255, 50, 130, 0.08);
        }

        .counter-number {
            color: #ff72aa;

            font-size: 100px;

            line-height: 1;

            font-weight: bold;

            text-shadow:
                0 0 25px rgba(255, 80, 150, 0.30);
        }

        .counter-label {
            color: #c9a4b5;

            margin-top: 18px;

            font-size: 16px;
        }

        /* =========================
           LAST THING
        ========================= */

        .last-thing {
            text-align: center;
        }

        #surpriseMessage {
            margin-top: 30px;

            min-height: 140px;

            color: #ff91bd;

            font-size: 20px;

            line-height: 1.8;

            transition: 0.5s;
        }

        /* =========================
           FLOATING HEARTS
        ========================= */

        .heart {
            position: fixed;

            bottom: -40px;

            pointer-events: none;

            z-index: 10;

            animation:
                floatHeart
                linear
                forwards;
        }

        @keyframes floatHeart {

            0% {
                transform:
                    translateY(0)
                    rotate(0deg);

                opacity: 0;
            }

            15% {
                opacity: 0.8;
            }

            100% {
                transform:
                    translateY(-110vh)
                    rotate(360deg);

                opacity: 0;
            }
        }

        /* =========================
           FOOTER
        ========================= */

        footer {
            padding: 35px 7%;

            text-align: center;

            color: #916c7d;

            border-top:
                1px solid rgba(255, 150, 190, 0.1);
        }

        /* =========================
           MOBILE
        ========================= */

        @media (max-width: 700px) {

            nav {
                padding: 18px 5%;
            }

            nav a {
                margin-left: 8px;

                font-size: 12px;
            }

            .section {
                padding: 70px 5%;
            }

            .letter {
                padding: 28px;
            }

            .counter-box {
                width: 100%;

                min-width: auto;
            }

            .hero p {
                font-size: 17px;
            }
        }
    </style>
</head>

<body>

<!-- =========================
     NAVIGATION
========================= -->

<nav>

    <div class="logo">
        LOVE ROMAN ♥ PINK
    </div>

    <div>

        <a href="#home">
            Home
        </a>

        <a href="#story">
            Our Love
        </a>

        <a href="#letter">
            Letter
        </a>

        <a href="#last">
            Last Thing
        </a>

    </div>

</nav>


<!-- =========================
     HERO
========================= -->

<section class="hero" id="home">

    <div class="hero-content">

        <div class="mini-title">
            Made with love by Roman
        </div>

        <h1>
            ROMAN <span>♥</span> PINK
        </h1>

        <p>
            This little corner of the internet was made especially
            for Pink, filled with our love and memories.
            <br><br>
            I made this for you so you can always remember that
            love is everywhere, even here on the internet.
        </p>

        <div class="buttons">

            <button
                class="primary"
                onclick="openHeart()"
            >
                Open My Heart ♥
            </button>

            <button
                class="secondary"
                onclick="goToLetter()"
            >
                Read My Letter
            </button>

        </div>

        <div id="heroMessage"></div>

    </div>

</section>


<!-- =========================
     OUR STORY
========================= -->

<section class="section" id="story">

    <div class="title">

        <span>
            Our Story
        </span>

        <h2>
            Things I Love About Us
        </h2>

    </div>


    <div class="cards">

        <div class="card">

            <div class="emoji">
                💗
            </div>

            <h3>
                Your Smile
            </h3>

            <p>
                Your smile can turn an ordinary moment
                into one of my favorite memories.
            </p>

        </div>


        <div class="card">

            <div class="emoji">
                🌷
            </div>

            <h3>
                Your Heart
            </h3>

            <p>
                I love your heart, your kindness,
                and all the little things that make
                you who you are.
            </p>

        </div>


        <div class="card">

            <div class="emoji">
                🌙
            </div>

            <h3>
                Our Moments
            </h3>

            <p>
                Every conversation, laugh and little
                moment becomes another memory for us.
            </p>

        </div>


        <div class="card">

            <div class="emoji">
                💍
            </div>

            <h3>
                Our Future
            </h3>

            <p>
                I don't only want memories from yesterday.
                I want many more chapters with you.
            </p>

        </div>

    </div>

</section>


<!-- =========================
     LOVE LETTER
========================= -->

<section class="section" id="letter">

    <div class="title">

        <span>
            From Roman
        </span>

        <h2>
            A Letter For Pink
        </h2>

    </div>


    <div class="letter">

        <h3>
            Dear Pink, ♥
        </h3>

        <p>
            I made this little website because sometimes
            words don't feel like enough to explain how
            important you are to me.
        </p>

        <p>
            I appreciate all the little things about us —
            the conversations, the laughs, the random moments,
            and every memory that we continue to create.
        </p>

        <p>
            I never want to take what we have for granted.
            I want to keep learning, growing, understanding,
            and choosing you.
        </p>

        <p>
            I hope we continue making memories, supporting
            each other, and protecting the love that we
            have built together.
        </p>

        <p>
            Thank you for being part of my life.
            Thank you for being you.
        </p>

        <p class="signature">

            Always yours,
            <br>

            Roman ♥

        </p>

    </div>

</section>


<!-- =========================
     MEMORY
========================= -->

<section class="section counter">

    <div class="title">

        <span>
            Our Love
        </span>

        <h2>
            Our Memory
        </h2>

    </div>


    <div class="counter-box">

        <div class="counter-number">
            ∞
        </div>

        <div class="counter-label">
            our love has no end
        </div>

    </div>

</section>


<!-- =========================
     LAST THING
========================= -->

<section
    class="section last-thing"
    id="last"
>

    <div class="title">

        <span>
            One More Thing
        </span>

        <h2>
            Last Thing
        </h2>

    </div>


    <button
        class="primary"
        onclick="surprise()"
    >
        Click
    </button>


    <div id="surpriseMessage"></div>

</section>


<!-- =========================
     FOOTER
========================= -->

<footer>
    Made with love by Roman for Pink ♥
</footer>


<script>

    /* =========================
       FLOATING HEARTS
    ========================= */

    function createHeart() {

        const heart =
            document.createElement("div");

        heart.className = "heart";

        heart.innerHTML =
            Math.random() > 0.5
                ? "♥"
                : "♡";

        heart.style.left =
            Math.random() * 100 + "vw";

        heart.style.color =
            Math.random() > 0.5
                ? "#ff5d9c"
                : "#ff9ac2";

        heart.style.fontSize =
            (15 + Math.random() * 25) + "px";

        heart.style.animationDuration =
            (5 + Math.random() * 6) + "s";

        document.body.appendChild(heart);

        setTimeout(
            () => heart.remove(),
            12000
        );
    }


    setInterval(
        createHeart,
        700
    );


    /* =========================
       OPEN MY HEART
    ========================= */

    function openHeart() {

        document.getElementById(
            "heroMessage"
        ).innerHTML =
            "I love you both, coco and baby ♥";

        for (
            let i = 0;
            i < 20;
            i++
        ) {

            setTimeout(
                createHeart,
                i * 80
            );

        }
    }


    /* =========================
       GO TO LETTER
    ========================= */

    function goToLetter() {

        document
            .getElementById("letter")
            .scrollIntoView({
                behavior: "smooth"
            });
    }


    /* =========================
       LAST THING
    ========================= */

    function surprise() {

        const message =
            document.getElementById(
                "surpriseMessage"
            );

        message.innerHTML =
            "Pink... ♥<br><br>" +

            "I love you both, coco and baby.<br>" +

            "No matter where we are,<br>" +

            "no matter how far apart we may be,<br>" +

            "I hope you always remember<br>" +

            "that a part of my heart will always belong to you.";

        for (
            let i = 0;
            i < 35;
            i++
        ) {

            setTimeout(
                createHeart,
                i * 60
            );

        }
    }

</script>

</body>
</html>
"""


@app.route("/")
def home():

    return render_template_string(HTML)

("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://pinkroman.onrender.com/</loc>
    </url>
</urlset>
"""
    return Response(xml, mimetype="application/xml")



if __name__ == "__main__":

    print()
    print("==========================================")
    print("          LOVE ROMAN ♥ PINK")
    print("==========================================")
    print("Website is starting...")
    print()
    print("Open this in your browser:")
    print("http://127.0.0.1:5000")
    print("==========================================")
    print()

    app.run(debug=True)
