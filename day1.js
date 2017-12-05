import fs from 'fs'

/**
 * Split a string into numbers
 * @param {string} str The string to split into numbers
 * @return {Array} result An array of numbers
 */
const getNumbersFromString = str => str.trim().split('').map(Number)

/**
 * Get an item from a circular array (the first element is rigth after the last one)
 * @param {Array} array An array of items
 * @param {number} index The given position (could be greater than array length)
 * @return {*} result The returned item
 */
const getItem = (array, index) => {
  return array[index % array.length]
}

/**
 * Whether an element matches the one n steps forward
 * @param {number} n The number of steps to use to find the element to compare
 * @param {*} element The current element
 * @param {number} index The current position in the array
 * @param {Array} array An array of items
 * @return {boolean} result Whether the items match
 */
const isRepeated = (n, element, index, array) => {
  return element === getItem(array, index + n)
}

/**
 * Sum every number of an array
 * @param {Array} array An array of numbers
 * @return {number} result The result of the sum
 */
const sumArrayNumbers = array => array.reduce((a, b) => a + b, 0)

// Read file
fs.readFile('day1.txt', 'utf8', (err, data) => {
  if (err) {
    throw err
  }
  const numbers = getNumbersFromString(data)
  const jump = numbers.length / 2
  const repeatedNumbers = numbers.filter(isRepeated.bind(null, jump))
  const result = sumArrayNumbers(repeatedNumbers)

  console.log(result)
})
