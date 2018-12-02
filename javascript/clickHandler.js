console.log("Goodbye World.");
var semBtnGroup = document.getElementById("semBtnGroup");

function getWeightedGrade(weight, maxScore, scoreAchieved){
    var result = 0;
    if(maxScore > 0){
        result = weight * (scoreAchieved/ maxScore);
    }
}
