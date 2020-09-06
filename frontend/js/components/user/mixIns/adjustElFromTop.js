export const adjustElFromTop={
    methods:{
        adjustFromTop(el){
            console.log(el)
            el.style.height='100vh'
            el.style.top=window.scrollY+'px'
        }
    }
}