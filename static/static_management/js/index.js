$(".body_left_list >li >label").on('click',function () {
    $gao = $(this).parent('li').css('max-height');
    if($gao == '1500px'){
        $(this).parent('li').animate({'max-height':'40px'});
        $(this).children('i').css({
            'transform':'rotate(-90deg)'
        })
    }else{
        $(this).parent('li').animate({'max-height':'1500px'});
        $(this).children('i').css({
            'transform':'rotate(0)'
        })
    }
});