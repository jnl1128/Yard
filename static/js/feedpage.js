const tagBtn = document.getElementById("tag-list-btn")
const tagList = document.getElementById('tag-list')

const feedContainer = document.getElementById('feed-list')

function toggleTagList(){
  tagBtn.classList.toggle('open')
  tagList.classList.toggle('tagClose')
  feedContainer.classList.toggle('small')
}

tagBtn.addEventListener('click', toggleTagList)

const feedForm = document.getElementById('feedForm')
const feedBody = feedForm.querySelector('.modal-body')
feedBody.style.display = 'flex'
feedBody.style.flexDirection='column'
const feedFormB = document.querySelector('.post-form')
const musicFeed = document.querySelector('.searchDiv')
musicFeed[0].classList.add('form-white-btn')

const musicTitle = feedFormB.childNodes[3]
const musicArtist = feedFormB.childNodes[5]
const musicTitleInput = musicTitle.querySelector('input')
const musicArtistInput = musicArtist.querySelector('input')
musicTitleInput.classList.add('form-white-btn')
musicTitleInput.classList.add('musicTitleInput')
musicArtistInput.classList.add('form-white-btn')
musicArtistInput.classList.add('musicArtistInput')

const ptag = feedFormB.querySelectorAll('p')
const tagSelection = ptag[2].querySelector('select')
ptag[2].style.marginBottom = '1rem'
tagSelection.style.width = '100%';
tagSelection.style.borderRadius = '0.5rem';
tagSelection.style.border = '0.1rem solid black'
tagSelection.style.padding = '0.5rem'
tagSelection.style.boxShadow = '0px 4px 4px 0px rgba(0, 0, 0, 0.25)';
const tagOptions = ptag[2].querySelectorAll('option')
tagOptions.forEach((option)=>{
  option.style.fontSize = '1.2rem'
})
ptag[3].style.display= 'flex'
ptag[3].style.flexDirection = 'column'


ptag[4].style.display= 'flex'
ptag[4].style.flexDirection = 'column'
ptag[4].style.marginBottom = '1rem'
ptag[5].style.marginBottom = '1rem'
const hashTagInput = ptag[3].querySelector('input')
//hashTagInput.classList.add('form-white-btn')
hashTagInput.style.width = '100%'

const textarea = document.querySelector('textarea')
textarea.style.borderRadius = '0.5rem';
textarea.style.border = '0.1rem solid black'
textarea.style.padding = '0.5rem'
textarea.style.boxShadow = '0px 4px 4px 0px rgba(0, 0, 0, 0.25)';
