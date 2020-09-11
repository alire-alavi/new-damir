<template>
	<div id="contactUsSection">
		<div id='contactUsSectionWrapper'>

			<div class="contatUsItems">
				<div class="detail">
					<div class="detailWrapper">
						<p>تماس با ما</p>
						<p>021-77569156,77542719</p>
						<p>info@famirco.com</p>
					</div>

				</div>
				<div class="icons">
					<div class="iconsWrapper">
						<a href="#"><inst></inst></a>
						<a href="#"><linkd></linkd></a>
						<a href="#"><watsapp></watsapp></a>
					</div>
				</div>
				<div class="subscribe">
					<div class="subscribeWrapper">
						<p>برای دریاف اخرین قیمت ها ایمیل خود را وارد کنید</p>
						<form>
							<div id="email" class="inputs">
				              <div class="formInputsWrapper">
				                <input autocomplete="off" @blur="focusOut($event),startValidation('email',$event)" class="signupFormInputs inputWithLabelThatShouldStay" id="userEmail" type="text"/>
				                <label class="comeUpLabel" for="userEmail">ایمیل</label>
				              </div>
				              <p class="inputError">فرمت ایمیل اشتباه است</p>
				            </div>
				            <button class="submit">تایید</button>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<style scoped>
.subscriveWrapper{
	    display: flex;
    flex-direction: column;
    align-items: center;
}
.subscribeWrapper > p{
	width: 200px;
	text-align: center;
	margin:20px;
}
.detailWrapper{
	display: flex;
    flex-direction: column;
    align-items: center;
}
	.icons{
		display: flex;
	}
	.singleIcon{
		width: 50px;
		height: 50px
	}
	.contatUsItems{
		display: flex;
		flex-direction: column;
		align-items: center;

	}
	p{
		line-height: 2rem
	}
	.iconsWrapper{
		display: flex;
		width: 170px;
		justify-content: space-between;
	}
	form{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.formInputsWrapper{
		margin-top:-15px;
	}
	#contactUsSection{
		margin: 20px
	}

</style>

<script>
	import inst from "./instagram.vue"
	import linkd from "./linkdin.vue"
	import watsapp from "./watsApp.vue"
	import {keepStay} from "../../../mixIns/keepStay.js"
    import {validationRules} from "../../../mixIns/validationMixIn.js"
	export default{
		name:"contact",
		mixins:[keepStay,validationRules],
		components:{
			inst,
			linkd,
			watsapp
		},
		methods:{
			startValidation(type,e){
                const el=e.target
                const parentNode=e.target.parentElement
            
                const error=parentNode.nextElementSibling
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