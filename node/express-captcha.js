const express = require('express')
const svgCaptcha = require('svg-captcha')

const app = express()
const port = 3000

app.get('/captcha', (req, res) => {
    const captcha = svgCaptcha.create()
    req.session.captcha = captcha.text
    res.type('svg')
    res.status(200).send(captcha.data)
})

app.get('/validate', (req, res) => {
    const userInput = req.query.input
    if (userInput === req.session.captcha) {
        res.send('ok')
    } else {
        res.send('wrong')
    }
})

app.listen(port, () => {
    console.log(`endpoint at http://localhost:${port}`)
})
