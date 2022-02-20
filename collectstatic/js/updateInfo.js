const infoContainer = document.getElementById('preview-img-div')

const imgInput = document.getElementById('updateInfo-img')
imgInput.childNodes[2].className = 'image-container'

let imgTag = imgInput.childNodes[2].querySelector('a')
if (imgTag === undefined || imgTag === null){
  imgTag = 'https://picsum.photos/100/100'
  const inputNewImg = imgInput.childNodes[2].querySelector('input')
  inputNewImg.className = 'newImg'
}else{
  imgTag = imgTag.href
  const inputNewImg = imgInput.childNodes[2].querySelectorAll('input')[1]
  inputNewImg.className = 'newImg'
}

const newImg = document.querySelector('.newImg')
newImg.addEventListener('change', showPreview)
const currImg = document.createElement('img')
currImg.className = 'preview-img'
currImg.id = 'preview-img'
currImg.src = imgTag;
currImg.style.width = '100px';
currImg.style.height = '100px';
currImg.style.border = '1px solid #fff'
currImg.style.borderRadius = '50%';
infoContainer.appendChild(currImg)





function showPreview(event){
  if(event.target.files.length > 0){
    const src = URL.createObjectURL(event.target.files[0]);
    console.log(src)
    const preview = document.getElementById('preview-img');
    preview.src = src;
    preview.style.display = "block";
  }
}

