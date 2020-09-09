<template>
	<div class="card">
		
		<div class="splide">
			<div class="titleCard"><p>{{cardTitle}}</p></div>
			<div class="splide__track">
				<ul class="splide__list">
					<li class="splide__slide" v-for="(p,index) in products">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img :src="getImage(p.product_image)" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a class="link" href="#">{{p.title}}</a>
									</div>
									<div class="descsP">
										<p>{{p.description}}</p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
										<p>{{p.price || 0}}  تومان</p>
									</div>
								</div>
							</div>
						</div>
					
					</li>
					
					<!-- <li class="splide__slide">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img src="/images/abchasb.png" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a class="link" href="#">اب چسب</a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
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
										<a class="link" href="#">اب چسب</a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
									</div>
								</div>
							</div>
						</div>
					
					</li><li class="splide__slide">
						<div class="singleSlide">
							<div class="singleSlideWrapper">
								<div class="img">
									<img src="/images/bandRole.png" alt="">
								</div>
								<div class="descs">
									<div class="title">
										<a class="link" href="#">اب چسب</a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
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
										<a class="link" href="#">اب چسب</a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
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
										<a class="link" href="#"><p>اب چسب</p></a>
									</div>
									<div class="descsP">
										<p>فلان لان فلان لان للللللللان فلانل الن انل نفنلفننفئ لئفنئ لئنفثنئل </p>
									</div>
									<div class="link">
										<a class="submit">مشاهده</a>
									</div>
								</div>
							</div>
						</div>
					
					</li> -->
				</ul>
			</div>
		</div>
	</div>
</template>
<script>	
    export default{
		props:['products'],
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
			let per=this.reCalculatePer()
			const glide=new Splide( '.splide',{
					type   : 'loop',
					perPage: per,
					perMove: 1,
				} );
				glide.mount()
				window.addEventListener("resize",()=>{
					let pper=this.reCalculatePer()
					glide.options.perPage=pper
				})
				
				// glide.on('resize',()=>{
				// 	let per=this.reCalculatePer()
					
				// 	glide.options.perPage=per
				// })
			
			
			
		},
        methods:{
			reCalculatePer(){
				let per=2
					let width=window.innerWidth
					if(width>=1100){
						per=4
					}
					else if(width<=1099 && width>=851){
						per=3
					}else if(width<=850 && width>=600){
						per=2
					}else if(width<=599){
						per=1
					}
					return per
					
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
			},
			getPrice(p){
				// return "hey"
				let price=p || p.toString().split("")
				let c=0
				const newPrice=[]
				for (let i=price.length-1;i>0;i--){
					newPrice.push(price[i])
					c++
					if(c==3){
						newPrice.push(",")
						c=0
					}
				}
				return newPrice.reverse().join("")
			},
			getImage(img){
				console.log(img)
				return '/images/کیسه-پر-کنCBE-NWB-300x300.png'
			}
		}
    }
	
</script>



<style scoped>
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
		width:280px;
		margin-top:10px;
	}
	.link{
		display: flex;
    justify-content: space-between;
    align-items: center;
	}
	.singleSlide img{
		width:280;
	}
	.img{
		display:flex;
		justify-content: center;
	}
	.singleSlide .descsP{
		height:120px;
	}
	.descsP p{
		color:#707070;
		font-weight:bold
	}
	.splide__slide{
		padding:10px;
	}
	.title{
		margin-top:5px;
		margin-bottom:5px;
		display:flex;
		justify-content: flex-end;
	}
	.splide--draggable>.splide__track>.splide__list>.splide__slide {
    -webkit-user-select: none;
    user-select: none;
    display: flex;
	justify-content: center;
	margin-top:20px;
	margin-bottom:10px
}
.splide{
	margin-top:3px

}
	

	
</style>