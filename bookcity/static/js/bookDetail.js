if(num!=0){
    for (var i=num; i>0; i--) {
        $('#label' + i).css('background-color', '#F90')
    }
}
$(document).ready(function(){
    // Check Radio-box
    $(".rating input:radio").attr("checked", false);
    $('.rating input').click(function () {
        $(".rating span").removeClass('checked');
        $(this).parent().addClass('checked');
    });
    $('input:radio').change(function(){
        var userRating = this.value;
        window.location='rate/'+ userRating
    });
});
function readMe(){
    window.location = 'read/'
}
function unReadMe(){
    window.location = 'unread/'
}
function wishList(){
    window.location = 'wishList/'
}
function unWish(){
    window.location = 'unWish/'
}