const form = document.getElementById('payForm');
const orderIdInput = document.getElementById('order_id_input');

form.addEventListener("submit", submitHandler);

function submitHandler(e) {
  e.preventDefault();

  // Serialize the form data
  const serializedData = $(form).serialize();

  // Make the AJAX request
  $.ajax({
    type: 'POST',
    url: '{% url "product_detail" product.id %}',
    data: serializedData,
    dataType: 'json',
    success: function (data) {
      const price = data.price;
      const des = data.descrip;

      // Attach click event handler to the payButton

      const payload = {
        price_amount: price,
        price_currency: 'usd',
        order_id: orderIdInput.value,
        order_description: des,
        ipn_callback_url: 'https://nowpayments.io',
        success_url: 'https://nowpayments.io',
        cancel_url: 'https://nowpayments.io'
      };

      const settings = {
        url: 'https://api.nowpayments.io/v1/invoice',
        method: 'POST',
        headers: {
          'x-api-key': '6QW5RCW-HW7MBKQ-JFD823E-1527K1S',
          'Content-Type': 'application/json'
        },
        data: JSON.stringify(payload),
        success: function (response) {
          const paymentUrl = response.invoice_url;
          window.location.href = paymentUrl;
        },
        error: function (error) {
          console.log(error);
        }
      };

      $.ajax(settings);


      console.log('Redirecting to the payment page');
    }
  });
}

