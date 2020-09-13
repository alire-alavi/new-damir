<template>
    <div class="consulate" @click='closeConsulate($event)'>
        <div @click='prevent($event)' class="consulateWrapper">
             <div id="email" class="inputs">
                <div class='formInputsWrapper'>
                        <input autocomplete="off" name="email" @blur='focusOut($event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userEmail' type="text">
                        <label class='comeUpLabel' for="userEmail">نام</label>                                                                  
                </div> 
            </div>
             <div id="email" class="inputs">
                <div class='formInputsWrapper'>
                        <input autocomplete="off" name="email" @blur='focusOut($event),startValidation("phone",$event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userEmail' type="text">
                        <label class='comeUpLabel' for="userEmail">شماره تلفن</label>                                                                  
                </div>
                <p class="inputError">فرمت شماره اشتباه است</p> 
            </div>
            <div>
                <button @click='consulateRequest' class="submit">ثبت</button>
            </div>
            <input type="hidden" :value="productName">

        </div>
    </div>

</template>

<script>
    import {mapActions} from 'vuex'
    import {validationRules} from '../mixIns/validationMixIn.js'
    import {keepStay} from "../mixIns/keepStay.js"
    export default {
        mixins:[validationRules,keepStay],
        props:['productName'],
        methods:{
            ...mapActions([
                'toggleConsulate'
            ]),
            prevent(e){
                e.preventDefault();
                e.stopPropagation()
            },
            closeConsulate(e){
                    e.target.style.display="none"
                    document.body.style.overflow=""
                    // cons.style.display='none'
            },
            consulateRequest(){
                const doneMessage=document.querySelector('#doneMessage')
                doneMessage.style.display='block'
                setTimeout(()=>{
                    doneMessage.style.display='none'
                },5000)
            },
            startValidation(type,e){
                const el=e.target
                const parentNode=e.target.parentElement
            
                const error=parentNode.nextElementSibling
                const res=this.validateUserInput(type,e)
                console.log(error)
                
                
                if(res){
                    error.style.display="none"
                    return
                }
                error.style.display="block"
                
            }
        },
        data(){
            return{
                name:""
            }
        },
        computed:{
            shoudIShow(){
                return this.$store.state.isShowConsulate
                
            }            
        }        
    }
</script>

<style scoped>
    .consulate{
        position: absolute;
        width:100%;
        height:100%;
        display:none;
        top:0;
        right:0;
        left:0;
        bottom:0;
        background: rgb(0,0,0,0.6);
        z-index:667;
        transition: all 0.3s;
        animation: fadeIn 0.3s linear;
    }
    @keyframes fadeIn {
        from{
            opacity: 0;
        }
        to{
            opacity: 1;
        }
    }
    .consulateWrapper{
        display: flex;
        flex-direction: column;
        align-items: center;
        position: absolute;
        background: rgb(233, 233, 233);
        padding:20px;
        left:50%;
        transform: translateX(-50%);
    }
    .submit{
        margin-top:20px;
    }
    .input{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .input label,.input input{
        padding:10px;
        color:black;

    }
    .input:nth-child(:first-child) input
    {
        direction: rtl;
    }
    .input:nth-child(2) input
    {
        direction: ltr;
    }
</style>
