<template>
	<div id="footer">
		
		<div id="footerWrapper" class='maxIs'>
			<div class="firstRow">
				<mega></mega>
			</div>
			<div class="secondRow">
				<mission></mission>
				<abouts></abouts>
				<sign-up></sign-up>
				<cont></cont>


				
			</div>
			<div id="slicer"></div>

			<div id="thirdRow">
				<p>شرایط استفاده</p>
				<p>حریم خصوصی</p>
				<p>تقشه سایت</p>
				
			</div>
			
			



		</div>
		<p class="copy">تمام حقوق این سایت متعلق به دمیرکو است &#169;</p>
	</div>

</template>


<style scoped>
.copy{
	text-align:center
}
#thirdRow{
	display: flex;
	justify-content: center;
	flex-wrap: wrap;
}
#thirdRow p{

	margin: 15px
}
.copy{
	margin:auto;
}
	#slicer{
		width: 90%;
    margin: auto;
    height: 3px;
    background-color: #9f9f9f;
	}
	input{
		border:1px solid rgb(184, 184, 184);
		padding:5px;
		border-radius:10px;
		direction: ltr;
		color:black
	}
	#footerWrapper{
		display: flex;
		flex-direction: column;
		padding:10px;
		width:100%;
		justify-content: space-between;
	}
	form input,form button
	{
		margin-top: 10px;
	}
	#footer{
		display: flex;
		flex-direction: column;
		align-items: center;
		background: #f6f6f4;
		border-top:1px solid #d9d8d8;
		
		/* position: relative; */
	}
	#footer p,#footer a{
		color:black
	}
	a:hover{
		text-decoration:underline;
	}
	form{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.phoneNum p{
		text-align:center;
		color:black
	}
	p{
		color:black
	}
	@media (max-width: 1120px)
	{
		#footerWrapper{
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		form p{
			text-align: center;
		}
		#footer{
			padding-bottom:30px
		}
		#footerWrapper > div{
			margin-top: 20px;
		}
	}
	.secondRow{
		display: flex;
		flex-wrap: wrap;
		justify-content:space-evenly;

		margin-top:50px;
	}



</style>


<script>
	import mega from "./menu.vue"
	import cont from "./contact/contact.vue"
	import signUp from "./signUp/signUp.vue"
	import mission from "./mission/mission.vue"
	import abouts from "./abouts/abouts.vue"
	
	export default{
		components:{
			mega,
			cont,
			signUp,
			abouts,
			mission
		}
	}
</script>