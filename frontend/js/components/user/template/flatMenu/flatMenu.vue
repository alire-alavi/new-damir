<template>
	<div id="flatMenu" @click="toggleSubMenu(),toggleOverFlow()">
		<div id="flatMenuWrapper" @click='prevent'>
			<ul>
			    <li>	
			    	<div class="link" @click="openMySubMenu($event)">
			    		
			    		<svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(180deg)"></path></svg>
			    		<p>دسته 1</p>
			    	</div>
			    	

			    	<ul class="subMenu">
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    	</ul>
			    </li>
			    <li>
			    	<div class="link">
			    		
			    		<svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(270deg)"></path></svg>
			    		<p @click="openMySubMenu($event)">دسته 1</p>
			    	</div>
			    	<ul class="subMenu">
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    	</ul>
				</li>
			    <li>
			    	<div class="link">
			    		
			    		<svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(270deg)"></path></svg>
			    		<p @click="openMySubMenu($event)">دسته 1</p>
			    	</div>
			    	<ul class="subMenu">
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    	</ul>
				</li>
			    <li>
			    	<div class="link">
			    		
			    		<svg viewBox="0 0 100 100"><path d="M 50,0 L 60,10 L 20,50 L 60,90 L 50,100 L 0,50 Z" class="arrow" transform="translate(85,100) rotate(270deg)"></path></svg>
			    		<p @click="openMySubMenu($event)">دسته 1</p>
			    	</div>
			    	<ul class="subMenu">
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    		<li>زیر دسته یک</li>
			    	</ul>
				</li>
				
			</ul>
		</div>
	</div>
</template>

<style scoped>
	#flatMenu{
		position: absolute;
		width:100%;
		top:0;
		bottom:0;
		background:rgba(0,0,0,0.5);
		z-index:669
	}
	#flatMenuWrapper{
		position:absolute;
		width:max-content;
		background:#f6f6f4;
		height:100vh;
		z-index:670;
		right:-100%;
		width:max-content;
		transition: all 1s;
		overflow: auto;

	}
	ul{
		padding:10px;
		line-height: 2rem
	}
	li{
		text-align: right;
		position:relative;
		margin-top: 5px;
		margin-bottom: 5px
	}
	.subMenu{
		background-color: #dfdfdf;
		width:100%;
		padding:0;
		height:0;
		overflow: hidden;
	}
	.subMenu li{
		padding:5px;
	}
	svg{
		width:15px;
		height: 15px;
		transform: rotate(-90deg);
	}
	.link{
		display: flex;
    	justify-content: space-between;
    	align-items: center;
	}


</style>

<script>
	import {mapActions} from "vuex"
	import {toggleBodyOverFlow} from "../../mixIns/toggleBodyOverFlow.js"
	import {adjustElFromTop} from '../../mixIns/adjustElFromTop.js'
	export default{
		mixins:[toggleBodyOverFlow,adjustElFromTop],
		methods:{
			...mapActions([
				'toggleSubMenu'
			]),
			prevent(e){
				e.stopPropagation();
				e.preventDefault();
				
				
			},
			toggleOverFlow(){
	
				this.toggleBodyOverFlow()
			},
			openMySubMenu(e){
				const parentEl=e.target.parentNode
				const next=parentEl.nextElementSibling
				const allSubs=document.querySelectorAll('.subMenu')
				allSubs.forEach( sub=>{
					sub.style.height=0
				});
				const height = getComputedStyle(next).height
				console.log(height )
				if(height=="0px"){
					next.style.transition = "all 0.4s linear"
					next.style.height = 'max-content'
				}else{
					next.style.height = 0
				}
				
				console.log(parentEl,)
			}

		},
		mounted(){
			const menuWrapper=document.querySelector("#flatMenuWrapper")
			this.adjustFromTop(menuWrapper)
			this.toggleBodyOverFlow('hidden')
			menuWrapper.style.right="0"
			window.addEventListener("resize",()=>{
				if(window.innerWidth>801)
				{
					this.toggleBodyOverFlow()
				}
			})

		}
		
		
	}


</script>