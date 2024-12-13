const event_date_time = '#id_event_date_time';
const date_time = document.querySelector(event_date_time).value;
flatpickr(event_date_time, {
    enableTime: true,
    altInput: true,
    dateFormat: "Y-m-d H:i",
    altFormat: 'l J F, Y h:i K',
    minDate: 'today',
    defaultDate: date_time !== '' ? date_time : new Date(),
});