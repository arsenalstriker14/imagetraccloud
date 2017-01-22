function get_sku(){
    sku = $(this).html().slice(0, 15)
    href = "/product/" + sku + "/" + $(this).html()
    watchConsole(href);
}
function getExcel(url){
    newwindow=window.open(url,'b5advertising | watchedimages','height=700, width=1200,top=20,left=0,resizable');
    if (window.focus) {newwindow.focus()}
}

function processJobNumber(){
    url = $('#search_button').attr('href');
    var input = $('#job_id').val();
    var href = url + input;
    showConsole(href);
}
function editAdSheet(){
    url = $('#edit_button').attr('href');
    var input = $('#job_id').val();
    var href = url + input;
    showConsole(href);
}

function processProductNumber(){
    url = $('#product_button').attr('href');
    var input = $('#product_id').val();
    var href = url + input;
    showConsole(href);
}

function showConsole(url) {
    newwindow=window.open(url,'b5advertising | imageconsole','height=700, width=1200,top=20,left=0,resizable');
    if (window.focus) {newwindow.focus()}
}

function watchConsole(url) {
    newwindow=window.open(url,'b5advertising | watchedimages','height=800, width=1260,top=20,left=0,resizable,scrollbars=yes');
    if (window.focus) {newwindow.focus()}
}

function showQuickcard(url) {
    newwindow=window.open(url,'b5advertising | showMessage','height=350, width=650,top=20,left=0,resizable');
    if (window.focus) {newwindow.focus()}
}

function showQuickpost(url) {
    $('.shell').css('margin', '0');
    $('.stage').fadeOut( "fast", function() { });
    $('#inbox_frame').attr('src', url);
    $('#inbox_frame').fadeIn(4000, function() { })
}


function showDashboard() {
    url = $('#inbox_button').attr('href');
    $('.shell').css('margin', '0');
    $('.stage').fadeOut( "fast", function() { });
    $('iframe').fadeOut( "fast", function() { });
    $('#inbox_frame').attr('src', url);
    $('#inbox_frame').fadeIn(4000, function() { });
    
//  newwindow=window.open(url,'WRMS | Project Inbox','height=700, width=1200,top=20,left=0,resizable');
//  if (window.focus) {newwindow.focus()}
}

function showChangeList() {
    url = $('#edit_link').attr('href');
    $('.shell').css('margin', '0');
    $('.stage').fadeOut( "fast", function() { });
    $('iframe').fadeOut( "fast", function() { });
    $('#inbox_frame').attr('src', url);
    $('#inbox_frame').fadeIn(4000, function() { });
    
//  newwindow=window.open(url,'WRMS | Project Inbox','height=700, width=1200,top=20,left=0,resizable');
//  if (window.focus) {newwindow.focus()}
}

function addOnload(newFunction) {
    var oldOnload = window.onload;

    if (typeof oldOnload == "function") {
        window.onload = function() {
            if (oldOnload) {
                oldOnload();
            }
            newFunction();
        }
    }
    else {
        window.onload = newFunction;
    }

}

function addRow(){
    var hiddenrow = document.getElementsByClassName("postrequest_row");
console.log(hiddenrow);
    for(var i=0; i< hiddenrow.length; i++){
        console.log(hiddenrow[i].style);
        var styleDisplay = getStyle(hiddenrow[i], "display");

        if(styleDisplay  == "none"){
            hiddenrow[i].style.display = "block";
            break;
        }
    }
}
function addLink(){
    var hiddenrow = document.getElementsByClassName("request_row");
console.log(hiddenrow);
    for(var i=0; i< hiddenrow.length; i++){
        console.log(hiddenrow[i].style);
        var styleDisplay = getStyle(hiddenrow[i], "display");

        if(styleDisplay  == "none"){
            hiddenrow[i].style.display = "block";
            break;
        }
    }
}

function callTacticPage(){
    window.open ("../../newtacticpage", "Create New Tactic Page", "width=500", "height=400");
}
function getStyle(el, styleProp)
{
    if (el.currentStyle)
        var y = el.currentStyle[styleProp];
    else if (window.getComputedStyle)
        var y = document.defaultView.getComputedStyle(el,null).getPropertyValue(styleProp);
    return y;
}



//page scripts

//base.html

function multiPost(url){
    var input = $('#job_id').val();
    var input = input.toUpperCase();
    var client = $('#client_select').find(":selected").attr('id');
    if (input.length < 8 || input.length > 15) {
        alert ("Please input a valid job number");
    }else if (client == "null_option"){
    alert ("Please choose a client from the dropdown menu at left");
    }else{                
    var href ='{{ base_url }}/b5/multipost-init/' + client + '/' + input ;
    window.location = href;
    }
}
function routeToAdd(){
    var href ='{{ base_url }}/b5/multipost/';
    window.location = href;
}
function routeToDex(){
    var href ='{{ base_url }}/b5/add_dex/';
    window.location = href;
}
function routeFR(){
    var href ='{{ base_url }}/b5/add_first/';
    window.location = href;
}

function get_sku(){
    sku = $(this).html().slice(0, 15)
    href = "/product/" + sku + "/" + $(this).html()
}
function mark_status(){
    $('.marker').each(function(index, element){
        var status = $(this).siblings('.status');
        if ($(this).html() && $(this).html() != 'None'){
            status[0].innerHTML = "<div class='stat_in'></div> IN";
        }else{
            status[0].innerHTML = "<div class='stat_out'></div> OUT";
        }
         
    });
}
       

//check_template.html

//console_template.html
