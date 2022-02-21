const certForm = document.querySelector('.cert-container')
const imgInput = document.getElementById('updateInfo-img')
const flipSound = document.getElementById('flip')
imgInput.childNodes[2].className = 'image-container'


imgInput.addEventListener('change', showPreview)


const titleInput = document.querySelector('#id_music');
const artistInput = document.querySelector('#id_artist');
titleInput.placeholder = '노래'
artistInput.placeholder = '아티스트'

function showPreview(event){
  if(event.target.files.length > 0){
    const src = URL.createObjectURL(event.target.files[0]);
    const currImg = document.getElementById('certificate')
    currImg.style.backgroundImage = `url(${src})`
  
  
  }
}


const addMusicBtn = document.getElementById('addMusicBtn')
addMusicBtn.addEventListener('click', addMusicList)

let list = document.querySelector('.musicListList');
const card = document.getElementById('exampleCard');
console.log(card)
card.style.display ='none'

$(document).ready(
            $('.musicList').empty()
        )

    function addMusicList() {
      list.style.display = 'block';
      card.style.display = 'none';

        let musicKeyWord = $('#songinfo').val()
        $('.musicList').empty()
        $('.musicListList').empty()
        $.ajax({
            type: 'GET',
            url: 'http://ws.audioscrobbler.com/2.0/?method=track.search&track='+musicKeyWord+'&api_key=91921c9761d97539ea8147f4599b5f3e&format=json',
            success: function (response) {
                    let musicList = response["results"]["trackmatches"]["track"];
                    for (let i = 0; i < musicList.length; i++) {
                    let albumTitle = musicList[i]["name"]
                    let albumArtist = musicList[i]["artist"]
                    getMusicHtml(albumTitle, albumArtist)
                }
            }
        })
    }

    function getMusicHtml(title, artist) {
        let musicHtml = `<div class="songs">
            <input class="form-check-input" type="checkbox" value="" id="musicChoice"  name="musicChoice" onclick='doOpenCheck(this)'>
            <label class="form-check-label" for="musicChoice" id="musicInfo">
                ${title}
                |
                ${artist}
            </label>
        </div>`
        $('.musicListList').append(musicHtml)
    }

    const registerMusicBtn = document.getElementById('registerMusic');
    registerMusicBtn.addEventListener("click", registerMusic);

    function registerMusic() {
        console.log('등록')
        let listedMusic = document.querySelectorAll(".songs");
        for (let i=0;i<listedMusic.length;i++) {
            if (listedMusic[i].querySelector("#musicChoice").checked) {
                let checkedMusic = listedMusic[i];
                let musicInfo = checkedMusic.querySelector('#musicInfo').innerHTML;
                let musicTitle = musicInfo.split('|')[0].trim();
                let musicArtist = musicInfo.split('|')[1].trim();

                onClickMusic(musicTitle, musicArtist);
            }

        }
        flipSound.play()

    }

    const onClickMusic = async (music, artist) => {
        const url = "addMusicAjax/";
        const { data } = await axios.post(url, {
        music,
        artist,
        });
        musicHandleResponse(data.music, data.artist);
    };

    const musicHandleResponse = (music, artist) => {

        
        titleInput.value = music;
        artistInput.value = artist;

        list.style.display = 'none';

        card.style.display = 'block';
        const cardMusic = document.querySelector('.example-music')
        const cardArtist = document.querySelector('.example-artist')
        cardMusic.innerText = titleInput.value;
        cardArtist.innerText = artistInput.value;
        
        
    };

    function doOpenCheck(chk) {
    var obj = document.getElementsByName("musicChoice");
    for (var i = 0; i < obj.length; i++) {
      if (obj[i] != chk) {
        obj[i].checked = false;
      }
    }
  }