class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
         let stack = [];
         let s = 0;

           for ( let op of operations){
            console.log("op1", op);
            console.log("stackinit", stack);
                if(op === "+"){
                    let a = Number(stack.pop());
                    let b = Number(stack.pop());
                    console.log("op2", a, b);
                    let sum = a + b;
                    console.log("op3", sum);
                    stack.push(b);
                    stack.push(a);
                    stack.push(sum);
                }else if (op === "D"){
                    let temp = stack.pop();
                    stack.push(temp);
                    stack.push(2 * temp);
                }else if(op === "C"){
                    stack.pop();
                }else{
                    stack.push(Number(op));
                }
            }
 
            console.log("stackfinal", stack);
            for(let num of stack){
                s = s + num;
            }

            return s;
        
    }
}
