<template>
	<div id="flatMenu" @click="toggleSubMenu(),toggleOverFlow()">
		<div id="flatMenuWrapper" @click='prevent'>
			<ul>
			    <li>	
			    	<a href="#">دسته 1</a>
			    </li>
			    <li>
			    	<a href="#">کسیه پر کن</a>
				</li>
			    <li>
			    	<a href="#">دستگاه برش چسب</a>
				</li>
			    <li>
			    	<a href="#">کابل کئوکسال</a>
				</li>
				<li>
			    	<a href="#">شرینک پد</a>
				</li>
				<li>
			    	<a href="#">جت پرینتر</a>
				</li>
				<li>
			    	<a href="#">باند رول</a>
				</li>
				<li>
			    	<a href="#">تسمه کش</a>
				</li>
				<li>
			    	<a href="#">دستگاه توزین</a>
				</li>
				<li>
			    	<a href="#">پالت استرچ </a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته کشاورزی</a>
				</li>
				<li>
			    	<a href="#">کابل کئوکسال</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته کشاورزی</a>
				</li>
				<li>
			    	<a href="#">کابل کئوکسال</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته کشاورزی</a>
				</li>
				<li>
			    	<a href="#">کابل کئوکسال</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته کشاورزی</a>
				</li>
				<li>
			    	<a href="#">کابل کئوکسال</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				<li>
			    	<a href="#">دسته 5</a>
				</li>
				
			</ul>
		</div>
	</div>
</template>

<style scoped>
	
	#flatMenu{
		background: white;
		position: absolute;
		z-index:668;
		top:0;
		background: rgba(0,0,0,0.5);
		width:100%;
		height:100%;
		display:flex;
		justify-content: center;

	}
	#flatMenuWrapper{
		padding: 10px;
		background: rgb(20,40,80);
		padding-right: 0;
		position: absolute;
		line-height: 2rem;
		width:90%;
		height: 400px;
		display:flex;
		flex-wrap: nowrap;
		width:max-content;
		right:0;
		top:0;
		bottom:0;
		overflow: scroll;
		
		
	}
	ul{
		direction: rtl;
		display:flex;
		width:100%;
		flex-direction: column;
		max-height: 100%;
		justify-content: flex-end;
		flex-wrap: wrap;
		position: relative;
		display:flex;
		flex-direction:column;
		align-items: flex-end;
		justify-content: flex-start;
		max-height: max-content;
		flex-wrap: nowrap;
		height:100%
	}
	li{
		cursor: pointer;
		position: relative;
		margin-top:5px;
		padding:5px;
		transition: all 0.5s linear;
		text-align:right;
		width:100%
	}
	li a{
		position: relative;
		color:white;
	}
	li a:before,
	li a:after {
		background-color: red;
	} 
	
	li a:hover:before,li:hover a:before{
		transform:scaleX(1)
	}
	li a:before{
		content:'';
		position:absolute;
		top:0;
		left:0;
		width:100%;
		height:2px;
		transform: scaleX(0);
		transition:all 0.5s ;
		transform-origin: left;
	}
	li a:after{
		content:'';
		position:absolute;
		bottom:0;
		left:0;
		width:100%;
		height:2px;
		transform: scaleX(0);
		transition:all 0.5s ;
		transform-origin: right;
	}
	li:hover a:before,li:hover a:after{
		transform:scaleX(1)
	}
	.subMenu:hover{
		display: block
	}
	@media (max-width: 924px){
		#flatMenuWrapper{
			width:max-content;
			right:0;
			top:0;
			bottom:0;
			overflow: scroll;
			height:100vh
		}
		#flatMenuWrapper ul{
			height:100%;

		}
		#flatMenu{
			display: flex;
			align-items: flex-start;
			max-height: max-content;
		}
		ul{
			display:flex;
			flex-direction:column;
			align-items: flex-end;
			justify-content: flex-start;
			max-height: 100%;
			flex-wrap: nowrap;
			height:100%
		}
		li{
			height: max-content;
			line-height: 3em;
			width:100%;
			text-align:right
		}
		li:nth-child(odd)
		{
			border-left: 0
		}
		li:nth-child(even)
		{
			border-left: 0
		}

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
				console.log(e)
				e.stopPropagation();
				e.preventDefault();
				
				
			},
			toggleOverFlow(){
				this.toggleBodyOverFlow()
			}

		},
		mounted(){
			this.adjustFromTop(document.querySelector("#flatMenuWrapper"))
			this.toggleBodyOverFlow('hidden')
			window.addEventListener("resize",()=>{
				if(window.innerWidth>801)
				{
					this.toggleBodyOverFlow()
				}
			})

		}
		
		
	}


</script>