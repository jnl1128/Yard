const tagBtn = document.getElementById("tag-list-btn")
const tagList = document.getElementById('tag-list')

const feedContainer = document.getElementById('feed-list')

console.log(tagList)
function toggleTagList(){
  tagBtn.classList.toggle('open')
  tagList.classList.toggle('tagClose')
  feedContainer.classList.toggle('small')
}

tagBtn.addEventListener('click', toggleTagList)