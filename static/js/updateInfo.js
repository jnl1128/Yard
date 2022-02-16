const infoContainer = document.getElementById('preview-img-div')

const imgInput = document.getElementById('updateInfo-img')
imgInput.childNodes[2].className = 'image-container'

const imgTag = imgInput.childNodes[2].querySelector('a').href

const currImg = document.createElement('img')
currImg.className = 'preview-img'
currImg.id = 'preview-img'
currImg.src = imgTag;
infoContainer.appendChild(currImg)

const clearBox = imgInput.childNodes[2].querySelectorAll('input')[0]
const clearLabel = imgInput.childNodes[2].querySelector('label')
const brTag = imgInput.childNodes[2].querySelector('br')
//brTag.style.display = 'none'
clearBox.style.display = 'none'
clearLabel.style.display = 'none'
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

const d = document.createElement('div')
d.appendChild(inputNewImg)

imgInput.childNodes[2].appendChild(d)
