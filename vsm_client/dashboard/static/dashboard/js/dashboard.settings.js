var site_settings = '<div class="ts-button">'
        +'<span class="fa fa-cogs fa-spin"></span>'
    +'</div>'
    +'<div class="ts-body">'
        +'<div class="ts-title">Options</div>'
        +'<div class="ts-row">'
            +'<label class="check"><input type="checkbox" class="icheckbox" name="st_row1" value="1" /> Hide Capacity</label>'
        +'</div>'
        +'<div class="ts-row">'
            +'<label class="check"><input type="checkbox" class="icheckbox" name="st_row2" value="1" />Hide Cluster</label>'
        +'</div>'
        +'<div class="ts-row">'
            +'<label class="check"><input type="checkbox" class="icheckbox" name="st_row3" value="1" />Hide Performance</label>'
        +'</div>'
        +'<div class="ts-row">'
            +'<label class="check"><input type="checkbox" class="icheckbox" name="st_row4" value="1"/>Hide Log</label>'
        +'</div>'
    +'</div>';
    
var settings_block = document.createElement('div');
    settings_block.className = "theme-settings";
    settings_block.innerHTML = site_settings;
    document.body.appendChild(settings_block);

$(document).ready(function(){

    $(".theme-settings input").on("ifClicked",function(){
        var input = $(this);
        var checked = input.is(':checked')
        var display = "none";
        if(checked == true)
            display = "";

        switch(input.attr("name")){
            case "st_row1":
                $("#row1").css("display",display);
                break;
            case "st_row2":
                $("#row2").css("display",display);
                break;
            case "st_row3":
                $("#row3").css("display",display);
                break;
            case "st_row4":
                $("#row4").css("display",display);
                break;
        }
    });

    /* Open/Hide Settings */
    $(".ts-button").on("click",function(){
        $(".theme-settings").toggleClass("active");
    });
    /* End open/hide settings */
});