<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SNH48TeamXFans</title>
  {% include '_third-party/analytics/index.swig' %}
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
  <meta name="google-site-verification" content="v0OrECtdVkj5UBsT-m2uycBhubf93gLqqP49ewDOLDI" />

  <!-- Link Swiper's CSS -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.1/css/swiper.min.css">
	<!-- link rel="stylesheet" href="//css/index-separate/index.css" -->
	<link rel="stylesheet" href="/css/index-separate/all.css">

</head>

<body>
   <div class="swiper-container"> <div class="swiper-wrapper"> <div class="swiper-slide" style="background-image:url(/img/index/background1/bk1.png)"> <img src="/img/index/background1/bk1-name.png" alt class="bk1_name" style> <img src="/img/index/background1/bk1-name-pinyin.png" alt class="bk1_name_pinyin" style> <img src="/img/index/onlinearchive.png" alt class="bk_archive" style> </div><div class="swiper-slide" style="background-image:url(/img/index/background2/bk2.png)"> <img src="/img/index/background2/bk2-intro.png" alt class="bk2_intro" style> <img src="/img/index/background2/bk2-list.png" alt class="bk2_list" style> <img src="/img/index/onlinearchive.png" alt class="bk_archive" style> <button type="button" class="btn ghost-button responsive-width btn-zhibo-bk2"> <a href="/ybystream/"> 直播列表 </a> </button> </div><div class="swiper-slide" style="background-image:url(/img/index/background3/bk3.png)"> <img src="/img/index/background3/bk3-intro.png" alt class="bk3_intro" style> <img src="/img/index/onlinearchive.png" alt class="bk_archive" style> <button type="button" class="btn ghost-button responsive-width btn-budang-bk3"> <a href="/ybysource/"> 补档链接 </a> </button> </div><div class="swiper-slide" style="background-image:url(/img/index/background4/bk4.jpg); background-size:cover; background-repeat:no-repeat;"> <img src="/img/index/background4/bk4-teamx.png" alt class="bk4_teamx" style> <a href="http://www.snh48.com/member_list.html#s_team_x"> <img src="/img/index/background4/bk4-zhuye.png" alt class="bk4_zhuye" style> </a> <a href="http://weibo.com/u/5621452734"> <img src="/img/index/background4/bk4-yingyuanhui.png" alt class="bk4_yingyuanhui" style> </a> <a href="http://www.snh48.com/html/allnews/"> <img src="/img/index/background4/bk4-xinwen.png" alt class="bk4_xinwen" style> </a> <img src="/img/index/onlinearchive.png" alt class="bk_archive_l" style> <button type="button" class="btn ghost-button responsive-width btn-budang-bk4"> <a href="/teamX-show/"> 公演全集 </a> </button> </div></div><div class="swiper-pagination"></div></div>

  <!-- Swiper JS -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Swiper/4.0.1/js/swiper.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>

  <!-- Initialize Swiper -->
  <script>
    var swiper = new Swiper('.swiper-container', {
        pagination: {
                  el: '.swiper-pagination',
           clickable: true,
        },
        loop: true,
        preload: true,
        mousewheel: true,
        slideToClickedSlide: true,
    });
  </script>
</body>
</html>
