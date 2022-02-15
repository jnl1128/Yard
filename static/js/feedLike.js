const likeButtons = document.querySelectorAll(".likeButton")

likeButtons.forEach(function (button) {
  button.addEventListener("click", (event) => {
    const feedId = event.target.dataset.id

    axios.get(`/search/${feedId}/like/`).then((response) => {
      document.querySelector(`#like-count-${feedId}`).innerText =
        response.data.count

      if (response.data.liked) {
        event.target.classList.remove("far")
        event.target.classList.add("fas")
      } else {
        event.target.classList.remove("fas")
        event.target.classList.add("far")
      }
    })
  })
})
