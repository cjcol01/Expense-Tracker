function filterTable(type) {
    var table = document.getElementById("expenseTable");
    var rows = table.getElementsByTagName("tr");
    var visibleRowIndex = 0;
    for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        if (type === "") {
            row.style.display = "";
            recolorRow(row, visibleRowIndex);
            visibleRowIndex++;
        } else if (row.classList.contains(type)) {
            row.style.display = "";
            recolorRow(row, visibleRowIndex);
            visibleRowIndex++;
        } else {
            row.style.display = "none";
        }
    }
}

function recolorRow(row, index) {
    if (index % 2 === 0) {
        row.style.backgroundColor = "#fafafa";
    } else {
        row.style.backgroundColor = "#eeeeee";
    }
}

function deleteExpense(id) {
    if (confirm("Are you sure you want to delete this expense?")) {
        fetch(`/delete_expense/${id}`, {
            method: "POST",
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    location.reload();
                }
            });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll(".delete-button");

    deleteButtons.forEach((button) => {
        button.addEventListener("click", function (e) {
            const expenseId = e.target.getAttribute("data-id");
            deleteExpense(expenseId);
        });
    });
});
