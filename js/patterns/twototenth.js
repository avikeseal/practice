//In this program we will calculate
//and show the value of 2^10:

//we will use two bindings:
//one to keep track of our result
//one to count often we multiplied this result by 2

let result  = 1;
//good idea to count from 0:
let counter = 0;

//the loop tests whether the second binding 
//has reached 10 yet
//and if not updates both bindings:
while (counter < 10) {
    result *= 2;
    counter += 1;
}

console.log(result);