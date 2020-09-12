<template>
	<div class="footeSignUp">
		<p>ثبت نام</p>
		<div class="footeSignUpWrapper">
			<form>
				<div  class="inputs">
	              <div class="formInputsWrapper">
	                <input autocomplete="off" @blur="focusOut($event),startValidation('name',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="footerUserName" type="text" name="userName"/>
	                <label class="comeUpLabel" for="footerUserName">نام</label>
	              </div>
	              <p class="inputError">فرمت نام اشتباه است</p>
	            </div>
	            <div  class="inputs">
	              <div class="formInputsWrapper">
	                <input autocomplete="off" @blur="focusOut($event),startValidation('email',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="footerUserEmail" type="text" name="userEmail"/>
	                <label class="comeUpLabel" for="footerUserEmail">ایمل </label>
	              </div>
	              <p class="inputError">فرمت ایمیل اشتباه است</p>
	            </div>
	            <div  class="inputs">
	              <div class="formInputsWrapper">
	                <input autocomplete="off" @blur="focusOut($event),startValidation('pass',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="footerUserPassword" type="text" name="userPassword"/>
	                <label class="comeUpLabel" for="footerUserPassword">رمز</label>
	              </div>
	              <p class="inputError">
                	رمز باید حداقل 8 کاراکتر باشد و همچنین حداقل شامل یک کاراکتر خاص مثل
                	<span>#</span> باشد
              	</p>
	            </div>
	            <div  class="inputs">
	              <div class="formInputsWrapper">
	                <input autocomplete="off" @blur="focusOut($event)" class="signupFormInputs inputWithLabelThatShouldStay" id="footerUserPassConf" type="text" name="userPasswordConf"/>
	                <label class="comeUpLabel" for="footerUserPassConf">تایید رمز</label>
	              </div>
	              <p class="inputError">فرمت نام اشتباه است</p>
	            </div>
	            <button class="submit">ثبت نام</button>
			</form>
		</div>
	</div>
</template>


<style scoped>
	.formInputsWrapper{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.inputs{
		margin-top:10px;
	}
	.inputs:nth-child(1)
	{
		margin-top:0;
	}
	form{
		display: flex;
    	flex-direction: column;
	}
	.footeSignUp{
		margin:20px;
	}
	.footeSignUp > p{
		margin-bottom: 5px
	}
	

</style>

<script>
	
	import {keepStay} from "../../../mixIns/keepStay.js"
    import {validationRules} from "../../../mixIns/validationMixIn.js"
	export default{
		name:"signUp",
		mixins:[keepStay,validationRules],
		methods:{
			startValidation(type,e){
                const el=e.target
                const parentNode=e.target.parentElement
            
                const error=parentNode.nextElementSibling
                const res=this.validateUserInput(type,e)
                
                
                if(res){
                    error.style.display ="none"
                    return
                }
                error.style.display ="block"

            }

		}
	}
</script>