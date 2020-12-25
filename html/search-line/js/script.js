const search = document.body.querySelector('#search')
const searchInput = document.body.querySelector('#search input')
const autocomplete = document.body.querySelector('#autocomplete')

searchInput.oninput = function (e) {
  for (const item of autocomplete.children) {
    item.classList.remove('visable')
  }
  const selected = autocomplete.querySelectorAll('.complete-selected')
  for (const sel of selected) {
    sel.classList.remove('complete-selected')
  }
  const query = searchInput.value
  if (query) {
    const list = Array.from(autocomplete.children).filter(x => x.textContent.indexOf(query) != -1)
    for (const comp of list) {
      comp.classList.add('visable')
    }
  }
}

searchInput.onkeydown = function (e) {
  const list = Array.from(autocomplete.querySelectorAll('.visable'))
  const selected = autocomplete.querySelector('.visable.complete-selected')
  if (list.length) {
    if (e.keyCode == 40) {
      const next = (selected && list[list.indexOf(selected)+1]) ?? list[0]
      if (selected) selected.classList.remove('complete-selected')
      next.classList.add('complete-selected')
      e.preventDefault()
    } else if (e.keyCode == 38) {
      const previous = (selected && list[list.indexOf(selected)-1]) ?? list[list.length-1]
      if (selected) selected.classList.remove('complete-selected')
      previous.classList.add('complete-selected')
      e.preventDefault()
    } else if (e.keyCode == 13 && selected) {
      autocomplete.classList.add('hidden')
      searchInput.value = selected.textContent.trim()      
      for (const item of autocomplete.children) {
        item.classList.remove('visable')
      }
      autocomplete.classList.remove('hidden')
      e.preventDefault()
    }
  }
}

search.onsubmit = function (e) {
  const selected = autocomplete.querySelector('.visable.complete-selected')
  if (selected) {
    e.preventDefault()
  }
}

autocomplete.onclick = function (e) {
  if (e.target.classList.contains('complete')) {
    autocomplete.classList.add('hidden')
    searchInput.value = e.target.textContent.trim()
    searchInput.focus()    
    for (const item of autocomplete.children) {
      item.classList.remove('visable')
    }
    autocomplete.classList.remove('hidden')
  }
}

console.log('script ended.')

