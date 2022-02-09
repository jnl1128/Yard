const certificates = document.querySelectorAll('.certificate-container');

function displayMusicInfo(event){
  console.log(event.target.childNodes[3])
  event.target.childNodes[3].classList.toggle('hidden');
  event.target.childNodes[1].style.filter = 'brightness(50%)'
}
function hideMusicInfo(event){
  event.target.childNodes[3].classList.add('hidden')
  event.target.childNodes[1].style.filter = 'brightness(100%)'
}
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseenter', displayMusicInfo)

});
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseleave', hideMusicInfo);

});