class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        s = [...s];
        let map = {
            ')': "(",
            "]": "[",
            "}": "{"
        }

        for (let i=0;i<s.length;i++){
            if (map[s[i]]){
                console.log("1",map[s[i]]);
                if(stack.pop()!=map[s[i]]){
                    return false;
                }
            }else{
                stack.push(s[i]);
            }
        }

        return (stack.length?false:true);

    }
}
