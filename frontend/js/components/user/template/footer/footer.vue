<template>
	<div id="footer">
		
		<div id="footerWrapper" class='maxIs'>
			<mega></mega>
			<contacts></contacts>
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

</style>


<script>
	import mega from "./menu.vue"
	import contacts from "./contacts.vue"
	
	export default{
		components:{
			mega,
			contacts
		}
	}
</script>