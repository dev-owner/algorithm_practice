function restoreString(s: string, indices: number[]): string {
    const ans: string[] = []
    for (let i = 0; i <= indices.length; i++) {
        ans[indices[i]] = s[i]
    }
    return ans.join("")
};

const s = "codeleet"
const indices = [4,5,6,7,0,2,1,3]

console.log(restoreString(s, indices))