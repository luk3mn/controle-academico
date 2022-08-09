let open = document.querySelector('.open-menu')
let close = document.querySelector('#close-menu')


open.addEventListener("click", () => {
    document.querySelector('.menu-modal').classList.remove('hidden')
})

close.addEventListener("click", () => {
    document.querySelector('.menu-modal').classList.add('hidden')
})