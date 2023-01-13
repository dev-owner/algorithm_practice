function decompressRLElist(nums: number[]): number[] {
    let result: number[] = [];

    for (let i = 0; i < nums.length; i+=2) {
        result.push(...new Array(nums[i]).fill(nums[i+1]))
    }

    return result
};


const nums = [1,2,3,4]

console.log(decompressRLElist(nums))