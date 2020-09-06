export const toggleDoneMessage={
    methods:{
        toggleDoneMessage(){
            const donemes=document.querySelector("#doneMessage")
            donemes.style.display='block'
            setTimeout(()=>{
                donemes.style.display='none'
            },5000)
        }
    }
}