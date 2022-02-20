function shareTwitter() {
  var sendText = "야드Yard"; // 전달할 텍스트
  var sendUrl = "http://127.0.0.1:5500/"; // 전달할 URL
  window.open("https://twitter.com/intent/tweet?text=" + sendText + "&url=" + sendUrl);
}

function shareFacebook() {
  var sendUrl = "http://127.0.0.1:5500/"; // 전달할 URL
  window.open("http://www.facebook.com/sharer/sharer.php?u=" + sendUrl);
}

