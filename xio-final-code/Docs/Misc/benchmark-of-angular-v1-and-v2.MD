Benchmark of Angular 1 Vs Angular 2
-----------------------------------

Angular 2 is not the upgrade of angular 1. Angular 2 is completely rewritten.

### Performance improvements

Angular 2 is using Hierarchical Dependency Injection system which is major performance booster. Angular 2 implements unidirectional tree based change detection which again increases performance . As per ng-conf meetup, angular 2 is 5 times faster as compared to angular 1.

### Choice for languages.

Angular 2 provides more choice for languages. We can use any of the languages from ES5, ES6, TypeScript or Dart to write Angular 2 code. Where, Angular 1.x has ES5, ES6, and Dart. Using of TypeScript is a great step as TypeScript is awesome way to write JavaScript.

### Component-Based

Angular 2 implements web standards like components, and it provides better performance than Angular 1.

Angular 2 is entirely component based. Controllers and $scope are no longer used. They have been replaced by components and directives. Components are directives with a template. 

### Duration in milliseconds (Slowdown = Duration / Fastest)

| Tables        | angular v1.5.8           | angular v2.2.1  |
| ------------- |-----:| -----:|
| Duration for creating 1000 rows after the page loaded.      | 258.39 +- 4.65 (2.05) | 176.36 +- 4.67 (1.40) |
| Replace all rows duration for updating all 1000 rows of the table (with 5 warmup iterations).      | 251.32 +- 5.35 (4.66)      |   178.76 +- 3.85 (3.31) |
| Partial update Time to update the text of every 10th row (with 5 warmup iterations).| 11.23 +- 0.36 (1.00)      |    9.17 +- 0.52 (1.00) |
| Select row Duration to highlight a row in response to a click on the row. (with 5 warmup iterations). | 8.16 +- 2.90 (1.00) |5.35 +- 1.07 (1.00) |
|Swap rows time to swap 2 rows on a 1K table. (with 5 warmup iterations).|12.80 +- 0.44 (1.00)| 11.73 +- 0.26 (1.00)|
|Remove row duration to remove a row. (with 5 warmup iterations).| 54.13 +- 3.40 (1.49) | 50.59 +- 1.24 (1.40) |
|Create many rows duration to create 10,000 rows|2247.40 +- 20.05 (1.85)| 1776.01 +- 19.21 (1.46)|
|Append rows to large table duration for adding 1000 rows on a table of 10,000 rows.| 388.07 +- 4.59 (1.66)| 278.94 +- 3.75 (1.19)|
|Clear rows Duration to clear the table filled with 10.000 rows.| 650.28 +- 29.54 (3.40) | 320.76 +- 5.81 (1.68)|
|Clear rows a 2nd time Time to clear the table filled with 10.000 rows. But warmed up with only one iteration.| 1388.19 +- 21.56 (7.27)| 311.20 +- 6.44 (1.63)|
|slowdown geometric mean|2.01|1.41|

### Memory allocation in MBs
| | angular v1.5.8| angular v2.2.1|
| --------- | ---------- | ------- |
| ready memory Memory usage after page load.| 5.15 +- 0.26 (1.89) | 5.45 +- 0.14 (2.00) |
| run memory Memory usage after adding 1000 rows.| 14.80 +- 0.68 (3.05)| 11.51 +- 0.44 (2.37) |

### Conclusion:

We can consider this as a major upgrade from Angular 1. Angular 2 has very powerful routes. The Angular 2 Router will only load components when it absolutely needs them. Kind of partial loading which is a great feature I think. Angular 2 is 5 times faster as compared to Angular 1.

AngularJS 1 is still a valid choice for Javascript SPA framework. AngularJS 1 is simple and easier to understand and follow for pure Javascript developers. There are a lot more documentation and community contributions for AngularJS 1. For these reasons, AngularJS 1 is still going to be around for many more years. However, Angular 2 is a great framework to start a greenfield project. 
