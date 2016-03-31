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

// function set_settings(theme_settings,option){
    
//     /* Start Header Fixed */
//     if(theme_settings.st_head_fixed == 1)
//         $(".page-container").addClass("page-navigation-top-fixed");
//     else
//         $(".page-container").removeClass("page-navigation-top-fixed");    
//     /* END Header Fixed */
    
//     /* Start Sidebar Fixed */
//     if(theme_settings.st_sb_fixed == 1){        
//         $(".page-sidebar").addClass("page-sidebar-fixed");
//     }else
//         $(".page-sidebar").removeClass("page-sidebar-fixed");
//     /* END Sidebar Fixed */
    
//     /* Start Sidebar Fixed */
//     if(theme_settings.st_sb_scroll == 1){          
//         $(".page-sidebar").addClass("scroll").mCustomScrollbar("update");        
//     }else
//         $(".page-sidebar").removeClass("scroll").css("height","").mCustomScrollbar("disable",true);
    
//     /* END Sidebar Fixed */
    
//     /* Start Right Sidebar */
//     if(theme_settings.st_sb_right == 1)
//         $(".page-container").addClass("page-mode-rtl");
//     else
//         $(".page-container").removeClass("page-mode-rtl");
//     /* END Right Sidebar */
    
//     /* Start Custom Sidebar */
//     if(theme_settings.st_sb_custom == 1)
//         $(".page-sidebar .x-navigation").addClass("x-navigation-custom");
//     else
//         $(".page-sidebar .x-navigation").removeClass("x-navigation-custom");
//     /* END Custom Sidebar */
    
//     /* Start Custom Sidebar */
//     if(option && option === 'st_sb_toggled'){
//         if(theme_settings.st_sb_toggled == 1){
//             $(".page-container").addClass("page-navigation-toggled");
//             $(".x-navigation-minimize").trigger("click");
//         }else{          
//             $(".page-container").removeClass("page-navigation-toggled");
//             $(".x-navigation-minimize").trigger("click");
//         }
//     }
//     /* END Custom Sidebar */
    
//     /* Start Layout Boxed */
//     if(theme_settings.st_layout_boxed == 1)
//         $("body").addClass("page-container-boxed");
//     else
//         $("body").removeClass("page-container-boxed");
//     /* END Layout Boxed */
    
//     /* Set states for options */
//     if(option === false || option === 'st_layout_boxed' || option === 'st_sb_fixed' || option === 'st_sb_scroll'){        
//         for(option in theme_settings){
//             set_settings_checkbox(option,theme_settings[option]);
//         }
//     }
//     /* End states for options */
    
//     /* Call resize window */
//     $(window).resize();
//     /* End call resize window */
// }

// function set_settings_checkbox(name,value){
    
//     if(name == 'st_layout_boxed'){    
        
//         $(".theme-settings").find("input[name="+name+"]").prop("checked",false).parent("div").removeClass("checked");
        
//         var input = $(".theme-settings").find("input[name="+name+"][value="+value+"]");
                
//         input.prop("checked",true);
//         input.parent("div").addClass("checked");        
        
//     }else{
        
//         var input = $(".theme-settings").find("input[name="+name+"]");
        
//         input.prop("disabled",false);            
//         input.parent("div").removeClass("disabled").parent(".check").removeClass("disabled");        
        
//         if(value === 1){
//             input.prop("checked",true);
//             input.parent("div").addClass("checked");
//         }
//         if(value === 0){
//             input.prop("checked",false);            
//             input.parent("div").removeClass("checked");            
//         }
//         if(value === -1){
//             input.prop("checked",false);            
//             input.parent("div").removeClass("checked");
//             input.prop("disabled",true);            
//             input.parent("div").addClass("disabled").parent(".check").addClass("disabled");
//         }        
                
//     }
// }