const titleInput = document.querySelector('.musicTitleInput')
const artistInput = document.querySelector('.musicArtistInput')

let musicListListList = document.querySelector('.musicListList')
$(document).ready($(".musicList").empty());

function addMusicList() {
  musicListListList.style.display='block';
  let musicKeyWord = $("#songinfo").val();
  $(".musicList").empty();
  $(".musicListList").empty();
  $.ajax({
    type: "GET",
    url:
      "http://ws.audioscrobbler.com/2.0/?method=track.search&track=" +
      musicKeyWord +
      "&api_key=91921c9761d97539ea8147f4599b5f3e&format=json",
    success: function (response) {
      let musicList = response["results"]["trackmatches"]["track"];
      for (let i = 0; i < musicList.length; i++) {
        let albumTitle = musicList[i]["name"];
        let albumArtist = musicList[i]["artist"];
        getMusicHtml(albumTitle, albumArtist);
      }
    },
  });
}

function getMusicHtml(title, artist) {
  let musicHtml = `<div class="songs">
          <input name="musicChoice" class="form-check-input" type="checkbox" value=""  onclick='doOpenCheck(this)' id="musicChoice">
          <label class="form-check-label" for="musicChoice" id="musicInfo">
              ${title}
              |
              ${artist}
          </label>
      </div>`;
  $(".musicListList").append(musicHtml);
}

let registerMusicBtn = document.querySelector("#registerMusic");
registerMusicBtn.addEventListener("click", registerMusic());

function registerMusic() {
  let listedMusic = document.querySelectorAll(".songs");
  for (let i = 0; i < listedMusic.length; i++) {
    if (listedMusic[i].querySelector("#musicChoice").checked) {
      let checkedMusic = listedMusic[i];
      let musicInfo = checkedMusic.querySelector("#musicInfo").innerHTML;
      let musicTitle = musicInfo.split("|")[0].trim();
      let musicArtist = musicInfo.split("|")[1].trim();

      onClickMusic(musicTitle, musicArtist);
    }
  }
}

const onClickMusic = async (music, artist) => {
  console.log(music);
  const url = "addMusicAjax/";
  const { data } = await axios.post(url, {
    music,
    artist,
  });
  
  musicHandleResponse(data.music, data.artist);
};

const musicHandleResponse = (music, artist) => {
  const titleInput = document.querySelector("#id_music");
  const artistInput = document.querySelector("#id_artist");

  titleInput.value = music;
  artistInput.value = artist;
  
  titleInput.style.backgroundColor = 'rgba(122, 71, 204, 0.2)'
  artistInput.style.backgroundColor = 'rgba(122, 71, 204, 0.2)'
  
  musicListListList.style.display='none';
};

function doOpenCheck(chk) {
  var obj = document.getElementsByName("musicChoice");
  for (var i = 0; i < obj.length; i++) {
    if (obj[i] != chk) {
      obj[i].checked = false;
    }
  }
}

function hashTagsToArray(tags) {
  console.log("!!")
  const hashTagArray = str.split(" ");
  
  for (let i = 0; i < hashTagArray.length; i++){
    //const element = document.querySelector(`.hashTag`);
    const newDiv = document.createElement('div');
    newDiv.setAttribute("class", "hashtag--btn");
    const newText = document.createTextNode(hashTagArray[i]);
    newDiv.appendChild(newText);
    const tagDiv = document.querySelector('.feed-hashtagList');
    tagDiv.append(newDiv);
  
  }
}

function autolink() {
  var container = document.getElementsByClassName("feed-content");
  for (let i = 0; i < container.length; i++) {
    var doc = container[i].innerHTML;
    var regURL = new RegExp("(http|https|ftp|telnet|news|irc)://([-/.a-zA-Z0-9_~#%$?&=:200-377()]+)","gi");
    container[i].innerHTML = doc.replace(regURL,"<a href='$1://$2' target='_blank'>$1://$2</a>");
  }
}

autolink();