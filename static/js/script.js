//set csrftoken in header
( function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {'X-CSRFToken': csrftoken}
    });
})();

//show form for comment
let openForm = function (id) {
    $(`#${id}`).show()
};

//hide form for comment
let closeForm = function (id) {
    $(`#${id}`).hide()
};

//put like
let like = function (id) {
    $.ajax({
        url:'http://127.0.0.1:8000/like/',
        type:'POST',
        data:{
            pk:id,
        },
        success: (response) => {

        }
    })
};