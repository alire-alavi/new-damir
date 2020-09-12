export const adjustElFromTop={
    methods:{
        adjustFromTop(el,changeElHeight=true){
        	if(changeElHeight){
        		el.style.height='100vh'	
        	}
            
            el.style.top=window.scrollY+'px'
        }
    }
}