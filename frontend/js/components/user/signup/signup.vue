<template>
    <div id="signup" class='shouldCollapse'>
        <div id="signupWrapper" v-if='signupFormShouldShowMethod()'>
            <div class="title">
                <p>ثبت نام</p>
            </div>
            <div id="signupForm">
                <form action="/users/register/" method="post" novalidate>
                    <div id="email" class="inputs">
                        <div class='formInputsWrapper'>
                                <input autocomplete="off" name="email" @blur='focusOut($event),startValidation("email",$event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userEmail' type="text">
                                <label class='comeUpLabel' for="userEmail">ایمیل</label>                                                                  
                        </div>
                        <p class="inputError">فرمت ایمیل اشتباه است</p> 
                    </div>

                    <div id="userName" class="inputs">
                        <div class='formInputsWrapper'>
                                <input autocomplete="off" name="username" @blur='focusOut($event),startValidation("name",$event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userName' type="text">
                                <label class='comeUpLabel' for="userName">نام کاربری</label>                                                                  
                        </div>
                        <p class="inputError">فرمت نام اشتباه است</p> 
                    </div>

                    <div id="password" class="inputs">
                        <div class='formInputsWrapper'>
                                <input autocomplete="off" name="password1" v-model="pass" @blur='focusOut($event),startValidation("pass",$event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userPassword' type="password">
                                <label class='comeUpLabel' for="userPassword">رمز</label>                                
                        </div>
                        <p class="inputError">رمز باید حداقل 8 کاراکتر باشد و همچنین حداقل شامل یک کاراکتر خاص مثل <span>#</span> باشد</p> 
                    </div>
                    <div id="passwordConf" name="password2" class="inputs">
                        <div class='formInputsWrapper'>
                                 
                                <input autocomplete="off" @blur='focusOut($event),checkConfirmation($event)' id='userPasswordCond' class='inputWithLabelThatShouldStay signupFormInputs' name='password2'  type="password">
                                <label class='comeUpLabel' for="userPasswordCond">رمز را دوباره وارد کنید</label>
                                
                        </div>
                        <p class="inputError">با رمز اصلی برابر نیست</p> 
                    </div>
                    <div id="submit" class='inputs'>
                        <button @click='checkInputs($event)' class="submit">
                            ثبت نام
                        </button>
                    </div>
                </form>
            </div>
        </div>





        <div id="signupWrapper" v-if='signinFormShouldShowMethod()'>
            <div class="title">
                <p>ورود</p>
            </div>
            <div id="signupForm">
                <form action="">
                    <div id="email" class="inputs">
                        <div class='formInputsWrapper'>
                                                       
                                <input @blur='focusOut($event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userEmail' type="text">
                                <label class='comeUpLabel' for="userEmail">ایمیل یا نام کاربری</label>

                        </div>
                    </div>
                    <div id="password" class="inputs">
                        <div class='formInputsWrapper'>
                                
                                <input @blur='focusOut($event)' class='inputWithLabelThatShouldStay signupFormInputs' id='userPassword' type="text">
                                <label class='comeUpLabel' for="userPassword">رمز</label>
                        </div>
                    </div>
                    <div id="submit" class='inputs'>
                        <button class="submit">
                            ورود
                        </button>
                    </div>
                </form>
            </div>
        </div>




    </div>

</template>

<style scoped>
    #signup{
        background: white;
        margin-top:20px;
        border-radius: 5px;
    }
    label,p{
        color:rgb(41,41,41)
    }
    #signupWrapper{
        display:flex;
        flex-direction:column;
        justify-content: center;
        padding:10px        
    }
    form{
        width:100%;
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .inputs{
        display: flex;
        flex-direction: column;
        align-items: center;
        width:100%;
        margin-top:20px;
    }
    
    form div div{
        display:flex;
        justify-content: space-around;
    }
    input + label{
      display:block;
        cursor:text;
        color:#777;
        transition:.15s ease-out all;
        position:absolute;
        right:1em;
    }
    .title{
        display:flex;
        justify-content: center;
        font-size:24pt
    }
    input{
        border:1px solid rgb(202, 202, 202);
        border-radius:5px;
        padding:1em 1em .8em 1em;
        color:black;
        direction:ltr
    }
    
    .inputError{
        max-width:150px;
        text-align:justify ;
    }
    .inputError span{
        color:black !important
    }

</style>


<script>
    import {validationRules} from "../mixIns/validationMixIn.js"
    import {keepStay} from "../mixIns/keepStay.js"
    export default{
        mixins:[validationRules,keepStay],
        mounted(){
            const inputs=document.querySelectorAll(".formInputsWrapper input")
            inputs.forEach(inp=>{
                inp.addEventListener("focus",input=>{
                
            })
            })
        },
        props:["signupformshouldshow",'signinformhouldshow'],
        created(){
            // console.log(this.validateUserInput())
        },
        data(){
            return{
                pass:''
            }
        },
        methods:{
            
            signupFormShouldShowMethod(){
                return this.signupformshouldshow=="true" ? true : false
            },
            signinFormShouldShowMethod(){
                return this.signinformhouldshow=="true" ? true : false
            },
            startValidation(type,e){
                const el=e.target
                const parentNode=e.target.parentElement
            
                const error=parentNode.nextElementSibling
                if(el.id=="userPassword" && el.value.length<8)
                {
                     error.style.visibility="visible"
                     el.classList.remove("correct")
                     el.classList.add("wrong")
                     return
                }
                const res=this.validateUserInput(type,e)
                
                
                if(res){
                    error.style.display="none"
                    return
                }
                error.style.display="block"
            }
        }
    }
</script>