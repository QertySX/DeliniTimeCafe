$(function () {
  const $form = $('#form2');
  const $authMessage = $('#auth-message');
  const $submitBtn = $form.find('button[type="submit"]');

  function getCSRFToken() {
    return $('input[name="csrfmiddlewaretoken"]').val();
  }

  $form.on('submit', function (e) {
    e.preventDefault();
    
    // Очистка предыдущего сообщения
    $authMessage.text('').css('color', '');

    // Блокируем кнопку
    $submitBtn.prop('disabled', true).text('Зачекайте...');

    $.ajax({
      url: $form.attr('action'),
      type: 'POST',
      data: $form.serialize(),
      headers: {
        'X-CSRFToken': getCSRFToken()
      },
      success: function (response) {
        const color = response.status === 'success' ? 'green' : 'red';
        $authMessage.text(response.message).css('color', color);

        if (response.status === 'success') {
          setTimeout(() => {
            window.location.href = '/';
          }, 1500);
        }
      },
      error: function () {
        $authMessage.text('Помилка з’єднання із сервером. Спробуйте пізніше.').css('color', 'red');
      },
      complete: function () {
        // Разблокируем кнопку
        $submitBtn.prop('disabled', false).text('Увійти');
      }
    });
  });
});
