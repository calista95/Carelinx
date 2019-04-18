$(document).ready(function(){

   //handlers for the click/double click toggles 
   $(".friday").click(function(){
    $('.rowFriday').show();
   });

   $(".friday").dblclick(function(){
    $('.rowFriday').hide();
   });

   $(".saturday").click(function(){
    $('.rowSaturday').show();
   });

   $(".saturday").dblclick(function(){
    $('.rowSaturday').hide();
   });

   $(".sunday").click(function(){
    $('.rowSunday').show();
   });

   $(".sunday").dblclick(function(){
    $('.rowSunday').hide();
   });

});