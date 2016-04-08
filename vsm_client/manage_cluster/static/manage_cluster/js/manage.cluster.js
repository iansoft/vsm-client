$(function(){
    uiSmartWizard();
})



var uiSmartWizard = function(){
    if($(".wizard").length > 0){
        //Check count of steps in each wizard
        $(".wizard > ul").each(function(){
            $(this).addClass("steps_"+$(this).children("li").length);
        });

        $(".wizard").smartWizard({
            //next step
            onLeaveStep: function(obj){
                var wizard = obj.parents(".wizard");

                if(wizard.hasClass("wizard-validation")){
                    var valid = true;
                    
                    $('input,textarea',$(obj.attr("href"))).each(function(i,v){
                        console.log(v);
                        //valid = validator.element(v) && valid;
                    });

                    if(!valid){
                        wizard.find(".stepContainer").removeAttr("style");
                        //validator.focusInvalid();                                
                        return false;
                    }
                }    
                
                return true;
            },// <-- TO
            //finish the wizard
            onFinish:function(obj){
                console.log("finish the wizard");
            },// <-- TO
            //This is important part of wizard init
            onShowStep: function(obj){              
                var wizard = obj.parents(".wizard");

                if(wizard.hasClass("show-submit")){
                    var step_num = obj.attr('rel');
                    var step_max = obj.parents(".anchor").find("li").length;

                    //if this is the last step, show the finished button
                    if(step_num == step_max){                             
                        obj.parents(".wizard").find(".actionBar .btn-primary").css("display","block");
                    }                         
                }
                return true;                         
            }//End
        });
    }
}




// // Start Smart Wizard
//         var uiSmartWizard = function(){
            
//             if($(".wizard").length > 0){
                

                
//                 // This par of code used for example
//                 if($("#wizard-validation").length > 0){
                    
//                     var validator = $("#wizard-validation").validate({
//                             rules: {
//                                 login: {
//                                     required: true,
//                                     minlength: 2,
//                                     maxlength: 8
//                                 },
//                                 password: {
//                                     required: true,
//                                     minlength: 5,
//                                     maxlength: 10
//                                 },
//                                 repassword: {
//                                     required: true,
//                                     minlength: 5,
//                                     maxlength: 10,
//                                     equalTo: "#password"
//                                 },
//                                 email: {
//                                     required: true,
//                                     email: true
//                                 },
//                                 name: {
//                                     required: true,
//                                     maxlength: 10
//                                 },
//                                 adress: {
//                                     required: true
//                                 }
//                             }
//                         });
                        
//                 }// End of example
                
//                 $(".wizard").smartWizard({                        
//                     // This part of code can be removed FROM
//                     onLeaveStep: function(obj){
//                         var wizard = obj.parents(".wizard");

//                         if(wizard.hasClass("wizard-validation")){
                            
//                             var valid = true;
                            
//                             $('input,textarea',$(obj.attr("href"))).each(function(i,v){
//                                 valid = validator.element(v) && valid;
//                             });
                                                        
//                             if(!valid){
//                                 wizard.find(".stepContainer").removeAttr("style");
//                                 validator.focusInvalid();                                
//                                 return false;
//                             }         
                            
//                         }    
                        
//                         return true;
//                     },// <-- TO
                    
//                     //This is important part of wizard init
//                     onShowStep: function(obj){                        
//                         var wizard = obj.parents(".wizard");

//                         if(wizard.hasClass("show-submit")){
                        
//                             var step_num = obj.attr('rel');
//                             var step_max = obj.parents(".anchor").find("li").length;

//                             if(step_num == step_max){                             
//                                 obj.parents(".wizard").find(".actionBar .btn-primary").css("display","block");
//                             }                         
//                         }
//                         return true;                         
//                     }//End
//                 });
//             }            
            
//         }// End Smart Wizard