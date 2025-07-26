$(document).ready(() => {
    // 1 
    let result1 = false; // login
    let result2 = false; // pass1
    let result3 = false; // pass2
    let result4 = false; // email

    // 2 - login
    $('#login').blur(() => {
        let loginX = $('#login').val();
        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-\.]{5,15}$/;
        if (loginRe.test(loginX)) {
            // Проверка занятости логина
            $.ajax({
                url: '/accounts/ajaxreg',
                data: 'login=' + loginX,
                success: (result) => {
                    if (result.message === 'Логін зайнятий!') {
                        $('#login-err').text(result.message);
                        result1 = false;
                    } else {
                        $('#login-err').text(result.message);
                        result1 = true;
                    }
                }
            });
        } else {
            $('#login-err').text('Помилка формату введення');
            result1 = false;
        }
    });
    // 3 - pass1
    $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_\-\.]{8,}$/;
        if (passRe.test(pass1X)) {
            $('#pass1-err').text('');
            result2 = true
            console.log('Ok')
        } else {
            $('#pass1-err').text('Помилка формату введення пароля');
            result2 = false;
            console.log('Ne ok')
        }
    });
    // 4 - pass2 
    $('#pass2').blur(() => {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            $('#pass2-err').text('');
            result3 = true
        } else {
            $('#pass2-err').text('Введені паролі не співпадають');
            result3 = false;
        }
    });
    // 5 - email
    $('#email').blur(() => {
        let emailX = $('#email').val();
        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailRe.test(emailX)) {
            $('#email-err').text('');
            result4 = true;
        } else {
            $('#email-err').text('Не вірно вказана пошта');
            result4 = false
        }
        });
    // 6 - all together
    $('#submit').click(() => {
        if (
            result1 === true &&
            result2 === true &&
            result3 === true &&
            result4 === true 
        ) {
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Форма містить некоректні дани!\nВідправка даних заблокована!')
        }
    })
});