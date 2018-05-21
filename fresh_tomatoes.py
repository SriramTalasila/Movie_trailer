#!/usr/bin/env python
import webbrowser
import os
import re


mainpage_head = '''
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Movie</title>
  <link rel="stylesheet"
  href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet"
  href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
</head>
<style>
  .demo-card-image.mdl-card {
    width: 356px;
    height: 356px;
    background: url('../assets/demos/image_card.jpg') center / cover;
  }

  .demo-card-image>.mdl-card__actions {
    height: 52px;
    padding: 16px;
    background: rgba(0, 0, 0, 0.2);
  }

  .demo-card-image__filename {
    color: #fff;
    font-size: 14px;
    font-weight: 500;
  }

  main {
    padding: 2% 5% 0 5%;
  }

  .mdl-dialog {
    width: 490px;
  }


  @media only screen and (max-width:1160px) {
    .mdl-cell {
      width: 45%;
    }
    img {
      width: 320px;
      height: 370px;

    }
    main {
      padding-left: 10%;
    }
  }

  @media only screen and (min-width:550px) and (max-width:850px) {
    .mdl-cell {
      width: 100%;
    }
    main {
      padding: 2% 10% 0 10%;
    }

  }

  @media only screen and (max-width:550px) {
    .mdl-cell {
      width: 100%;
    }
    img {
      width: 280px;
      height: 320px;
    }
    main {
      padding-left: 8%;
    }
  }

  #ucoming {
    display: none;
  }
</style>

<body>
  <!-- Always shows a header, even in smaller screens. -->
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <!-- Title -->
        <span class="mdl-layout-title">Movie Trailer</span>
        <!-- Add spacer, to align navigation to the right -->
        <div class="mdl-layout-spacer"></div>
        <!-- Navigation. We hide it in small screens. -->
        <nav class="mdl-navigation ">
          <form action="#">
            <div
            class="mdl-textfield mdl-js-textfield mdl-textfield--expandable">
              <label class="mdl-button mdl-js-button mdl-button--icon"
              for="sample6">
                <i class="material-icons">search</i>
              </label>
              <div class="mdl-textfield__expandable-holder">
                <input class="mdl-textfield__input" type="text" id="sample6">
                <label class="mdl-textfield__label"
                for="sample-expandable">Expandable Input</label>
              </div>
            </div>
          </form>
        </nav>
      </div>
    </header>
    <div class="mdl-layout__drawer">
      <span class="mdl-layout-title">Movie Trailers</span>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Top Rated</a>
        <a id="uc" class="mdl-navigation__link" href="#">Up Coming</a>

      </nav>
    </div>
    <main class="mdl-layout__content">
      <div class="page-content">
        <!-- Your content goes here -->
        <div id="trated">
          <h3>Top Rated:</h3>
          <div class="mdl-grid">
'''

# body content
remain_content = '''
   </div>
        </div>

      </div>
    </main>

    <dialog class="mdl-dialog">
      <h4 id="dtitle" class="mdl-dialog__title"></h4>
      <div class="mdl-dialog__content">
        <iframe width="560px" height="315px"
        src="" frameborder="0" allow="autoplay;
        encrypted-media" allowfullscreen></iframe>
      </div>
      <div class="mdl-dialog__actions">
        <button type="button" class="mdl-button close">close</button>
      </div>
    </dialog>
  </div>
</body>
<script>
  var dialog = document.querySelector('dialog');
  var showDialogButton = document.querySelector('#show-dialog');
  if (!dialog.showModal) {
    dialogPolyfill.registerDialog(dialog);
  }
  dialog.querySelector('.close').addEventListener('click', function () {
    dialog.close();
    document.getElementsByTagName("iframe")[0].setAttribute("src", "");
  });

  function loadTrailer(title, key) {
    dialog.showModal();
    var url = "https://www.youtube.com/embed/";
    url += key;
    console.log(url);
    document.getElementsByTagName("iframe")[0].setAttribute("src", url);
    document.getElementById("dtitle").innerHTML = title;

  }
  document.getElementById("uc").addEventListener("click", function () {
    document.getElementById("ucoming").style.display = "block";
    document.getElementById("trated").style.display = "none";
  })
</script>

</html>
'''

cinema_content = '''
  <div class="mdl-cell mdl-cell--4-col">
              <div class="mdl-card ">
                <div class="mdl-card">
                  <img onclick="loadTrailer('{mov_title}',
                  '{mov_link}');" src="{mov_img}"
                    width="300" height="350" border="0" alt="" style="">
                  <div style="text-align:center;">
                    {mov_title}
                  </div>
                </div>
              </div>
   </div>
'''


def create_cinema_tile_content(allmovies):
    content = ""
    for movie in allmovies:
        content += cinema_content.format(
            mov_title=movie.m_title,
            mov_img=movie.banner,
            mov_link=movie.trailer_link
        )
    return content


def open_movies_page(all_movies):
    op_file = open('index.html', 'w')

    render_content = create_cinema_tile_content(all_movies)
    op_file.write(mainpage_head+render_content+remain_content)
    op_file.close()

    urls = os.path.abspath(op_file.name)
    webbrowser.open('file:///'+urls, new=2)
