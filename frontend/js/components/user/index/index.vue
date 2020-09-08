<template>
	<div id="index" class='mainItemPerPage'>
		<div id="topOfIndex">
			<div id="topOfIndexWrapper">
				<slider></slider>
				<categorie></categorie>
				
			</div>
			
		</div>
		<flip-card></flip-card>
		<!-- <expanding-card></expanding-card> -->
		
		<!-- <extra-sign-up></extra-sign-up> -->
		<div id="allCards" class='shouldCollapse maxIs'>
			<card cardTitle="بیشترین کلیک شده" descs='فلان لان فلان خیلی فلا هی فلان بازم فلان' :products='getProducts()'></card>
			
		</div>
		<div class="digiCardIndex shouldCollapse maxIs">
			<digi-card :imgs='JSON.stringify(["/images/shrink.png","/images/shrink2.png","/images/digi1.jpg","/images/digi2.jpg"])'></digi-card>
		</div>
	</div>
</template>
<script>
	import digiCard from "./digiCard/digiCard.vue"
	import slider from "./slider/slider.vue"
	import card from './card/card.vue'
	import flipCard from './flipCard/flipCard.vue'
	import categorie from './categorie/categorie.vue'
	import expandingCard from './expandingCard/expandingCard.vue'
	import extraSignUp from "./extraSignUp/extraSignUp.vue"
	export default{
		components:{
			slider,
			card,
			categorie,
			flipCard,
			digiCard,
			extraSignUp,
			expandingCard
		},
		props:['products','main_categories','posts'],
		data(){
			return{
				products:[{desc:'محصل فلانئ ئنیسئب ئنئ ثنصئب نئنئ ئن ئنئنئنئنئنئنئنئنئنئنئن و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"},{desc:'محصل فلان و فلان وفلان',url:"/images/a.jpg"}]
			}
		},
		methods:{
			getProducts(){
				return JSON.stringify(this.products)
			}
		}
		
	}
</script>

<style>
	.digiCardIndex{
		margin-top:20px;
		margin-bottom: 20px;
	}
	#topOfIndex{
		background: #ffffff;
	}
	#topOfIndexWrapper{
		display:flex;
		justify-content: center;
		widTH:100%;
		padding:20px;
	}
	#index{
		position: relative;
	}
	#allCards{
		display: flex;
		width:100% ;
		flex-direction: column;
		align-items: center;
	}
	#mostClicked{

		grid-area: mostClicked;
	}
	#slider{
		grid-area: slide
	}
	#new{
		grid-area: new;
	}

	#app{
		display: grid;
		width: 100%;
		grid-template-columns: repeat(2,1fr);
		grid-template-rows: fit-content(1000rem) auto auto auto fit-content(1000rem);
		grid-template-areas: 
		'header header'
		'slicer slicer'
		'navigation navigation'
		'main main'
		'footer footer'
	}
	.titleCard{
		display: flex;
		width:100%;
		justify-content: flex-end;
	}


	#index{
			display: flex;
			flex-direction: column;
			align-items: center;

		}

	#flatMenu{
		grid-area: flatMenu
	}


	.singleCard{
		background: white;
	}

	#footer{
		grid-area: footer
	}
	.hamCats{
		grid-area:hamCats
	}
	@media (max-width:924px)
	{
		#slider{
			width:100%;

		}
		#sideSliderCats{
			display:none
		}
	}
	@media (max-width:800px){
		#topOfIndexWrapper{
			padding:0
		}
	}


</style>


