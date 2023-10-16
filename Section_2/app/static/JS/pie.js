var expenseElement = document.getElementById("expense");
var incomeElement = document.getElementById("income");

var goalName = document.getElementById("goal_name").textContent || "No Name";
var goalValue = parseFloat(document.getElementById("goal_value").textContent || "0");

var expense = parseFloat(expenseElement.textContent || "0");
var income = parseFloat(incomeElement.textContent || "0");

var isDummyData = false;

var jsonData = {
    labels: ["Income", "Expense"],
    data: [income, expense],
};

if (isNaN(goalValue) && income == 0 && expense == 0) {
    goalValue = 1;
    goalName = "Dummy Goal";
    income = 0.5;
    expense = 0.2;
    isDummyData = true;
} else if (isNaN(goalValue)) {
    goalValue = 0;
    goalName = "Dummy Goal";
    isDummyData = true;
}

var difference = {
    labels: ["Income", "Expenses", "Balance", goalName],
    data: [income, expense, income - expense, goalValue],
};

// to give look of pie chart when no data is present (eg when submitting)
if (jsonData.data[0] === 0 && jsonData.data[1] === 0) {
    jsonData.data = [1, 1];
}

function drawPieChart(data) {
    var ctx = document.getElementById("myPieChart").getContext("2d");
    var myPieChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: data.labels,
            datasets: [
                {
                    data: data.data,
                    backgroundColor: ["rgba(54, 60, 235, 0.7)", "#6750a4"],

                    borderWidth: 0,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 2000,
                easing: "easeOutBounce",
                animateRotate: true,
                animateScale: true,
            },
        },
    });
}

function drawbarChart(data) {
    var ctx = document.getElementById("myBarChart").getContext("2d");
    var myPieChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: data.labels,
            datasets: [
                {
                    data: data.data,
                    backgroundColor: ["#6750a4", "#50A491", "#9150A4", "#5063A4"],
                    borderWidth: 0,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
        },
    });
}

window.onload = function () {
    drawPieChart(jsonData);
    drawbarChart(difference);

    if (isDummyData) {
        var dummyWarning = document.getElementById("dummy");
        var text = document.createTextNode("Dummy data used until data added!");

        dummyWarning.appendChild(text);
    }
};
