<template>
	<div id="footer">
		
		<div id="footerWrapper" class='maxIs'>
			<div class="newsTake">
				<form>
					<p>برای دریافت اخرین قیمت ها ایمیل خود را وارد کنید</p>
					<input autocomplete="off" type="text" placeholder="example@gmail.com" name="email">
					<button class='submit'>ثبت</button>
				</form>
			</div>
			<div class="aboutUs">
				<a href="#">در باره  ما</a>
			</div>
			<div class="phoneNum">
				<p>جهت دریافت اطلاعات با مما تماس بگیرید:</p>
				<p>021-35791862</p>
			</div>
		</div>
	</div>

</template>


<style scoped>
	input{
		border:1px solid rgb(184, 184, 184);
		padding:5px;
		border-radius:10px;
		direction: ltr;
		color:black
	}
	#footerWrapper{
		display: flex;
		width: 95%;
		padding:50px;

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

</style>


<script>
	
	export default{

	}
</script>