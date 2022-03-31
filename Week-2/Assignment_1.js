
//week-2 assignment 1

//part 1

function max(numbers) {
    var max_num = numbers[0];
    for (let x of numbers) {
        //console.log(x);
        if (x > max_num) {
            max_num = x;  
            //console.log("------------");
        }
    }
    return max_num;
}

console.log(max([1, 2, 4, 5])); // should print 5
console.log(max([5, 2, 7, 1, 6])); // should print 7

//part 2 V1

function findPosition(numbers, target) {
    let pos = -1; //position 起始值  if not find return -1
    let counter = 0; //紀錄目前變數 y 在 list 位置
    for (let y of numbers) {
        if (y === target) {
            pos = counter;
            return pos;
        }
        else {
            counter = counter + 1;
        }
    }
    return pos;
}

console.log(findPosition([5, 2, 7, 1, 6], 5)); // should print 0
console.log(findPosition([5, 2, 7, 1, 6], 7)); // should print 2
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7)); // should print 2 (the first one)
console.log(findPosition([5, 2, 7, 1, 6], 8)); // should print -1

//part 2 V2

function findPosition(numbers, target) {
    let pos = -1;
    for (let j = 0; j < numbers.length;j++) { //變數j 為 list 位置
        if (numbers[j] === target) {
            pos = j;
            return pos;
        }
    }
    return pos;
}

console.log(findPosition([5, 2, 7, 1, 6], 5)); // should print 0
console.log(findPosition([5, 2, 7, 1, 6], 7)); // should print 2
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7)); // should print 2 (the first one)
console.log(findPosition([5, 2, 7, 1, 6], 8)); // should print -1