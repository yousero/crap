const readline = require('readline')

function parse(text) {
  const tokens = text.replace(/\s/g, '').match(/(\d+\.?\d*|[+\-*/])/g) || []
  
  if (tokens.length === 0) return 0

  const parsedTokens = tokens.map(token => 
    isNaN(token) ? token : parseFloat(token)
  )

  return parsedTokens
}

function exec(tokens) {  
  for (let i = 0; i < tokens.length; i++) {
    if (['*', '/'].includes(tokens[i])) {
      const left = tokens[i - 1]
      const operator = tokens[i]
      const right = tokens[i + 1]
      let result = operator === '*' ? left * right : left / right

      tokens.splice(i - 1, 3, result)
      i -= 2
    }
  }

  let result = tokens[0]
  for (let i = 1; i < tokens.length; i += 2) {
    const operator = tokens[i]
    const right = tokens[i + 1]
    result = operator === '+' ? result + right : result - right
  }

  return result
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: ' > '
})

rl.prompt()

rl.on('line', (input) => {
  if (input.toLowerCase() === 'exit') {
    rl.close()
  }
  const result = exec(parse(input))
  console.log(result)
  rl.prompt()
}).on('close', () => {
  process.exit(0)
})
