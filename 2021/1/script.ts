import * as fs from 'fs';

let input = fs.readFileSync('input.txt','utf8')
let array = input.split('\n')
var increased = 0
var decreased = 0

//Parte 1
array.forEach((value, index)=>{
    if(array[index+1] && parseInt(value) < parseInt(array[index+1])){
        increased++
    } else{
        decreased++
    }
})

console.log("Part 1 --> increased: "+increased+" decreased: "+ decreased)

//Parte 2
var previousSum = 0
var increased = 0
var decreased = 0
for(let i=0; i<array.length; i++){
    if(i == 0){
        previousSum = parseInt(array[i])+parseInt(array[i+1])+parseInt(array[i+2])
    } else {
        let currentSum = parseInt(array[i])+parseInt(array[i+1])+parseInt(array[i+2])
        if(previousSum<currentSum) {
            increased++
        } else {
            decreased++
        }
        previousSum = currentSum
    }
}

console.log("Part 2 --> increased: "+increased+" decreased: "+ decreased)