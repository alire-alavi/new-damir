<template>
	<div id="header" >
		<div id="headerWrapper" class="maxIs">
			<div class="logo">
				<img src="/images/logo.jpg" alt="">
			</div>
			<div class="searchBar">
				<div id="searchBarWrapper">
						<form>
							<input type="" placeholder="جست و جو ..." name="">
							<button class='magnifier'>
								<img src="/images/mag.png" alt="">
							</button>
						</form>
				</div>
			</div>
			<div class="phone">
				<p>تلفن :3579514862-021</p>
			</div>

		</div>
	</div>
</template>

<style scoped>
	#header{
		width: 100%;
		background:#f6f6f4;
		display: flex;
		justify-content: center;
	}
	p{
		color:black
	}
	#headerWrapper{
		width: 95%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#searchBarWrapper{
		padding:5px;
		display: flex;
		
		
	}
	
	.magnifier img{
		height: 20px;
		width: 20px;
	}
	form{
		display: flex;
		align-items: center;
		border:2px solid rgb(9,111,211);
		border-radius:28px;
		
	}
	input{
		
		border: 0;
		min-width: 0;
		flex: 1;
		color: black;
		padding: .5rem 1rem;
		border-top-left-radius: 27px;
		border-bottom-left-radius: 27px;
		border-top-right-radius: 0;
		border-bottom-right-radius: 0;
		height:100%;
	}
	::placeholder {
  		color: black;
  		opacity: 1; 
	}
	.magnifier{
		border: 0;
		border-top-right-radius: 27px;
		border-bottom-right-radius: 27px;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		background-color:#ffffff;
		padding: 0 22px 0 18px;
		padding:10px;
		display: flex;
		justify-content: center;
		height: 100%;
	}
	.logo{
		max-width:270px;

	}
	.logo img{
		width:100%
	}
	@media  (max-width: 833px)
	{
		#headerWrapper{
			display: flex;
			flex-direction: column;
		}
		#headerWrapper div
		{
			margin-top: 20px
		}
		.phone
		{
			margin-bottom: 20px;
		}
	}

</style>

<script>

</script>