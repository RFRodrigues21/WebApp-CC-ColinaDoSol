function equalValues() {
            const weekdays = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado'];
            const horarioSegAbValue = document.getElementById('id_segunda-opening_time').value;
            const horarioSegFeValue = document.getElementById('id_segunda-closing_time').value;
            const horarioSegAbAlmocoValue = document.getElementById('id_segunda-lunch_start_time').value;
            const horarioSegFeAlmocoValue = document.getElementById('id_segunda-lunch_end_time').value;

            weekdays.forEach(day => {
                document.getElementById(`id_${day}-opening_time`).value = horarioSegAbValue;
                document.getElementById(`id_${day}-closing_time`).value = horarioSegFeValue;
                document.getElementById(`id_${day}-lunch_start_time`).value = horarioSegAbAlmocoValue;
                document.getElementById(`id_${day}-lunch_end_time`).value = horarioSegFeAlmocoValue;
            });
        }