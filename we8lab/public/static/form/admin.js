function select_InputTypeFunctionality_handle(select) {
    let container = select.parentNode.parentNode.parentNode
    if (container) {
        if(select.value == 9) {
            container.querySelector('.field-select_options').style.display = 'block';
        } else {
            container.querySelector('.field-select_options').style.display = 'none';
        }

    }
}

function select_InputTypeFunctionality() {
    document.querySelectorAll('div.field-input_type select').forEach(select => {
        select.onchange = function() {
            select_InputTypeFunctionality_handle(this);
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    setInterval(() => {
        select_InputTypeFunctionality();
    }, 500)
});