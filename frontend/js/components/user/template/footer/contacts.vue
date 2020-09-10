<div>
	<div id="contactUs">
		<div id='contactUsWrapper'>
				<div id="emailAndPhone">
					<div emailAndPhoneWrapper>
						<p>تماس با ما</p>
						<p>021-77569156,77542719</p>
						<p>info@damirco.com</p>
					</div>
				</div>
				<div class="icons">
					<div class="iconsWrapper">
						<div class="linkdin">
							<linkdin class="singleIcon"></linkdin>
						</div>
						<div class="instagram">
							<insta class="singleIcon"></insta>
						</div>
						<div class="watsApp">
							<wats-app class="singleIcon"></wats-app>
						</div>
					</div>
				</div>
		</div>
	</div>
</div>
<style scoped>
	.icons{
		display: flex;
	}
	.singleIcon{
		width: 50px;
		height: 50px
	}

</style>

<script>
	import linkdin from "./linkdin.vue"
	import insta from "./instagram.vue"
	import watsApp from "./watsApp.vue"
	export default{
		components:{
			linkdin,
			insta,
			watsApp
		}
	}

</script>