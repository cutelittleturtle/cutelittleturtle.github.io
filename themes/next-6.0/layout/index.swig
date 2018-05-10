<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>SNH48TeamXFans
    </title>
    {% include '_third-party/analytics/index.swig' %}
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
    <meta name="google-site-verification" content="v0OrECtdVkj5UBsT-m2uycBhubf93gLqqP49ewDOLDI" />
    <!-- Link Swiper's CSS -->
    <link rel="stylesheet" href="/css/index-separate/swiper-4.0.1.min.css">
    <link rel="stylesheet" href="/css/index-separate/all.css">
  </head>
  <body>
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <div class="swiper-slide" style="background-image:url(/img/index/teamX.jpg); background-size:cover; background-repeat:no-repeat;">
          <img src="/img/index/background4/bk4-teamx.png" alt class="bk4_teamx" style>
          <img src="/img/index/onlinearchive.png" alt class="bk_archive_l" style>
            <a href="/teamX-show/" class="btn ghost-button responsive-width btn-budang-bk4">
		          视频补档
            </a>
        </div>

        <div class="swiper-slide" style="background-image:url(/img/index/电灯胆.jpg); background-size:cover; background-repeat:no-repeat;">
          <img src="/img/index/onlinearchive.png" alt class="bk_archive_l" style>
            <a href="/teamX-cp/" class="btn ghost-button responsive-width btn-budang-bk2">
		          CP全集
            </a>
        </div>

      </div>

      <div class="swiper-pagination"></div>
    </div>
    <!-- Swiper JS -->
    <script src="/js/swiper-4.0.1.min.js"></script>
    <! -- script src="/js/jquery-3.2.1.js" -->
    <!-- Initialize Swiper -->
    <script>
      var swiper = new Swiper('.swiper-container', {
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        }
        ,
        direction: "vertical",
        loop: true,
        preload: true,
        mousewheel: true,
        slideToClickedSlide: true,
      }
      );
    </script>
  </body>
</html>

