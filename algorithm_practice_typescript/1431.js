function kidsWithCandies(candies, extraCandies) {
    var highest = Math.max.apply(Math, candies);
    return candies.map(function (candy) { return candy + extraCandies >= highest; });
}
;
var candies = [2, 3, 5, 1, 3];
var extraCandies = 3;
console.log(kidsWithCandies(candies, extraCandies));
console.log("hello");
