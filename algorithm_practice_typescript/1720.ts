
function decode(encoded: number[], first: number): number[] {
    const ans = [first];
    for (const i of encoded) {
        const last = ans[ans.length - 1];
        ans.push(last ^ i);
    }
    return ans;
};

function sol2(encoded: number[], first: number): number[] {
    const ans = [first];
    for (let i = 0; i < encoded.length; i++) {
        ans.push(ans[i] ^ encoded[i])
    }
    return ans;
};

const encoded = [1,2,3]
const first = 1

console.log(sol2(encoded, first))
