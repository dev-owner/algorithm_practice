function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const highest = Math.max(...candies);
    return candies.map(candy => candy +extraCandies >= highest)
}

const candies = [2,3,5,1,3]
const extraCandies = 3

console.log(kidsWithCandies(candies, extraCandies));
