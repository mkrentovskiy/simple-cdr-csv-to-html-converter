$(document).ready(function(){
	$("a[rel='audio']").click(function() { return play($(this)); });
    });
    
function play(i) 
{
	var p = i.position();
	var h = i.height();
	$("#pl").show().css('left', (p.left) + 'px').css('top', (p.top + h) + 'px').html("<audio controls autoplay><source src='" + i.attr('href') + "'/></audio>"); 
	return false;
}