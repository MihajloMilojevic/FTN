var loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(e) {
    e.preventDefault();

    var username = document.getElementById('txtUsername');
    console.log(username);
});