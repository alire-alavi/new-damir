<template>
	<div id="slider">
		<div id="sliderWrapper">
			<div class="active slide">
				<img src="/images/ec1.png" alt="">
				<div class="container">
					<div class="containerWrapper">
						<p>شرینگ پک</p>
						<!-- <p>انواع شرینگ پک فلان فلان فلانف فلان</p> -->
						<button class='submit'>مشاهده</button>
					</div>
				</div>
			</div>
			<div class="slide">
				<img src="/images/ec2.png" alt="">
				<div class="container">
					<div class="containerWrapper">
						<p>شرینگ پک</p>
						<!-- <p>انواع شرینگ پک فلان فلان فلانف فلان</p> -->
						<button class='submit'>مشاهده</button>
					</div>
				</div>
			</div>
		</div>
		<div class="indicators" >
			<div :id='index+1' v-for="(item,index) in slides" v-if='index==0' class='active' :key="index" @click='indicateSlide($event)'>{{index+1}}</div>
			<div :id='index+1' v-else @click='indicateSlide($event)'>{{index+1}}</div>

		</div>
		<div class="controlls">
			<div class="pre" @click="pre()"><svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(180)"></path></svg></div>
			<div class="next" @click='next()'><svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(180)"></path></svg></div>
		</div>
	</div>
</template>

<script>
	export default {
		mounted(){
			this.slides=document.querySelectorAll(".slide")
			this.ind=document.querySelector(".indicators")
			this.inter=setInterval(this.autoPlay,5000)
		},
		data(){
			return{
				slides:null,
				index:0,
				isMount:false,
				ind:null,
				inter:null
			}
		},
		methods:{
			pre(){
				if(this.index==0)
				{
					this.index=this.slides.length-1
				}else{
					this.index--
				}
				this.changeSlide()
				this.updateCircleIndicator()
				this.resetAutoPlay()
			},
			next(){
				if(this.index==this.slides.length-1)
				{
					this.index=0
				}else{
					this.index++
				}
				this.changeSlide()
				this.updateCircleIndicator()
				this.resetAutoPlay()
			},
			changeSlide(){
				for(let i=0;i<this.slides.length;i++){
					this.slides[i].classList.remove("active")
				}
				this.slides[this.index].classList.add("active")
			},
			indicateSlide(e){
				this.index=e.target.id-1
				this.changeSlide()
				this.updateCircleIndicator()
				this.resetAutoPlay()
			},
			updateCircleIndicator(){
				for(let i=0;i<this.ind.children.length;i++){
					this.ind.children[i].classList.remove('active')
				}
				this.ind.children[this.index].classList.add("active")
			},
			autoPlay(){
				this.next()
				this.updateCircleIndicator()
			},
			resetAutoPlay(){
				clearInterval(this.inter)
				this.inter=setInterval(this.autoPlay,4000)
			}
			
		},
	}	
</script>

<style scoped>
	.controlls .pre,.controlls .next{
		position: absolute;
		top:50%;
		height:50px;
		width:50px;
		cursor:pointer;
		z-index:2;
		background-color: hsla(0, 0%, 100%, 0.75);
		border-radius: 50%;
		transition:all 0.5s ease;
		text-align: center;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.pre{
		transform:rotateY(180deg)
	}
	svg{
		width:40px;
		height:40px
	}
	.next{
		right:0
	}
	
	img{
		width:100%
	}
	#sliderWrapper{
		display:flex;
		justify-content: center;
		overflow: hidden;
	}
	.slide{
		position: relative;
		
		display:none;
		animation: slide 2s ease;
	}
	.slide,#slider{
		max-height: max-content;
	}
	#slider{
		position:relative;
		width:688px;
		max-height:max-content;
		background-color: #ffffff
	}
	.container{
		position:absolute;
		top:50%;
		left:50%;
		transform:translateX(-50%) translateY(-50%)
		
	}
	.containerWrapper{
		display:flex;
		flex-direction:column;
		align-items: center;
		padding:20px
	}
	.container p{
		font-size:18pt;
		font-weight: lighter;
		
	}
	.slide.active p{
		opacity:0;
		animation:captionTextAn 0.5s linear forwards;
		animation-delay: 1.2s;
		color:white;
		margin-bottom:10px
	}
	.slide.active .container{
		animation:fadeTrans 1s linear forwards;
		animation-delay: 1.5s;
	}
	@keyframes fadeTrans {
		0%{
			background: transparent;
		}
		100%{
			background: rgba(0, 0, 0, 0.7);
		}
	}
	.slide.active button{
		opacity:0;
		animation:captionTextAn 0.5s linear forwards;
		animation-delay: 1.4s;
	}
	@keyframes captionTextAn{
		from {
			opacity:0;
			transform:translateX(-100px)
		}
		to{
			opacity:1;
			transform:translateX(0px)

		}
	}

	
	.slide.active{
		display:flex
	}
	.container p:nth-child(2){
			font-size:12pt
		}
	@keyframes slide{
		0%{
			opacity:0.2;
			transform: scale(1.2);
		}
		100%{
			opacity:1;
			transform:scale(1)
		}
	}
	@media (max-width:650px){
		.container p,.container button{
			font-size:12pt;
			font-weight: lighter;
		}
	}
	@media (max-width:924px)
	{
		#slider{
			width:100%;
			
		}
		img{
			object-fit: contain;
			height:auto;
		}
	}
	.indicators{
		position: absolute;
		left:50%;
		bottom:15px;
		z-index:667;
		transform:translateX(-50%)
	}
	.indicators div{
		display:inline-block;
		width:25px;
		height:25px;
		color:#ffffff;
		background-color: rgb(11,111,211);
		border-radius: 50%;
		text-align: center;
		margin:0 10px;
		cursor:pointer;
		transform:translateX(-50%)
	}
	.indicators div.active{
		background-color: black;
	}
	
</style>