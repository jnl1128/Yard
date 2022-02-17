const infoContainer = document.getElementById('preview-img-div')

const imgInput = document.getElementById('updateInfo-img')
imgInput.childNodes[2].className = 'image-container'

const imgTag = imgInput.childNodes[2].querySelector('a').href

const currImg = document.createElement('img')
currImg.className = 'preview-img'
currImg.id = 'preview-img'
currImg.src = imgTag;
currImg.style.width = '100px';
currImg.style.height = '100px';
currImg.style.border = '1px solid #fff'
currImg.style.borderRadius = '50%';
infoContainer.appendChild(currImg)

const inputNewImg = imgInput.childNodes[2].querySelectorAll('input')[1]
inputNewImg.className = 'newImg'
const newImg = document.querySelector('.newImg')

newImg.addEventListener('change', showPreview)

function showPreview(event){
  if(event.target.files.length > 0){
    const src = URL.createObjectURL(event.target.files[0]);
    const preview = document.getElementById('preview-img');
    preview.src = src;
    preview.style.display = "block";
  }
}