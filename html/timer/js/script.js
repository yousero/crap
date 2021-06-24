const timer = document.body.querySelector('#timer')

let startTime
let endTime
let timerID

const update = function () {
  let time = endTime - new Date()

  if (time < 0) {
    clearInterval(timerID)
    time = 0
  }

  const minutes = Math.floor(time / 1000 / 60)
  const seconds = Math.ceil((time / 1000) % 60)

  timer.value = ''

  if (time) {
    if (minutes) {
      if (minutes < 10) {
        timer.value += '0'
      }
      timer.value += String(minutes) + ':'
    }

    if (minutes && seconds < 10) {
      timer.value += '0'
    }
    timer.value += String(seconds)
  }
}

timer.addEventListener('focus', function () {
  clearInterval(timerID)
})

timer.addEventListener('change', function () {
  const input = timer.value.split(':')
  const time =
    (input.length == 2
      ? parseInt(input[0]) * 60 + parseInt(input[1])
      : parseInt(input[0])) * 1000
  if (time) {
    startTime = new Date()
    endTime = new Date(startTime)
    endTime.setMilliseconds(endTime.getMilliseconds() + time)
    timerID = setInterval(update, 1000)
  }
})
