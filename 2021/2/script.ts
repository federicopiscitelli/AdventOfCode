import * as fs from 'fs';

let input = fs.readFileSync('input.txt','utf8')
let array = input.split('\n')
var depth = 0;
var hPosition = 0;

//Parte 1
array.forEach((value, index)=>{
    let instructions = value.split(' ')
    if(instructions[0]=="forward")
        hPosition += parseInt(instructions[1])
    if(instructions[0]=="up")
        depth -= parseInt(instructions[1])
    if(instructions[0]=="down")
        depth += parseInt(instructions[1])
})

console.log(depth*hPosition)

//Parte 2
var aim = 0
var depth = 0
var hPosition = 0

array.forEach((value, index)=>{
    let instructions = value.split(' ')
    if(instructions[0]=="forward"){
        hPosition += parseInt(instructions[1])
        depth += (aim*instructions[1])
    }
    if(instructions[0]=="up")
        aim -= parseInt(instructions[1])
    if(instructions[0]=="down")
        aim += parseInt(instructions[1])
})
console.log(depth*hPosition)