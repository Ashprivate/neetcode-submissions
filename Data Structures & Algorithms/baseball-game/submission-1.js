class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        const stack = [];
        let sum = 0;

        for (const op of operations) {
            let score;

            if (op === "+") {
                score = stack[stack.length - 1] + stack[stack.length - 2];
                stack.push(score);
            } else if (op === "D") {
                score = 2 * stack[stack.length - 1];
                stack.push(score);
            } else if (op === "C") {
                sum -= stack.pop();
                continue;
            } else {
                score = Number(op);
                stack.push(score);
            }

            sum += score;
        }

        return sum;
    }
}