<template>
	<div class="card">
		<div class="titleCard"><p>{{cardTitle}}</p></div>
		<!-- <div @click='goToLeft()' class="left"><img src="/images/left.png" alt=""></div>
		<div @mousemove="mouseMove($event)" @mouseup="mouseup($event)" @mouseleave="mouseleave($event)" @mousedown="mouseDown($event)" class="cardWrapper">
			
				<div class="cardItem" :id='index' v-for='(p,index) in JSON.parse(products)' :key='index'>
					<div class="productImage">
						<img :src="getUrl(p)" alt="">
					</div>
					<div class="productTitle">
						<a href="#"><p>خط تولید مشاین لباسش شویی تمم اتومات</p></a>
					</div>
					<div class="productDesc">
						<p>{{getDesc(p.desc)}}</p>
					</div>
					<div class="productContinue">
						<a href="#"><button class=continue>ادامه مطلب</button></a>
					</div>
				</div>
				
		</div>
		<div @click='goToRight()' class="right"><img src="/images/left.png" alt=""></div> -->
		<!-- <div class="my-slider">
			<div><img src="/images/1.jpg" alt=""></div>
			<div><img src="/images/2.jpg" alt=""></div>
			<div><img src="/images/3.jpg" alt=""></div>
			<div><img src="/images/4.jpg" alt=""></div>
			<div><img src="/images/5.jpg" alt=""></div>
			<div><img src="/images/6.jpg" alt=""></div>

		</div> -->
		<div class="splide">
			<div class="splide__track">
				<ul class="splide__list">
					<li class="splide__slide">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img src="/images/bandRole.png" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a href="#"><p>اب چسب</p></a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<button class="done">مشاهده</button>
									</div>
								</div>
							</div>
						</div>
					
					</li>
					
					<li class="splide__slide">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img src="/images/abchasb.png" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a href="#"><p>اب چسب</p></a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<button class="done">مشاهده</button>
									</div>
								</div>
							</div>
						</div>
					
					</li>

					<li class="splide__slide">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img src="/images/htest2.jpg" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a href="#"><p>اب چسب</p></a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<button class="done">مشاهده</button>
									</div>
								</div>
							</div>
						</div>
					
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
<script>	
    export default{
		props:['cardTitle','descs','products'],
		data(){
			return{
				container:null,
				isDown:false,
				startX:null,
				scrollLeft:null,
				glide:null
			}
		},
		data(){
			return{
				perShow:2
			}
		},
		mounted(){
			this.container=document.querySelector('.cardWrapper');
			let per=window.addEventListener("resize",this.adjustSplitejs)
			this.adjustSplitejs()
			const glide=new Splide( '.splide',{
					type   : 'loop',
					perPage: this.per,
					perMove: 1,
				} );
				glide.mount()
			
			
			
		},
        methods:{
			adjustSplitejs(){
				if(window.innerWidth<=730){
					this.perShow=1
				}else{
					this.perShow=2
				}
				return this.perShow
					
			},
            getUrl(p){
                return p.url
            },
            getDesc(desc){
                console.log(desc.substring(0,30).length)
                return desc.length>30 ? desc.substring(0,100)+"..." : desc
			},
			mouseDown(e){
				this.isDown=true
				this.container.classList.add("active")
				this.startX=e.pageX-this.container.offsetLeft
				this.scrollLeft=this.container.scrollLeft
			},
			mouseleave(){
				this.isDown=false
				this.container.classList.remove("active")
			},
			mouseup(){
				this.isDown=false
				this.container.classList.remove("active")
			},
			mouseMove(e){
				if(!this.isDown) return
				e.preventDefault();
				const x=e.pageX-this.container.offsetLeft
				const walk=x-this.startX
				this.container.scrollLeft=this.scrollLeft-walk
				console.log(walk)
			},
			goToLeft(){
				console.log("left")
				this.sideScroll(this.container,'left',25,220,10)
			},
			goToRight(){
				this.sideScroll(this.container,'right',25,220,10)
			},
			sideScroll(element,direction,speed,distance,step){
				let scrollAmount = 0;
				var slideTimer = setInterval(()=>{
					if(direction == 'left'){
						element.scrollLeft -= step;
					} else {
						element.scrollLeft += step;
					}
					scrollAmount += step;
					if(scrollAmount >= distance){
						window.clearInterval(slideTimer);
					}
				}, speed);
			}
		}
    }
	
</script>



<style scoped>
	.right{
		right:0;
	}
	.left{
		left:0;
	}
	.right,.left{
		background: rgba(211, 110, 28, 0.801);
		position:absolute;
		top:50%;
		border-radius: 50%;
		display:flex;
		justify-content: center;
		align-items: center;
		width:45px;
		height: 30px;
	}
	.right{
		transform: rotate(180deg);
	}
	.right img,.left img{
		width:30px;
		height:20px;
	}
    .titleCard{
        padding:5px 0 5px 0;
		background: rgb(60,134,199);
		padding:10px;
		color:white;
		width:max-content;
		font-size:18pt;
		border-top-left-radius: 20px;
		border-top-right-radius: 20px;
    }
	.cardWrapper{
		display: flex;
		overflow-y: hidden;
        overflow-x: scroll;
		scrollbar-width: none;
		margin-top:10px;
		font-weight: lighter;
		
	}
	.cardWrapper::-webkit-scrollbar{
		display:none
	}
	.card{
		box-shadow: 0px 2px 5px 0 rgba(0,0,0,0.2);
		border-top-left-radius: 20px;
		margin-top:20px;
        overflow: auto;
        width:100%;
		position: relative;
		display: flex;
		/* align-items: flex-end; */
		flex-direction: column;
    }
    .cardItems{
        padding:30px
    }
	.cardItem{
		display: flex;
		flex-direction: column;
        align-items: center;
		padding:10px;
    }
    
	.cardItem p{
		word-break: keep-all;
	}
	.productDesc{
		width: 250px;
		min-height: 100px;
		margin-top:5px;
		
	}
	.productTitle{
		width: 250px;
		margin-top:5px;
	}
	.productTitle p{
		color:rgb(34, 105, 122)
	}
	.productImage{
		width: 250px;
		height: 230px;
	}
	
	img{
		width: 250px;
		height: 230px;
		border-top-left-radius: 10px;
		border-top-right-radius: 10px;
	}
	.active{
		cursor: grabbing;
	}
	.cardWrapper:hover{
		cursor: grabbing;
	}
	.singleSlide{
		width:300px;
		margin-top:10px;
		

	}
	.singleSlide img{
		width:300px;
	}
	.singleSlide .descsP{
		height:120px;
	}
	.descsP p{
		color:#707070;
		font-weight:bold
	}
	.splide__slide{
		background: rgb(233, 233, 233);
		padding:10px;
	}
	.title a{
		color:rgb(56, 56, 255)
	}
	.title{
		margin-top:5px;
		margin-bottom:5px
	}
	.splide--draggable>.splide__track>.splide__list>.splide__slide {
    -webkit-user-select: none;
    user-select: none;
    display: flex;
    justify-content: center;
}
.splide{
	border-top:2px solid rgb(60,134,199);
	margin-top:3px

}
	

	
</style>