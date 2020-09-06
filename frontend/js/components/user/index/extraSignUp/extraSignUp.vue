<template>
  <div id="extraSignUp" class='lax'>
    <img src="/images/signupBack4.jpg" alt="">
    <div class="overLay"></div>
    <div class="extraSignUpWrapper">
      <div class="descs">
        <div class="descsWrapper">
            <p>با ثبت نام در دمیرکو به میلیون ها تامین کننده و خریدار دسترسی داشته باشید </p>

        </div>
      </div>

      <div class="signUp">
        <div class="signUpWrapper">
          <form action>
            <div id="email" class="inputs">
              <div class="formInputsWrapper">
                <input autocomplete="off" @blur="focusOut($event),startValidation('email',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="userEmail" type="text"/>
                <label class="comeUpLabel" for="userEmail">ایمیل</label>
              </div>
              <p class="inputError">فرمت ایمیل اشتباه است</p>
            </div>

            <div id="phoneNumber" class="inputs">
              <div class="formInputsWrapper">
                <input autocomplete="off" @blur="focusOut($event),startValidation('phone',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="userPhone" type="text"/>
                <label class="comeUpLabel" for="userPhone">شماره تلفن همراه</label>
              </div>
              <p class="inputError">فرمت شماره اشتباه است</p>
            </div>

            <div id="password" class="inputs">
              <div class="formInputsWrapper">
                <input autocomplete="off" @blur="focusOut($event),startValidation('pass',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="userPassword" type="password"/>
                <label class="comeUpLabel" for="userPassword">رمز</label>
              </div>
              <p class="inputError">
                رمز باید حداقل 8 کاراکتر باشد و همچنین حداقل شامل یک کاراکتر خاص مثل
                <span>#</span> باشد
              </p>
            </div>
            <div id="passwordConf" class="inputs">
              <div class="formInputsWrapper">
                <input autocomplete="off" @blur="focusOut($event),checkConfirmation($event)" id="userPasswordCond inputWithLabelThatShouldStay" class="signupFormInputs" name="passConf" type="password"/>
                <label class="comeUpLabel" for="userPasswordCond">رمز را دوباره وارد کنید</label>
              </div>
              <p class="inputError">با رمز اصلی برابر نیست</p>
            </div>
            <div id="submit" class="inputs">
              <button @click="checkInputs($event)" class="submit">ثبت نام</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import {keepStay} from "../../mixIns/keepStay.js"
    import {validationRules} from "../../mixIns/validationMixIn.js"
    export default{
        mixins:[keepStay,validationRules],
        methods:{
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
                    error.style.visibility="hidden"
                    return
                }
                error.style.visibility="visible"

            }
        }
    }
</script>


<style scoped>
#extraSignUp{
    width:100%;
    position: relative;
}
.signUpWrapper{
    padding:40px;
    -moz-padding:20px;
}
.signUp{
    width:40%;
    background: rgba(187, 186, 186, 0.678);
    max-width:max-content;
}
.overLay{
    position: absolute;
    width:100%;
    background: rgba(0,0,0,0.7);
    z-index:-1;
    height:100%
}
img,#extraSignUp{
  height:630px
}
img{
    width:100%;
    z-index:-2;
    position: absolute;
}
input {
  border: 1px solid rgba(204, 203, 203, 0.918);
  border-radius: 5px;
  padding: 1em 1em 0.8em 1em;
  color: black;
  direction: ltr;
}
.inputs{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top:20px
}
form{
    width:220px
}
.inputs p{
    text-align: center;
}
input + label{
      display:block;
        cursor:text;
        color:#777;
        transition:.15s ease-out all;
        position:absolute;
        right:1em;
    }
.extraSignUpWrapper{
    display:flex;
    justify-content: space-around;
    align-items: center;
    height:100%
}
.descsWrapper p{
    padding:20px;
}
.descs{
    width:60%;
    max-width:max-content;
}
.descsWrapper{
    background: rgba(187, 186, 186, 0.678);
    
}
.correct{
	border:2px solid rgb(51, 250, 25) !important;
}
.wrong{
	border:2px solid rgb(255, 15, 15) !important;
}
.inputError{
	color:rgb(255, 15, 15) !important;
}
@media (max-width:699px)
{
  .extraSignUpWrapper{
    flex-direction:column;
    justify-content: center;
    align-items: center;
    padding:20px;
  }
  #extraSignUp{
    height:max-content
  }
  img{
    height:100%
  }
  .descs{
    width:100%;
  }
  .signUp{
    width:max-content;
    margin-top:50px;
    
    max-width:max-content;
  }
}
</style>