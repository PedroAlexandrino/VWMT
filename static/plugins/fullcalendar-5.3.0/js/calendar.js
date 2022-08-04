document.addEventListener('DOMContentLoaded', function() {
    //Quando o Html estiver totalmente renderizado:


    /* initialize the external events = Eventos Externos, cria um objecto Draggable 
    -----------------------------------------------------------------*/

    var containerEl = document.getElementById('external-events-list');
    new FullCalendar.Draggable(containerEl, {
        itemSelector: '.fc-event', //pega todos os elementos filhas da div external events list que possuirem a classe fc
        eventData: function(eventEl) {
            return {
                title: eventEl.innerText.trim()
            }
        }
    });



    /* initialize the calendar: Criacao do calendario
    -----------------------------------------------------------------*/

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        },
        locale: 'pt',
        navLinks: true,
        //eventLimit: true,
        selectable: true,
        editable: true,
        droppable: true, // this allows things to be dropped onto the calendar
        drop: function(arg) {
            // is the "remove after drop" checkbox checked? O TAL CHECKBOX
            if (document.getElementById('drop-remove').checked) {
                // if so, remove the element from the "Draggable Events" list
                arg.draggedEl.parentNode.removeChild(arg.draggedEl);
            }
        },
        eventDrop: function(event) { //Quando ha um evento de drop para outro local
            alert('Event Drop');
        },
        eventClick: function(event) { //Quando eu clico em cima do evento
            alert('Event Click');
        },
        eventResize: function(event) { //Quando acabo de fazer resize
            alert('Event Resize');
        },
        select: function(event) { //Quando acabo de fazer resize
            alert('Event Select');
        },
        events: routeEvents('routeLoadEvents'),

    });
    calendar.render();

});

console.log(routeEvents('routeLoadEvents'));