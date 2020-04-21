

const appendToList = (self, str) => {
    let newElem = document.createElement('li');
    newElem.innerHTML = str;
    newElem.onclick = function() {
        this.remove();
    }
    self.parentElement.parentElement.querySelector('.list-wrapper > ul').append(newElem);
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('Form New JS applied');
    document.querySelectorAll('div.list-wrapper > ul > li').forEach(el => {
        el.addEventListener('click', function() {
            console.log('clicked on lsit element');
            this.remove();
        });
    });

    document.querySelectorAll('div.list-append-form > button').forEach(appendButton => {
        appendButton.addEventListener('click', function(e) {
            e.preventDefault();

            let inputElement = this.parentElement.querySelector('input[type="text"]');

            let newItem = inputElement.value.trim();
            inputElement.value = '';

            appendToList(this, newItem);
        });
    });
});