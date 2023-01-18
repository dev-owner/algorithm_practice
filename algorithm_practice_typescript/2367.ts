function arithmeticTriplets(nums: number[], diff: number): number {
    let ans = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums.includes(nums[i] + diff) && nums.includes(nums[i] + diff * 2)) {
            ans++
        }
    }
    return ans
}

function sol2(nums: number[], diff: number): number {
    let ans = 0
    let hash = new Set()

    for (let i = 0; i < nums.length; i++) {
        const currentNum = nums[i]

        if (hash.has(currentNum - diff) && hash.has(currentNum - diff * 2)) {
            ans++
        }
        hash.add(currentNum)
    }

    return ans
}

const n: number[] = [0,1,4,6,7,10]
const diff = 3

console.log(sol2(n, diff))
