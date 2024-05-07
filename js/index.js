$(document).ready(function () {
    document.getElementById('top_left').addEventListener('click', function () {
        // Navigate to page1.html
        location.href = '#';
    });

    document.getElementById('top_right').addEventListener('click', function () {
        // Navigate to page2.html
        location.href = '../html/under_construction.html';
    });

    document.getElementById('bottom_left').addEventListener('click', function () {
        location.href = '../html/primary_sales.html';
    });

    document.getElementById('bottom_right').addEventListener('click', function () {
        location.href = '../html/secondary_sales.html';
    });
});
