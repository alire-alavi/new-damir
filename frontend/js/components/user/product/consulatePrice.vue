<template>
    
        <div class="productConsulate" @click='closeConsulate'>
                <div class="productConsulateWrapper" @click="preventDefault($event)">
                    <form action="">
                        <div id="email" class="inputs">
                            <div class='formInputsWrapper'>
                                    <input autocomplete="off" name="email" @blur='focusOut($event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userName' type="text">
                                    <label class='comeUpLabel' for="userName">نام</label>                                                                  
                            </div>
                        </div>
                        <div id="email" class="inputs">
                            <div class='formInputsWrapper'>
                                    <input autocomplete="off" name="email" @blur='focusOut($event),startValidation("email",$event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userPhone' type="text">
                                    <label class='comeUpLabel' for="userPhone">شماره تلفن</label>                                                                  
                            </div>
                            <p class="inputError">فرمت شماره اشتباه است</p> 
                        </div>
                        <div class="sendReq">
                            <button @click.prevent="sendPriceRequest" class="submit">ثبت</button>
                        </div>
                    </form>
                </div>
            </div>
</template>

<script>
import {keepStay} from "../../user/mixIns/keepStay.js"
import {adjustElFromTop} from "../../user/mixIns/adjustElFromTop.js"
import doneMessage from "../../user/template/doneMessage/doneMessage.vue"
export default {
    mixins:[keepStay,adjustElFromTop],
    components:{
        doneMessage
    },
    methods:{

       
            sendPriceRequest(){
                const done=document.querySelector("#doneMessage")
                done.style.display='block'
                setTimeout(()=>{
                    done.style.display="none"
                },5000)

            },
            preventDefault(e)
            {
                e.stopPropagation()
            },
            closeConsulate(){
                const consulet=document.querySelector(".productConsulate")
                consulet.style.display="none"

            }
    }
}
</script>

<style scoped>
.productConsulate{
    position:absolute;
    background: rgba(0,0,0,0.6);
    height:100%;
    width:100%;
    top:0;
    left:0;
    display:none;
    z-index:668

}
.inputs{
    margin-top:5px
}
.productConsulateWrapper{
    position:fixed;
    background:#ffffff;
    padding:10px;
    transform: translateY(50%) translateX(-50%);
    left: 50%;
}
.sendReq{
    display:flex;
    justify-content: center;
}

</style>