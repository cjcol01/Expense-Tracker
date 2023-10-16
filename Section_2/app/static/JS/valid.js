document.addEventListener("DOMContentLoaded", function () {
    const form = document.forms["form1"];

    form.addEventListener("submit", function (e) {
        let valid = true;

        // Validate name
        const name = form["name"].value.trim();
        if (name === "" || name.length > 25) {
            alert("Name must be non-empty and less than 50 characters.");
            valid = false;
        }

        // Validate cost
        const cost = parseFloat(form["cost"].value);
        if (isNaN(cost) || cost <= 0 || cost > 10000) {
            alert("Cost must be a number between 0 and 10000");
            valid = false;
        }
        // Prevent form submission if validation fails
        if (!valid) {
            e.preventDefault();
        }
    });
});
