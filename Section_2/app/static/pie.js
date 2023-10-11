var expenseElement = document.getElementById("expense");
var incomeElement = document.getElementById("income");
var goalValue = parseFloat(document.getElementById("goal_value").textContent || "0");
var goalName = document.getElementById("goal_name").textContent || "No Name";

console.log(goalName);

var expense = parseFloat(expenseElement.textContent || "0");
var income = parseFloat(incomeElement.textContent || "0");

var jsonData = {
    labels: ["Income", "Expense"],
    data: [income, expense],
};

var difference = {
    labels: ["Income - Expenses", goalName],
    data: [income - expense, goalValue],
};

// to give look of pie chart when no data is present (eg when submitting)
if (jsonData.data[0] === 0 && jsonData.data[1] === 0) {
    jsonData.data = [1, 1];
}

function drawPieChart(data) {
    var ctx = document.getElementById("myPieChart").getContext("2d");
    var myPieChart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: data.labels,
            datasets: [
                {
                    data: data.data,
                    backgroundColor: [
                        "rgba(30, 99, 132, 0.7)",
                        "rgba(54, 60, 235, 0.7)",
                        "rgba(60, 206, 86, 0.7)",
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                    ],
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
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
                    backgroundColor: [
                        "rgba(30, 99, 132, 0.7)",
                        "rgba(54, 60, 235, 0.7)",
                        "rgba(60, 206, 86, 0.7)",
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                    ],
                    borderWidth: 1,
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
};
